from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/client/',include('client.url')),
    path('api/creditor/',include('creditor.url')),
    path('api/creditordetails/',include('creditordetails.url')),
    path('api/debtor/',include('debtor.url')),
    path('api/debtordetails/',include('debtordetails.url')),
    path('api/drug/',include('drug.url')),
    path('api/drugin/',include('drugin.url')),
    path('api/drugout/',include('drugout.url')),
 
    path('api/fingerprint/',include('fingerprint.url')),
    path('api/mistake/',include('mistake.url')),
    path('api/notifications/',include('notifications.url')),
    path('api/offer/',include('offer.url')),
    path('api/outcome/',include('outcome.url')),
    path('api/punishment/',include('punishment.url')),
    path('api/readyprescription/',include('readyprescription.url')),
    path('api/readyprescriptiondrug/',include('readyprescriptiondrug.url')),
    path('api/reward/',include('reward.url')),
    path('api/service/',include('service.url')),
    path('api/sessiondrugs/',include('sessiondrugs.url')),
    path('api/sessionx/',include('sessionx.url')),
    path('api/staff/',include('staff.url')),
    path('api/staffservicepercent/',include('staffservicepercent.url')),
 
 
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)