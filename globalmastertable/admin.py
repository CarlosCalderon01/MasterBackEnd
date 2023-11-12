from django.contrib import admin
from .models import *  # traigo el modelo

# Register your models here.
# modelo visible para el panel de administracion

# Section 1 - Country, State, City, location
admin.site.register(GmtCountry)
admin.site.register(GmtState)
admin.site.register(GmtCity)
# Section 2 - Language, Language, Communication
admin.site.register(GmtLanguage)
