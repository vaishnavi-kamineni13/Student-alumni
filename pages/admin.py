from django.contrib import admin
from .models import Books,Stationery,Sports,Electronics,Others,Favourites

# Register your models here.
admin.site.register(Books)
admin.site.register(Electronics)
admin.site.register(Stationery)
admin.site.register(Sports)
admin.site.register(Others)
admin.site.register(Favourites)