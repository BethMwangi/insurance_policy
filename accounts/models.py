from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


from django.utils import timezone


class User(AbstractUser):
    username = models.CharField(
        max_length=50, blank=True, null=True, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    bio = models.TextField(max_length=500, blank=True)
    mobile_number = models.CharField(max_length=10, unique=True, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(
        null=True, blank=True, help_text='The birthdate format "YYYY-MM-DD"')
    age = models.PositiveIntegerField(null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'birth_date']

    def __str__(self):
        return "{}".format(self.email)

    def save(self, *args, **kwargs):
        if self.birth_date:
            self.age = timezone.now().year - self.birth_date.year  
        super(User, self).save( *args, **kwargs)
