from rest_framework import serializers
from .models import *


class GmtCountrySerializers(serializers.ModelSerializer):
    class Meta:
        model = GmtCountry
        fields = '__all__'
        # fields = ['id', 'title', 'code', 'linenos', 'language', 'style']
        # fields --> modificar 1 por 1


class GmtStateSerializers(serializers.ModelSerializer):
    class Meta:
        model = GmtState
        Country = serializers.PrimaryKeyRelatedField(
            queryset=GmtCountry.objects.all())
        fields = '__all__'


class GmtLanguageSerializers(serializers.ModelSerializer):
    class Meta:
        model = GmtLanguage
        fields = '__all__'


# // ----- // ----- // ----- // ----- //
# puedes relacionar tablas en un serializer
    # utilizando los serializers relacionados.

        # PrimaryKeyRelatedField
        # StringRelatedField
        # SlugRelatedField
        # HyperlinkedRelatedField
        # HyperlinkedIdentityField
# // ----- // ----- // ----- // ----- //
