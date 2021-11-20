from django.urls import path,include

from . import views

urlpatterns=[
    path('sellform',views.sellform,name="sellform"),
    path('eventRegistration',views.eventRegistration,name="eventRegistration"),
]