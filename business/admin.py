from django.contrib import admin
from .models import *
admin.site.register([Business,Membership,Customer,Supplier,ProductService,Invoice,InvoiceItem,InvoicePayment,BusinessExpense,AuditLog])
