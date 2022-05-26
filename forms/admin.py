from django.contrib import admin
from .models import Eventform,Event,Techform,Questionform,Answerform,Techansform

# Register your models here.
admin.site.register(Eventform)
admin.site.register(Event)
admin.site.register(Questionform)
admin.site.register(Answerform)
admin.site.register(Techform)
admin.site.register(Techansform)