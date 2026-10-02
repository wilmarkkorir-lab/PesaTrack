from rest_framework import generics
from .models import *
from .serializers import *
class BusinessList(generics.ListCreateAPIView):
 serializer_class=BusinessSerializer
 def get_queryset(self): return Business.objects.filter(owner=self.request.user)
 def perform_create(self,s): s.save(owner=self.request.user)
class BusinessDetail(generics.RetrieveUpdateDestroyAPIView):
 serializer_class=BusinessSerializer
 def get_queryset(self): return Business.objects.filter(owner=self.request.user)
