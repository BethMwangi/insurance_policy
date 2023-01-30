
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import User
from .forms import CustomUserCreationForm, CustomUserChangeForm


class UserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    fieldsets = (
      (None, {'fields': ('email', 'password',  )}),
      (_('Personal info'), {'fields': ('first_name', 'last_name')}),
      (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                     'groups', 'user_permissions')}),
      (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('user_info'), {'fields': ('mobile_number', 'location', 'birth_date', )}),
    )
    add_fieldsets = (
      (None, {
          'classes': ('wide', ),
          'fields': ('email', 'password1', 'password2', 'mobile_number'),
      }),
    )
    list_display = ['email', 'username', 'first_name', 'mobile_number', 'location', 'birth_date', 'age' ,'date_joined']
    search_fields = ('email', 'first_name', 'last_name', 'birth_date')
    ordering = ('email', )


admin.site.register(User, UserAdmin)