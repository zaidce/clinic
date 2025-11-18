from django.contrib import admin

from . import models
# Register your models here.
class OutcomeDisplay(admin.ModelAdmin):
         list_display = ('id', 'outcomeDate', 'outcomeType', 'name','total' ) # Add desired fields here
         search_fields = [ 'outcomeDate', 'outcomeType', 'name','total']
admin.site.register(models.Outcome,OutcomeDisplay)