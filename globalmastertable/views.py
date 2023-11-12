from rest_framework import viewsets
from .serializer import *
from .models import *

# // ----- // ----- // ----- // ----- // ----- //
# Section 1 - Country, State, City, location
# // ----- // ----- // ----- // ----- // ----- //


class GmtCountryViewSet(viewsets.ModelViewSet):
    queryset = GmtCountry.objects.all()
    serializer_class = GmtCountrySerializers


class GmtStateViewSet(viewsets.ModelViewSet):
    queryset = GmtState.objects.all()
    serializer_class = GmtStateSerializers


class GmtCityViewSet(viewsets.ModelViewSet):
    queryset = GmtCity.objects.all()
    serializer_class = GmtCitySerializers

# // ----- // ----- // ----- // ----- // ----- //
# Section 1 - Finish Section
# // ----- // ----- // ----- // ----- // ----- //

# // ----- // ----- // ----- // ----- // ----- //
# Section 2 - Language, Language, Communication
# // ----- // ----- // ----- // ----- // ----- //


class GmtLanguageViewSet(viewsets.ModelViewSet):
    queryset = GmtLanguage.objects.all()
    serializer_class = GmtLanguageSerializers

# // ----- // ----- // ----- // ----- // ----- //
# Section 2 - Finish Section
# // ----- // ----- // ----- // ----- // ----- //
