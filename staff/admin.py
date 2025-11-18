from django.contrib import admin
from . import models
# Register your models here.
class StaffDisplay(admin.ModelAdmin):
         list_display = ('id', 'name', 'job', 'salary','isBanned','isAdmin' ) # Add desired fields here
         search_fields = ['name', ]
admin.site.register(models.Staff,StaffDisplay)