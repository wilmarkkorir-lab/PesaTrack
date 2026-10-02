from django.conf import settings
from django.db import models
class Profile(models.Model):
 user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="profile")
 full_name=models.CharField(max_length=150)
 currency=models.CharField(max_length=3,choices=[("KES","KES"),("USD","USD")],default="KES")
 timezone=models.CharField(max_length=64,default="Africa/Nairobi")
 email_verified=models.BooleanField(default=False)
 created_at=models.DateTimeField(auto_now_add=True)
 updated_at=models.DateTimeField(auto_now=True)
class SecurityEvent(models.Model):
 user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="security_events")
 event=models.CharField(max_length=100)
 ip_address=models.GenericIPAddressField(null=True,blank=True)
 created_at=models.DateTimeField(auto_now_add=True)
