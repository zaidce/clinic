from django.contrib import admin

from . import models
# Register your models here.
class RewardDisplay(admin.ModelAdmin):
         list_display = ('id', 'staff_id__name', 'gift',  ) # Add desired fields here
         search_fields = ['staff_id__name' ]
admin.site.register(models.Reward,RewardDisplay)