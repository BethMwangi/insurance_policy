from django.urls import path, include

from .views import (
    confirm_quote,
    pay_quote,
    set_status,
    PolicyListView,
    PolicyDetailView,
    QuoteListView,
    QuoteDetailView,
    CreateQuoteView,
    QuotesByCustomerView

)

app_name = 'policy'

urlpatterns = [
    path('', PolicyListView.as_view(), name='policy_list'),
    path('<int:pk>',
         PolicyDetailView.as_view(), name='policy-detail'),

    path('quote/', QuoteListView.as_view(), name='quote_list'),
    path('<int:pk>',
         QuoteDetailView.as_view(),
         name='quote_detail'),
    path('create_qoute/',
         CreateQuoteView.as_view(),
         name='create_quote'),
    path(
        'policies/<int:customer>/',
        QuotesByCustomerView.as_view()
    ),


    path('<int:pk>/confirm_quote/',
         confirm_quote
         ),
    path('<int:pk>/pay_quote/',
         pay_quote
         ),
]


