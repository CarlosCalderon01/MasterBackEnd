from rest_framework import serializers
from .models import Gmtcountry


class GmtcountrySerializers(serializers.ModelSerializer):
    class Meta:
        model = Gmtcountry
        # fields = ('name','alfa2') #--> para modificar unos cuantos, no todo en la tabla.
        fields = '__all__'
