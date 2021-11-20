from django.urls import path,include

from . import views

urlpatterns = [
    path('about',views.about,name="about"),
    path('books/<str:my_username>',views.books,name="books"),
    path('electronics/<str:my_username>',views.electronics,name="electronics"),
    path('event',views.event,name="event"),
    path('favourites/<str:direct>',views.favourites,name="favourites"),
    #path('favourite_post/<int:my_id>',views.favourite_post,name="favourite_post"),
    path('others/<str:my_username>',views.others,name="others"),
    path('books_product_details/<int:my_id>/<str:my_username>',views.books_product_details,name="books_product_details"),
    path('electronics_product_details/<int:my_id>/<str:my_username>',views.electronics_product_details,name="electronics_product_details"),
    path('stationery_product_details/<int:my_id>/<str:my_username>',views.stationery_product_details,name="stationery_product_details"),
    path('sports_product_details/<int:my_id>/<str:my_username>',views.sports_product_details,name="sports_product_details"),
     path('others_product_details/<int:my_id>/<str:my_username>',views.others_product_details,name="others_product_details"),
     path('favourite_product_details/<int:my_id>',views.favourite_product_details,name="favourite_product_details"),
    path('sports/<str:my_username>',views.sports,name="sports"),
    path('stationery/<str:my_username>',views.stationery,name="stationery")
]
