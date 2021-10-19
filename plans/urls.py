
from rest_framework.routers import DefaultRouter 
from .views import DestinationViewSet, PlanViewSet

router_destination = DefaultRouter()
router_plan = DefaultRouter()

router_destination.register(prefix='destination', basename='destination', viewset=DestinationViewSet),
router_plan.register(prefix='plan', basename='plan', viewset=PlanViewSet),

