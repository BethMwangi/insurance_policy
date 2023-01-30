from django.urls import path, include
from . import views

app_name = 'policy'

urlpatterns = [
    path('', views.PolicyListView.as_view(), name='policy_list'),
    path('<int:pk>',
        views.PolicyDetailView.as_view(),
        name='policy-detail'),
]
