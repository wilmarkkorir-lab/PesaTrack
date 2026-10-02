from django.conf import settings
from django.db import models
class Business(models.Model):
 owner=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE); name=models.CharField(max_length=160); email=models.EmailField(blank=True); phone=models.CharField(max_length=40,blank=True); address=models.CharField(max_length=255,blank=True); currency=models.CharField(max_length=3,default="KES"); invoice_prefix=models.CharField(max_length=15,default="INV"); next_invoice_number=models.PositiveIntegerField(default=1); created_at=models.DateTimeField(auto_now_add=True)
class Membership(models.Model):
 business=models.ForeignKey(Business,on_delete=models.CASCADE,related_name="memberships"); user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE); role=models.CharField(max_length=15,default="viewer")
 class Meta: constraints=[models.UniqueConstraint(fields=["business","user"],name="uniq_member")]
class Customer(models.Model):
 business=models.ForeignKey(Business,on_delete=models.CASCADE); name=models.CharField(max_length=160); email=models.EmailField(blank=True); phone=models.CharField(max_length=40,blank=True); address=models.CharField(max_length=255,blank=True)
class Supplier(models.Model):
 business=models.ForeignKey(Business,on_delete=models.CASCADE); name=models.CharField(max_length=160); email=models.EmailField(blank=True); phone=models.CharField(max_length=40,blank=True)
class ProductService(models.Model):
 business=models.ForeignKey(Business,on_delete=models.CASCADE); name=models.CharField(max_length=160); description=models.TextField(blank=True); unit_price=models.DecimalField(max_digits=14,decimal_places=2); is_active=models.BooleanField(default=True)
class Invoice(models.Model):
 business=models.ForeignKey(Business,on_delete=models.CASCADE); customer=models.ForeignKey(Customer,on_delete=models.PROTECT); number=models.CharField(max_length=40); issue_date=models.DateField(); due_date=models.DateField(null=True,blank=True); status=models.CharField(max_length=15,default="draft"); notes=models.TextField(blank=True); subtotal=models.DecimalField(max_digits=14,decimal_places=2,default=0); tax_amount=models.DecimalField(max_digits=14,decimal_places=2,default=0); total=models.DecimalField(max_digits=14,decimal_places=2,default=0); amount_paid=models.DecimalField(max_digits=14,decimal_places=2,default=0); created_at=models.DateTimeField(auto_now_add=True)
 class Meta: constraints=[models.UniqueConstraint(fields=["business","number"],name="uniq_invoice_number")]
class InvoiceItem(models.Model):
 invoice=models.ForeignKey(Invoice,on_delete=models.CASCADE,related_name="items"); description=models.CharField(max_length=255); quantity=models.DecimalField(max_digits=12,decimal_places=2,default=1); unit_price=models.DecimalField(max_digits=14,decimal_places=2); tax_rate=models.DecimalField(max_digits=5,decimal_places=2,default=0); line_total=models.DecimalField(max_digits=14,decimal_places=2,default=0)
class InvoicePayment(models.Model):
 invoice=models.ForeignKey(Invoice,on_delete=models.CASCADE,related_name="payments"); amount=models.DecimalField(max_digits=14,decimal_places=2); paid_at=models.DateField(); method=models.CharField(max_length=15,default="cash"); reference=models.CharField(max_length=100,blank=True)
class BusinessExpense(models.Model):
 business=models.ForeignKey(Business,on_delete=models.CASCADE); supplier=models.ForeignKey(Supplier,on_delete=models.SET_NULL,null=True,blank=True); category=models.CharField(max_length=100); amount=models.DecimalField(max_digits=14,decimal_places=2); expense_date=models.DateField(); description=models.CharField(max_length=255,blank=True)
class AuditLog(models.Model):
 business=models.ForeignKey(Business,on_delete=models.CASCADE); actor=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True); action=models.CharField(max_length=100); target_type=models.CharField(max_length=80); target_id=models.CharField(max_length=64); metadata=models.JSONField(default=dict); created_at=models.DateTimeField(auto_now_add=True)
