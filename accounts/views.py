from rest_framework import generics,permissions
from .models import Profile
from .serializers import RegisterSerializer,ProfileSerializer
class RegisterView(generics.CreateAPIView): permission_classes=[permissions.AllowAny]; serializer_class=RegisterSerializer
class ProfileView(generics.RetrieveUpdateAPIView):
 serializer_class=ProfileSerializer
 def get_object(self): return Profile.objects.get(user=self.request.user)
