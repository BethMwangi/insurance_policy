from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Policy, AgeGroupPolicy


class PolicyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'history']
    prepopulated_fields = {'slug': ('name',)}

class AgeGroupPolicyAdmin(admin.ModelAdmin):
    list_display = ['id', 'policy', 'age_from', 'age_to', 'price', 'charge', 'created', 'updated']

admin.site.register(Policy, PolicyAdmin)
admin.site.register(AgeGroupPolicy, AgeGroupPolicyAdmin)
