from django.db import models
from django.db.models import Q
from django.core.validators import MaxValueValidator, MinValueValidator
from field_history.tracker import FieldHistoryTracker

from accounts.models import User
from .managers import QuoteManager
from decimal import Decimal


class Policy(models.Model):
    STATUS = (
        (1, "New"),
        (2, "Quoted"),
        (3, "Active Policy"),
        (4, "Archived"),
    )
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
 
    status = models.IntegerField(
        choices=STATUS,
        default='1',
    )
    description = models.TextField(blank=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]
        indexes = [
            models.Index(fields=["id", "slug"]),
            models.Index(fields=["name"]),
            models.Index(fields=["-created"]),
        ]

    def __str__(self):
        return  "{}".format(self.slug)


class AgeGroupPolicy(models.Model):
    """This class holds the different age groups of personas"""

    policy = models.ForeignKey(
        Policy, on_delete=models.CASCADE, related_name="policies"
    )
    age_from = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(120),
                    MinValueValidator(0)]
    )
    age_to = models.IntegerField(
        default=0, validators=[
            MaxValueValidator(120),
            MinValueValidator(0)]
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="this is the price per 100 unit coverage per annum")
    charge = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)],
        help_text="Percentage value (0 to 100)",
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Age Groups"
        ordering = ["price"]
        indexes = [
            models.Index(fields=["id"]),
            models.Index(fields=["-created"]),
        ]

    def __str__(self):
        return "{} to {}".format(self.age_to, self.age_from)




class Quote(models.Model):
    STATUS = (
        (1, "New"),
        (2, "Quoted"),
        (3, "Accepted"),
        (4, "Active Policy"),
        (5, "Archived"),
    )
    customer = models.ForeignKey(User,
                                 related_name='quotes',
                                 on_delete=models.CASCADE)
    policy = models.ForeignKey(Policy,
                               related_name='quote_policy',
                               on_delete=models.CASCADE)
    cover = models.DecimalField(max_digits=10,
                                decimal_places=2)
    status = models.IntegerField(
        choices=STATUS,
        default='1',
    )
    premium = models.DecimalField(max_digits=10,
                                decimal_places=2, default=0.0)
    paid = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    history = FieldHistoryTracker(['status'])

    objects = QuoteManager()

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return  "{}".format(self.id)

    @property
    def get_user_age(self):
        """ Get the users age to calculate the policy charge based on agegroup"""
        return self.customer.age

    @property
    def get_quote_related_age_group(self):
        """ Get the quote related to customer age"""
        age = self.get_user_age
        if age:
            results = AgeGroupPolicy.objects.filter(Q(policy=self.policy) & Q(age_from__lte=age, age_to__gte=age)).values_list('charge', flat=True)
        #todo return an exceptions when age is not valid and there is non type like policy returning None
        return results

    @property
    def get_price_by_age_group_returned(self):
        """
        Calculate the premium based on age_group represented in AgeGroupPolicy
        """
        # if self.get_quote_related_age_group:
        quote_charge = [quote for quote in self.get_quote_related_age_group]
        if quote_charge:
            return self.cover / 100 * (quote_charge[0] / Decimal(100))
        return None
    
    def save(self, *args, **kwargs):
        quote_charge = [quote for quote in self.get_quote_related_age_group]
        if quote_charge:
            self.premium = self.cover / 100 * (quote_charge[0] / Decimal(100))
        super(Quote, self).save( *args, **kwargs)

 
