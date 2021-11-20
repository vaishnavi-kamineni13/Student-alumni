from django.urls import path
from .import views

urlpatterns = [
    path('', views.index,name="index"),
    path('profile',views.profile,name="profile"),
    path('password',views.password,name="password"),
    path('single_product_details/<int:my_id>/<str:my_username>',views.single_product_details,name="single_product_details"),
    path('requests/<int:my_id>/<str:bool>',views.requests,name="requests"),
    path('orders',views.orders,name="orders"),
    path('sold',views.sold,name="sold")
]
