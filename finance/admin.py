from django.contrib import admin
from .models import *
admin.site.register([Category,Transaction,Budget,BudgetCategory,SavingsGoal,GoalContribution,RecurringTransaction,Bill,Debt,DebtPayment,Attachment])
