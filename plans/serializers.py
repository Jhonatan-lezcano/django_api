from .models import Destination, Plan
from rest_framework import serializers

class DestinationSerializer(serializers.ModelSerializer):

  class Meta:
    model = Destination
    fields = ('__all__')

class PlanSerializer(serializers.ModelSerializer):
  id_destination = DestinationSerializer()
  class Meta: 
    model = Plan
    fields = ['id', 'destination_name', 'description', 'url_img', 'id_destination']