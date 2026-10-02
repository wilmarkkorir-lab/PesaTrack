from rest_framework import serializers
from .models import *
class BusinessSerializer(serializers.ModelSerializer):
 class Meta: model=Business; fields="__all__"; read_only_fields=("owner",)
class CustomerSerializer(serializers.ModelSerializer):
 class Meta: model=Customer; fields="__all__"
class SupplierSerializer(serializers.ModelSerializer):
 class Meta: model=Supplier; fields="__all__"
class ProductSerializer(serializers.ModelSerializer):
 class Meta: model=ProductService; fields="__all__"
class InvoiceSerializer(serializers.ModelSerializer):
 class Meta: model=Invoice; fields="__all__"
class ExpenseSerializer(serializers.ModelSerializer):
 class Meta: model=BusinessExpense; fields="__all__"
