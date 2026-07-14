from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from user.decorators import allowed_roles
from .models import Property, Unit

@login_required(login_url='/login/')
@allowed_roles(allowed_roles_list=['landlord', 'admin'])
def property_list_view(request):
    """Show only the properties owned/managed by the logged-in landlord"""
    properties = Property.objects.filter(owner=request.user)
    return render(request, 'dashboards/landlord.html', {'properties': properties, 'user': request.user})

@login_required(login_url='/login/')
@allowed_roles(allowed_roles_list=['landlord', 'admin'])
def add_property_view(request):
    """Allow landlord to securely add a new property"""
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        city = request.POST.get('city')
        
        # Pull optional fields cleanly (returns None if empty or missing from form)
        state = request.POST.get('state') or None
        zip_code = request.POST.get('zip_code') or None
        total_units = request.POST.get('total_units') or None
        description = request.POST.get('description', '')
        
        # Save directly to the database
        Property.objects.create(
            owner=request.user,
            name=name,
            address=address,
            city=city,
            state=state,
            zip_code=zip_code,
            total_units=total_units,
            description=description
        )
        return redirect('landlord_dashboard')
        
    return render(request, 'properties/add_property.html')