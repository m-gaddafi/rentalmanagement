from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from user.models import CustomUser
from user.serializers import UserSerializer, UserDetailSerializer
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login

class UserViewSet(viewsets.ModelViewSet):
    """ViewSet for CustomUser model"""
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        """Allow any user to create a new account"""
        if self.action == 'create':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        """Use detailed serializer for retrieve"""
        if self.action == 'retrieve':
            return UserDetailSerializer
        return UserSerializer

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def me(self, request):
        """Get current authenticated user"""
        serializer = UserDetailSerializer(request.user)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def set_password(self, request, pk=None):
        """Change user password"""
        user = self.get_object()
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'password set'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def login_view(request):
    """Handle HTML template-based user login"""
    error_message = None
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate against CustomUser model attributes
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            # For now, redirect to the Django Admin dashboard as a placeholder
            return redirect('/admin/')
        else:
            error_message = "Invalid username or password."
            
    return render(request, 'auth/login.html', {'error': error_message})

def register_view(request):
    """Handle HTML template-based user registration"""
    error_message = None
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        role = request.POST.get('role')
        
        # Validation: Check if username already exists
        if CustomUser.objects.filter(username=username).exists():
            error_message = "Username is already taken."
        else:
            # Create the user using our custom manager to handle passwords properly
            user = CustomUser.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
                role=role
            )
            # Log the user in automatically after registration
            auth_login(request, user)
            return redirect('/admin/')
            
    return render(request, 'auth/register.html', {'error': error_message})

