from django.conf import settings
from django.db import models
class SupportTicket(models.Model): user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE); subject=models.CharField(max_length=200); message=models.TextField(); status=models.CharField(max_length=20,default="open"); created_at=models.DateTimeField(auto_now_add=True); updated_at=models.DateTimeField(auto_now=True)
class TicketReply(models.Model): ticket=models.ForeignKey(SupportTicket,on_delete=models.CASCADE,related_name="replies"); author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True); message=models.TextField(); created_at=models.DateTimeField(auto_now_add=True)
