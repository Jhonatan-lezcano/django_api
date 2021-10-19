from django.shortcuts import render
from plans.models import Destination, Plan
from .serializers import DestinationSerializer, PlanSerializer
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.

class DestinationViewSet(ModelViewSet):
  serializer_class = DestinationSerializer
  queryset = Destination.objects.all()

class PlanViewSet(ModelViewSet):
  serializer_class = PlanSerializer
  queryset = Plan.objects.all()
  filter_backends = [DjangoFilterBackend]
  filterset_fields = ['id_destination']
