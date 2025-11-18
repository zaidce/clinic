from django.db import models
from datetime import datetime

from drug.models import Drug
from sessionx.models import Sessionx
# Create your models here.
class SessionDrug(models.Model):
    session_id=models.ForeignKey(Sessionx,related_name="SessionDrugSessionx",on_delete=models.CASCADE)
    drug_id=models.ForeignKey(Drug,related_name="SessionDrugDrug",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.session_id