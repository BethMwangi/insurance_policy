from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.UserListView.as_view(), name='user_list'),
    path('create_customer/',
     views.UserCreateView.as_view(),
     name='create_customer'),
    path('<int:pk>', views.UserDetailView.as_view(), name='user_detail'),
    
]
