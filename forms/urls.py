from django.urls import path,include

from . import views

urlpatterns=[
    path('questionform',views.questionform,name="questionform"),
    path('eventRegistration',views.eventRegistration,name="eventRegistration"),
]