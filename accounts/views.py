from rest_framework import generics,permissions
from django.contrib.auth import get_user_model
from .models import Profile
from .serializers import RegisterSerializer,ProfileSerializer,AdminUserSerializer
User=get_user_model()
class RegisterView(generics.CreateAPIView): permission_classes=[permissions.AllowAny]; serializer_class=RegisterSerializer
class ProfileView(generics.RetrieveUpdateAPIView):
 serializer_class=ProfileSerializer
 def get_object(self): return Profile.objects.get(user=self.request.user)
class AdminUsersView(generics.ListAPIView):
 serializer_class=AdminUserSerializer
 permission_classes=[permissions.IsAdminUser]
 def get_queryset(self): return Profile.objects.select_related("user").order_by("-created_at")
