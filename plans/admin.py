from django.contrib import admin
from plans.models import Destination, Plan

# Register your models here.
@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
  list_display = ['id', 'destination', 'image']

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
  list_display = ['id','id_destination', 'destination_name', 'description', 'url_img']