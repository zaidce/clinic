from django.contrib import admin
from . import models
# Register your models here.
class SessionxDisplay(admin.ModelAdmin):
         list_display = ('id', 'client_id__name', 'staff_id__name', 'sessionDate','service_id__name','newPrice','sessionState' ,'paied','deleteRequest') # Add desired fields here
         search_fields = ['client_id__name', 'staff_id__name', 'sessionDate','service_id__name']
admin.site.register(models.Sessionx,SessionxDisplay)