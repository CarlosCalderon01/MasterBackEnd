from django.urls import path # libreria para rutas en los direcctorios
from django.urls import include # libreria para incluir url de otras apps
from rest_framework import routers # libreria
from testingApp1 import views #Modulo


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('', include(router.urls))
]

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]