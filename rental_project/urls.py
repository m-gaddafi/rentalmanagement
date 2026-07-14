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

    # Main Core Monolith Pages
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    
    # Dashboards
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('dashboard/landlord/', views.landlord_dashboard, name='landlord_dashboard'),

    #  Landlord views routed to properties app logic:
    path('dashboard/landlord/properties/', property_views.property_list_view, name='landlord_dashboard'),
    path('properties/add/', property_views.add_property_view, name='add_property'),
    
    path('dashboard/maintenance/', views.maintenance_dashboard, name='maintenance_dashboard'),
]