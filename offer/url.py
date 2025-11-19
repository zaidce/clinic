from django.urls import path,include
from rest_framework.routers import DefaultRouter

from .views  import *
router=DefaultRouter()
router.register('offer',OfferViewSet)
urlpatterns = [
  path('',include(router.urls)),
 
]