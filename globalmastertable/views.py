from rest_framework import viewsets
from .serializer import GmtcountrySerializers
from .models import Gmtcountry

# Create your views here.


class GmtcountryViewSet(viewsets.ModelViewSet):
    queryset = Gmtcountry.objects.all()
    serializer_class = GmtcountrySerializers
