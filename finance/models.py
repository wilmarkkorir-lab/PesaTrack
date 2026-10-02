from decimal import Decimal
from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models
V=MinValueValidator(Decimal("0.01"))
class Category(models.Model):
 user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="categories"); name=models.CharField(max_length=60); transaction_type=models.CharField(max_length=7,choices=[("income","Income"),("expense","Expense")]); icon=models.CharField(max_length=50,default="bi-tag"); color=models.CharField(max_length=20,default="#16a34a"); created_at=models.DateTimeField(auto_now_add=True)
 class Meta: constraints=[models.UniqueConstraint(fields=["user","name","transaction_type"],name="uniq_category")]
class Transaction(models.Model):
 user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="transactions"); category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True); transaction_type=models.CharField(max_length=7,choices=[("income","Income"),("expense","Expense")]); amount=models.DecimalField(max_digits=14,decimal_places=2,validators=[V]); description=models.CharField(max_length=255,blank=True); payment_method=models.CharField(max_length=10,default="cash"); transaction_date=models.DateField(); created_at=models.DateTimeField(auto_now_add=True); updated_at=models.DateTimeField(auto_now=True)
 class Meta: ordering=["-transaction_date","-created_at"]
class Budget(models.Model):
 user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE); month=models.DateField(); total_limit=models.DecimalField(max_digits=14,decimal_places=2,validators=[V]); created_at=models.DateTimeField(auto_now_add=True)
 class Meta: constraints=[models.UniqueConstraint(fields=["user","month"],name="uniq_budget_month")]
class BudgetCategory(models.Model):
 budget=models.ForeignKey(Budget,on_delete=models.CASCADE,related_name="limits"); category=models.ForeignKey(Category,on_delete=models.CASCADE); limit_amount=models.DecimalField(max_digits=14,decimal_places=2,validators=[V])
class SavingsGoal(models.Model):
 user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE); name=models.CharField(max_length=120); target_amount=models.DecimalField(max_digits=14,decimal_places=2,validators=[V]); current_amount=models.DecimalField(max_digits=14,decimal_places=2,default=0); target_date=models.DateField(null=True,blank=True); status=models.CharField(max_length=12,default="active"); created_at=models.DateTimeField(auto_now_add=True)
class GoalContribution(models.Model):
 goal=models.ForeignKey(SavingsGoal,on_delete=models.CASCADE,related_name="contributions"); amount=models.DecimalField(max_digits=14,decimal_places=2,validators=[V]); contributed_at=models.DateField(); note=models.CharField(max_length=255,blank=True)
class RecurringTransaction(models.Model):
 user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE); category=models.ForeignKey(Category,on_delete=models.PROTECT); transaction_type=models.CharField(max_length=7); amount=models.DecimalField(max_digits=14,decimal_places=2,validators=[V]); frequency=models.CharField(max_length=10); next_run_date=models.DateField(); end_date=models.DateField(null=True,blank=True); is_active=models.BooleanField(default=True)
class Bill(models.Model):
 user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE); name=models.CharField(max_length=120); amount=models.DecimalField(max_digits=14,decimal_places=2,validators=[V]); due_date=models.DateField(); frequency=models.CharField(max_length=10,default="monthly"); status=models.CharField(max_length=12,default="unpaid"); notes=models.TextField(blank=True)
class Debt(models.Model):
 user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE); person_name=models.CharField(max_length=120); debt_type=models.CharField(max_length=12,choices=[("lent","Lent"),("borrowed","Borrowed")]); original_amount=models.DecimalField(max_digits=14,decimal_places=2,validators=[V]); outstanding_amount=models.DecimalField(max_digits=14,decimal_places=2,validators=[V]); due_date=models.DateField(null=True,blank=True); status=models.CharField(max_length=12,default="open"); notes=models.TextField(blank=True)
class DebtPayment(models.Model):
 debt=models.ForeignKey(Debt,on_delete=models.CASCADE,related_name="payments"); amount=models.DecimalField(max_digits=14,decimal_places=2,validators=[V]); paid_at=models.DateField(); note=models.CharField(max_length=255,blank=True)
class Attachment(models.Model):
 user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE); transaction=models.ForeignKey(Transaction,on_delete=models.CASCADE,null=True,blank=True); file=models.FileField(upload_to="receipts/%Y/%m/"); original_name=models.CharField(max_length=255); created_at=models.DateTimeField(auto_now_add=True)
