"""
URL configuration for rental_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenRefreshView
from user.views import UserViewSet
from user.auth_views import CustomTokenObtainPairView, register, logout, current_user
from user.views import login_view, register_view as template_register
from properties.views import PropertyViewSet, UnitViewSet
from tenants.views import TenantViewSet
from payments.views import PaymentViewSet
from maintenance.views import MaintenanceRequestViewSet

# Create a single router for all ViewSets
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'properties', PropertyViewSet, basename='property')
router.register(r'units', UnitViewSet, basename='unit')
router.register(r'tenants', TenantViewSet, basename='tenant')
router.register(r'payments', PaymentViewSet, basename='payment')
router.register(r'maintenance', MaintenanceRequestViewSet, basename='maintenance')

@api_view(['GET'])
def api_root(request):
    """API root endpoint"""
    return Response({
        'message': 'Welcome to Rental Management API',
        'version': '1.0',
        'auth': {
            'login': '/api/token/',
            'refresh': '/api/token/refresh/',
            'register': '/api/register/',
            'me': '/api/me/',
            'logout': '/api/logout/',
        },
        'endpoints': {
            'users': '/api/users/',
            'properties': '/api/properties/',
            'units': '/api/units/',
            'tenants': '/api/tenants/',
            'payments': '/api/payments/',
            'maintenance': '/api/maintenance/',
            'admin': '/admin/',
        }
    })

urlpatterns = [

    path('', api_root, name='api-root'),
    
    path('admin/', admin.site.urls),
    # Authentication endpoints
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', register, name='register'),

    # Template-based Authentication View
    path('login/', login_view, name='login'),
    path('register/', template_register, name='template_register'),

    path('api/me/', current_user, name='current_user'),
    path('api/logout/', logout, name='logout'),
    
    # API endpoints
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]