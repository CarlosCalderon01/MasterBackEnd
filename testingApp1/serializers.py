from django.contrib.auth.models import User, Group
from rest_framework import serializers

# Observe que en este caso utilizamos relaciones de hipervínculo con HyperlinkedModelSerializer
# También puede utilizar la clave principal y otras relaciones
# pero los hipervínculos son un buen diseño RESTful.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
