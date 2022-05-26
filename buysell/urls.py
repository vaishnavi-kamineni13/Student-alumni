from django.urls import path
from .import views

urlpatterns = [
    path('', views.index,name="index"),
    path('profile',views.profile,name="profile"),
    path('password',views.password,name="password"),
    path('password1',views.password1,name="password1"),
    path('technical',views.technical,name="technical"),
    path('techform',views.techform,name="techform")
]
