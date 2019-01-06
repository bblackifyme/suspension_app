from django.contrib import admin

# Register your models here.
from .models import Setting, Bike, User

admin.site.register(Setting)
admin.site.register(Bike)
admin.site.register(User)