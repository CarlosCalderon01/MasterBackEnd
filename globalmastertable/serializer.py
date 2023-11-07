from rest_framework import serializers
from .models import *


class GmtCountrySerializers(serializers.ModelSerializer):
    class Meta:
        model = GmtCountry
        fields = '__all__'
        # fields = ('name','alfa2') #--> para modificar unos cuantos, no todo en la tabla. 

class GmtLanguageSerializers(serializers.ModelSerializer):
    class Meta:
        model = GmtLanguage
        fields = '__all__'