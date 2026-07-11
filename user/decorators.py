from django.http import HttpResponseForbidden
from django.shortcuts import redirect

def allowed_roles(allowed_roles_list=[]):
    """Decorator to restrict view access based on CustomUser role types"""
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            # 1. Force unauthenticated users to log in first
            if not request.user.is_authenticated:
                return redirect('/login/')
            
            # 2. Check if the user's role matches the permitted list
            if request.user.role in allowed_roles_list:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponseForbidden("<h3>Access Denied</h3>You do not have permission to view this page.")
        return wrapper_func
    return decorator