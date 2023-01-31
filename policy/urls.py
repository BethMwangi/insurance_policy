from django.urls import path, include

from .views import (
    set_status,
    PolicyListView,
    QuoteListView,
    PolicyDetailView,
    QuoteDetailView,
    QuoteCreateView,
    CreateQuoteView,
    QuotesByCustomerView,
    QuoteAcceptView,
    QuotePayView,

)

app_name = 'policy'

urlpatterns = [
    path('', PolicyListView.as_view(), name='policy_list'),
    path('<int:pk>',
         PolicyDetailView.as_view()),

    path('quote/', QuoteListView.as_view(), name='quote_list'),
    path('quote/<int:pk>', QuoteDetailView.as_view(),
    ),
    path('quote/create_qoute/',
         QuoteCreateView.as_view()),

    path('quote/<int:pk>/confirm_quote/',
         QuoteAcceptView.as_view()),

    path('quote/<int:pk>/pay_quote/',
         QuotePayView.as_view()),
    path(
        'quote/policies/<int:customer>/',
        QuotesByCustomerView.as_view(),
    ),
    
]


