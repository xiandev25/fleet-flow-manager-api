from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FamilyViewSet, StudentViewSet

router = DefaultRouter()
router.register(r'families', FamilyViewSet, basename='family')
router.register(r'students', StudentViewSet, basename='student')

urlpatterns = [
    path('', include(router.urls)),
]
