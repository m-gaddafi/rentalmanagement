from django.urls import path, include
from rest_framework.routers import DefaultRouter
from properties.views import PropertyViewSet, UnitViewSet

router = DefaultRouter()
router.register(r'properties', PropertyViewSet)
router.register(r'units', UnitViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
