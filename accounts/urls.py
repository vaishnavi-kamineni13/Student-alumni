from django.urls import path,include

from . import views

urlpatterns=[
    path('login',views.login,name="login"),
    path('signup',views.signup,name="signup"),
    path('signupalumni',views.signupalumni,name="signupalumni"),
    path('signupstudent',views.signupstudent,name="signupstudent"),
    path('logout',views.logout,name="logout"),
]