from django.db import models
from datetime import datetime
# Create your models here.
class Client (models.Model):
      bloodChoices={
        ("لا اعرف","لا اعرف"),
        ("A+","A+"),
        ("B+","B+"),
        ("AB+","AB+"),
        ("O+","O+"),
          ("A-","A-"),
        ("B-","B-"),
        ("AB-","AB-"),
        ("O-","O-"),
        }
      mariageChoices={
        ("اعزب","اعزب"),
        ("متزوج","متزوج"),
        ("مطلق","مطلق"),
        ("ارمل","ارمل")
        }
      genderChoices={
        ("ذكر","ذكر"),
        ("انثى","انثى"),
  
        }
      name=models.CharField(max_length=200,verbose_name="الاسم")
      bornYear=models.IntegerField(verbose_name="التولد")
      phone=models.CharField(max_length=11,verbose_name="رقم الهاتف")
      address=models.CharField(max_length=200,null=True,blank=True,verbose_name="العنوان")
      gender=models.CharField(default='ذكر',choices=genderChoices ,verbose_name="الجنس")# TODO: 
      alergy=models.CharField(max_length=200,null=True,blank=True,verbose_name="الحساسية")
      desiase=models.CharField(max_length=200,null=True,blank=True,verbose_name="امراض مزمنة")
      blood=models.CharField(max_length=20,choices=bloodChoices,default="لا اعرف",verbose_name="فصيلة الدم")
      mariage=models.CharField(max_length=20,choices=mariageChoices,default="اعزب",verbose_name="الحالة الزوجية")
      lastOperations=models.CharField(max_length=200,null=True,blank=True,verbose_name="عمليات سابقة")
      smooker=models.BooleanField(default=False,verbose_name="مدخن")
      hidden=models.BooleanField(default=False,verbose_name="اخفاء")
      note=models.CharField(max_length=200,null=True,blank=True,verbose_name="الملاحظات")
      def __str__(self):
        return self.name
      class Meta:
        verbose_name = "زبون"  # Singular name
        verbose_name_plural = "الزبائن" # Plural name
        #,verbose_name="القسم"