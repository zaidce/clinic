from django.urls import path,include
from rest_framework.routers import DefaultRouter

from .views  import *
router=DefaultRouter()
router.register('readyprescription',ReadyPrescriptionViewSet)
urlpatterns = [
  path('',include(router.urls)),
 
]