from django.db import models
from simple_history.models import HistoricalRecords
from django.core.validators import MaxValueValidator, MinValueValidator


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
    history = HistoricalRecords()

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


