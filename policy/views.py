
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from .serializers import  PolicySerializer
from .models import Policy


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
    
