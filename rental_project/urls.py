"""
URL configuration for rental_project project.
"""

from django.contrib import admin
from django.urls import path
from user import views
from properties import views as property_views

urlpatterns = [
    # Admin Panel
    path('admin/', admin.site.urls),

    # Main Core Monolith Pages (from user app)
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    
    # Dashboards (from user app)
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('dashboard/maintenance/', views.maintenance_dashboard, name='maintenance_dashboard'),
    
    # Landlord Dashboard (from properties app)
    path('dashboard/landlord/', property_views.property_list_view, name='landlord_dashboard'),
    
    # Tenant Property Browsing & Applying (FIXED: mapped to property_views)
    path('properties/', property_views.tenant_properties_list_view, name='properties_list'),
    path('properties/apply/<int:property_id>/', property_views.apply_property_view, name='apply_property'),
    
    # Landlord add property endpoint (FIXED: mapped to property_views)
    path('properties/add/', property_views.add_property_view, name='add_property'),
]