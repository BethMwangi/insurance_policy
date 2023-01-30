from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

from .models import User


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('first_name', 'last_name','email', 'mobile_number')


class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = User
        fields =  ('location', 'birth_date', 'mobile_number')

