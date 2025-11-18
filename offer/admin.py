from django.contrib import admin

# Register your models here.
from . import models
# Register your models here.
class OfferDisplay(admin.ModelAdmin):
         list_display = ('id', 'service_id__name', 'newPrice', 'startDate','endDate' ) # Add desired fields here
         search_fields = ['service_id__name']
admin.site.register(models.Offer,OfferDisplay)