from django.contrib import admin
from .models import Gmtcountry # traigo el modelo

# Register your models here.

admin.site.register(Gmtcountry) # modelo visible para el panel de administracion