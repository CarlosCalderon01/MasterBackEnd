from django.contrib import admin
from .models import *  # traigo el modelo

# Register your models here.

# modelo visible para el panel de administracion
admin.site.register(GmtCountry)
admin.site.register(GmtState)

admin.site.register(GmtLanguage)
