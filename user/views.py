from user.models import CustomUser
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from properties.models import Property
from user.decorators import allowed_roles

# --- Helper Redirection Function ---
def _route_user_by_role(user):
    """Inspects the user's database role and routes them accordingly"""
    if user.role == 'landlord':
        return redirect('/dashboard/landlord/')
    elif user.role == 'maintenance':
        return redirect('/dashboard/maintenance/')
    else:
        return redirect('/dashboard/') # Standard Tenant Dashboard

def home_view(request):
    """Simple landing page"""
    return render(request, 'home.html')


# --- 2. Centralized Routing Login View ---
def login_view(request):
    """Handle HTML template-based login and route roles dynamically"""
    if request.user.is_authenticated:
        return _route_user_by_role(request.user)

    error_message = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            return _route_user_by_role(user)
        else:
            error_message = "Invalid username or password."
            
    return render(request, 'auth/login.html', {'error': error_message})

# --- 3. Secure Tenant-Only Public Registration ---
def register_view(request):
    """Handle HTML template-based user registration securely"""
    if request.user.is_authenticated:
        return _route_user_by_role(request.user)

    error_message = None
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone', '')
        city = request.POST.get('city', '')
        
        # Absolute Security Rule: Public templates can ONLY register tenants
        role = 'tenant'
        
        if CustomUser.objects.filter(username=username).exists():
            error_message = "Username is already taken."
        elif CustomUser.objects.filter(email=email).exists():
            error_message = "An account with this email address already exists."
        else:
            try:
                user = CustomUser.objects.create_user(
                    username=username,
                    email=email,
                    password=password,
                    first_name=first_name,
                    last_name=last_name,
                    role=role,
                    phone=phone,
                    city=city
                )
                auth_login(request, user)
                return redirect('/dashboard/')
            except Exception as e:
                error_message = f"Registration failed: {str(e)}"
                
    return render(request, 'auth/register.html', {'error': error_message})

def logout_view(request):
    """Log out the user and redirect to login page"""
    auth_logout(request)
    return redirect('/login/')

@login_required(login_url='/login/')
@allowed_roles(allowed_roles_list=['tenant', 'admin'])
def dashboard_view(request):
    """Render the secure landing dashboard for authenticated users"""
    user = request.user
    context = {'user': user}
    
    # 1. Check for an active lease associated with this tenant
    # (Adjust this query to match your actual schema, e.g., Lease.objects.filter(tenant=user, is_active=True).first())
    lease = getattr(user, 'active_lease', None) 
    
    if lease:
        # === STATE A: Fetch active lease details ===
        context['lease'] = lease
        # context['payments'] = Payment.objects.filter(lease=lease).order_by('-date')[:5]
        # context['maintenance_requests'] = MaintenanceRequest.objects.filter(tenant=user).order_by('-date_submitted')[:5]
        # context['active_requests_count'] = context['maintenance_requests'].filter(status='pending').count()
    else:
        # === STATE B: Fetch available properties for the lease-less tenant ===
        # Adjust the filter based on how you track vacancy (e.g., is_available=True or total_units__gt=0)
        context['lease'] = None
        context['available_properties'] = Property.objects.all()[:6] 

    return render(request, 'dashboard.html', context)

# --- 6. Landlord Dashboard ---
@login_required(login_url='/login/')
@allowed_roles(allowed_roles_list=['landlord', 'admin'])
def landlord_dashboard(request):
    """Secure portal for landlords managing properties"""
    return render(request, 'dashboards/landlord.html', {'user': request.user})

# --- 7. Maintenance Staff Dashboard ---
@login_required(login_url='/login/')
@allowed_roles(allowed_roles_list=['maintenance', 'admin'])
def maintenance_dashboard(request):
    """Secure portal for repair teams tracking job tickets"""
    return render(request, 'dashboards/maintenance.html', {'user': request.user})


