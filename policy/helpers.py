
from rest_framework import generics, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import QuoteSerializer
from django.http import HttpResponse
from rest_framework import status


from django.http import HttpResponse
from .exceptions import InvalidArgumentError, QuoteAlreadyArchivedError


def set_status_handler(set_status_delegate):
    try:
        set_status_delegate()
    except (
            InvalidArgumentError,
            QuoteAlreadyArchivedError) as err:
        return HttpResponse(err, status=status.HTTP_400_BAD_REQUEST)

    return HttpResponse(status=status.HTTP_204_NO_CONTENT)


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
