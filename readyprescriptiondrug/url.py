from django.urls import path,include
from rest_framework.routers import DefaultRouter

from .views  import *
router=DefaultRouter()
router.register('readyprescriptiondrug',ReadyPrescriptionDrugViewSet)
urlpatterns = [
  path('',include(router.urls)),
 
]