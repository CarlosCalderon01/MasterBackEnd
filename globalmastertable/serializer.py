from rest_framework import serializers
from .models import *

# // ----- // ----- // ----- // ----- // ----- //
# Section 1 - Country, State, City, location
# // ----- // ----- // ----- // ----- // ----- //


class GmtCountrySerializers(serializers.ModelSerializer):
    class Meta:
        model = GmtCountry
        fields = '__all__'


class GmtStateSerializers(serializers.ModelSerializer):
    class Meta:
        model = GmtState
        Country = serializers.PrimaryKeyRelatedField(
            queryset=GmtCountry.objects.all())
        fields = '__all__'


class GmtCitySerializers(serializers.ModelSerializer):
    class Meta:
        model = GmtCity
        Country = serializers.PrimaryKeyRelatedField(
            queryset=GmtState.objects.all())
        fields = '__all__'

# // ----- // ----- // ----- // ----- // ----- //
# Section 1 - Finish Section
# // ----- // ----- // ----- // ----- // ----- //

# // ----- // ----- // ----- // ----- // ----- //
# Section 2 - Language, Language, Communication
# // ----- // ----- // ----- // ----- // ----- //


class GmtLanguageSerializers(serializers.ModelSerializer):
    class Meta:
        model = GmtLanguage
        fields = '__all__'

# // ----- // ----- // ----- // ----- // ----- //
# Section 2 - Finish Section
# // ----- // ----- // ----- // ----- // ----- //

# // ----- // ----- // ----- // Summary // ----- // ----- // ----- //

# puedes relacionar tablas en un serializer
    # Libreria --> from rest_framework import serializer
        # serializers.<FieldName>

    # fields --> specify keyword from model, 1 by 1.
        # fields = ['id', 'alfa2', 'alfa3', 'phone', 'num']

    # read_only_fields --> only allows read, do not edit.
        # read_only_fields = ['alfa2']
    
    # extra_kwargs --> only allows read, do not edit.

# Topics On Hold
"""

    ForeignKey
        PrimaryKeyRelatedField
        StringRelatedField
        SlugRelatedField
        HyperlinkedRelatedField
        HyperlinkedIdentityField
        
    ManyToManyField
    OneToOneField
    GenericForeignKey

"""

# Bibliografia
# Serializador --> https://www.django-rest-framework.org/api-guide/serializers/
# relations --> https://www.django-rest-framework.org/api-guide/relations/

# ForeignKey

    # utilizando los serializers relacionados.

