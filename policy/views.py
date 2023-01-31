
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status

from .serializers import PolicySerializer, QuoteSerializer
from .models import Policy, Quote
from .helpers import set_status_handler, QuoteListAPIBaseView
from .status import Status


class PolicyListView(generics.ListAPIView):
    queryset = Policy.objects.all()
    serializer_class = PolicySerializer
    search_fields = ['name']
    filterset_fields = (
        'name',
        'status',
        'available',
    )
    search_fields = ('name', 'status', 'available', )

    ordering_fields = (
        'name',
        'created',
    )


class PolicyDetailView(generics.RetrieveAPIView):
    queryset = Policy.objects.all()
    serializer_class = PolicySerializer


class QuoteListView(generics.ListAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    search_fields = ['name']
    filterset_fields = (
        'customer',
        'policy',
        'status',
    )
    search_fields = ('customer', 'policy', 'status', 'history', )

    ordering_fields = (
        'created',
    )


class QuoteDetailView(generics.RetrieveAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer


class QuoteCreateView(generics.CreateAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer


class QuoteListAPIBaseView(generics.ListAPIView):
    serializer_class = QuoteSerializer
    lookup_field = ''

    def get_queryset(self, lookup_field_id):
        pass

    def list(self, request, *args, **kwargs):
        try:
            result = self.get_queryset(kwargs.get(self.lookup_field, None))
        except Exception as err:
            return Response(err, status=status.HTTP_400_BAD_REQUEST)

        serializer = QuoteSerializer(result, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateQuoteView(generics.CreateAPIView):
    serializer_class = QuoteSerializer

    def post(self, request, *arg, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            quote = serializer.save()
            return Response(
                {'quote_id': quote.id,
                 'customer_id': quote.customer.id,
                 'email': quote.customer.email,
                 'policy': quote.policy.slug,
                 'status': quote.policy.status,
                 'cover': quote.cover,
                 'premium': quote.premium,
                 },
                status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)

class QuoteAcceptView(generics.ListCreateAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer

    def post(self, request, pk):
        qoute = get_object_or_404(Quote, id=pk)
        statuschange = set_status_handler(
        lambda: Quote.objects.accept_quote(qoute))
        data = {'status': statuschange}
        serializer = QuoteSerializer(qoute, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

class QuotePayView(generics.ListCreateAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer

    def post(self, request, pk):
        qoute = get_object_or_404(Quote, id=pk)
        statuschange = set_status_handler(
        lambda: Quote.objects.pay_quote(qoute))
        data = {'status': statuschange}
        serializer = QuoteSerializer(qoute, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})


def pay_quote(request, pk):
    qoute = get_object_or_404(Quote, id=pk)
    change = set_status_handler(
        lambda: Quote.objects.pay_quote(qoute)
    )
    return change


def set_status(request, quote_id, status_id):
    quote = get_object_or_404(Quote, quote_id=quote_id)
    try:
        status = Status(quote_id)
    except ValueError:
        return HttpResponse(
            'The status value is invalid.',
            status=status.HTTP_400_BAD_REQUEST)
    return set_status_handler(
        lambda: Quote.objects.set_status(quote, status)
    )


class QuoteConfirmationUpdateView(generics.UpdateAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer


class QuotesByCustomerView(QuoteListAPIBaseView):
    lookup_field = 'customer'

    def get_queryset(self, customer):
        return Quote.objects.get_all_quotes_by_customer(customer)
