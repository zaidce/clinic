from django.db import models
from datetime import datetime
# Create your models here.
class Service(models.Model):
    name=models.CharField(max_length=200,verbose_name="الخدمة")
    cost=models.IntegerField( verbose_name="الكلفة")
    price=models.IntegerField( verbose_name="السعر")
    points=models.IntegerField(default=0,verbose_name="النقاط")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "خدمة"  # Singular name
        verbose_name_plural = "الخدمات" # Plural name
        #,verbose_name="القسم"