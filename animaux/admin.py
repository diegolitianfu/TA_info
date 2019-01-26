from django.contrib import admin

# Register your models here.
from  .models import Animaux, Equipement

admin.site.register(Animaux)
admin.site.register(Equipement)
