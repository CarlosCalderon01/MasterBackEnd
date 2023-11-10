from rest_framework import viewsets
from .serializer import *
from .models import *

# Create your views here.


class GmtCountryViewSet(viewsets.ModelViewSet):
    queryset = GmtCountry.objects.all()
    serializer_class = GmtCountrySerializers


class GmtStateViewSet(viewsets.ModelViewSet):
    queryset = GmtState.objects.all()
    serializer_class = GmtStateSerializers


class GmtLanguageViewSet(viewsets.ModelViewSet):
    queryset = GmtLanguage.objects.all()
    serializer_class = GmtLanguageSerializers
