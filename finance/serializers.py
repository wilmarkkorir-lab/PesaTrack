from rest_framework import serializers
from .models import *
class CategorySerializer(serializers.ModelSerializer):
 class Meta: model=Category; fields="__all__"; read_only_fields=("user",)
class GoalContributionSerializer(serializers.ModelSerializer):
 class Meta: model=GoalContribution; fields="__all__"
class DebtPaymentSerializer(serializers.ModelSerializer):
 class Meta: model=DebtPayment; fields="__all__"
class TransactionSerializer(serializers.ModelSerializer):
 class Meta: model=Transaction; fields="__all__"; read_only_fields=("user",)
 def validate_category(self,v):
  if v.user!=self.context["request"].user: raise serializers.ValidationError("Invalid category")
  return v
class BudgetSerializer(serializers.ModelSerializer):
 class Meta: model=Budget; fields="__all__"; read_only_fields=("user",)
class GoalSerializer(serializers.ModelSerializer):
 class Meta: model=SavingsGoal; fields="__all__"; read_only_fields=("user","current_amount")
class RecurringSerializer(serializers.ModelSerializer):
 class Meta: model=RecurringTransaction; fields="__all__"; read_only_fields=("user",)
class BillSerializer(serializers.ModelSerializer):
 class Meta: model=Bill; fields="__all__"; read_only_fields=("user",)
class DebtSerializer(serializers.ModelSerializer):
 class Meta: model=Debt; fields="__all__"; read_only_fields=("user",)
class AttachmentSerializer(serializers.ModelSerializer):
 class Meta: model=Attachment; fields="__all__"; read_only_fields=("user",)
