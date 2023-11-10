
from django.contrib.auth.models import * # --> EXTRAER MODELOS
from rest_framework import viewsets # --> Agrupador de metodos {read, create, update, delete}
from rest_framework import permissions # --> Control de acceso, nivel vista o objeto
from serializers import * # --> EXTRAER MODELOS


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]