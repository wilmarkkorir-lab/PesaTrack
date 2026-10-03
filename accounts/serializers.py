from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Profile
User=get_user_model()
class RegisterSerializer(serializers.ModelSerializer):
 password=serializers.CharField(write_only=True,min_length=8)
 full_name=serializers.CharField(write_only=True)
 currency=serializers.ChoiceField(choices=["KES","USD"],write_only=True,default="KES")
 class Meta: model=User; fields=("username","email","password","full_name","currency"); extra_kwargs={"email":{"required":True},"username":{"required":False}}
 def create(self,data):
  name=data.pop("full_name"); currency=data.pop("currency"); email=data["email"].lower().strip(); username=data.pop("username","") or email
  user=User.objects.create_user(username=username,email=email,password=data["password"]); Profile.objects.create(user=user,full_name=name,currency=currency); return user
class ProfileSerializer(serializers.ModelSerializer):
 email=serializers.EmailField(source="user.email",read_only=True)
 class Meta: model=Profile; fields=("full_name","email","currency","timezone","email_verified","created_at","updated_at"); read_only_fields=("email_verified","created_at","updated_at")
class AdminUserSerializer(serializers.ModelSerializer):
 email=serializers.EmailField(source="user.email",read_only=True)
 username=serializers.CharField(source="user.username",read_only=True)
 is_active=serializers.BooleanField(source="user.is_active",read_only=True)
 is_staff=serializers.BooleanField(source="user.is_staff",read_only=True)
 last_login=serializers.DateTimeField(source="user.last_login",read_only=True)
 class Meta: model=Profile; fields=("id","full_name","email","username","currency","is_active","is_staff","last_login","created_at")
