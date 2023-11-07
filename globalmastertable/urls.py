from django.urls import path, include
from rest_framework import routers
from globalmastertable import views

router = routers.DefaultRouter()
router.register(r'country', views.GmtCountryViewSet)

urlpatterns = [
    path('', include(router.urls))
]
