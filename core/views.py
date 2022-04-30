from django.http import HttpResponse
from core.models import Species
from rest_framework import generics
from .serializers import *
import datetime
from django.db.models import Count

# Create your views here.
class SpecieCreateAPIView(generics.CreateAPIView):
    serializer_class = SpecieSerializer


class SpeciesListAPIView(generics.ListAPIView):
    serializer_class = SpecieSerializer
    model = Species
    
    def get_queryset(self): 
        return Species.objects.all()