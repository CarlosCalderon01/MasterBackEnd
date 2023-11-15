from django.urls import path, include
from rest_framework import routers
from globalmastertable import views

router = routers.DefaultRouter()
# Section 1 - Country, State, City, location
router.register(r'country', views.GmtCountryViewSet)
router.register(r'state', views.GmtStateViewSet)
router.register(r'city', views.GmtCityViewSet)
# Section 2 - Language, Language, Communication
router.register(r'language', views.GmtLanguageViewSet)
# Section 3 - 
router.register(r'testingtask1', views.Textingtask1ViewSet)


urlpatterns = [
    path('', include(router.urls))
]
