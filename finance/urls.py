from django.urls import path
from . import views
urlpatterns=[]
for n,l,d in [("categories",views.CategoryList,views.CategoryDetail),("transactions",views.TransactionList,views.TransactionDetail),("budgets",views.BudgetList,views.BudgetDetail),("goals",views.GoalList,views.GoalDetail),("recurring",views.RecurringList,views.RecurringDetail),("bills",views.BillList,views.BillDetail),("debts",views.DebtList,views.DebtDetail)]: urlpatterns += [path(f"{n}/",l.as_view()),path(f"{n}/<int:pk>/",d.as_view())]
urlpatterns += [
    path("attachments/", views.AttachmentList.as_view()),
    path("attachments/<int:pk>/", views.AttachmentDetail.as_view()),
    path("goals/<int:goal_pk>/contributions/", views.GoalContributionList.as_view()),
    path("debts/<int:debt_pk>/payments/", views.DebtPaymentList.as_view()),
]
