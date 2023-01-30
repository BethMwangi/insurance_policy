from django.contrib import admin
from .models import Policy, AgeGroupPolicy, Quote


class PolicyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'history']
    prepopulated_fields = {'slug': ('name',)}


class AgeGroupPolicyAdmin(admin.ModelAdmin):
    list_display = ['id', 'policy', 'age_from', 'age_to',
                    'price', 'charge', 'created', 'updated']


class QuoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'policy', 'cover', 'status']


admin.site.register(Policy, PolicyAdmin)
admin.site.register(AgeGroupPolicy, AgeGroupPolicyAdmin)
admin.site.register(Quote, QuoteAdmin)
