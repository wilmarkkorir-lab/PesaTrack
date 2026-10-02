from decimal import Decimal
from django.db.models import Sum
from django.db.models.functions import TruncMonth
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from finance.models import Transaction, Category

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def personal_summary(request):
    q = Transaction.objects.filter(user=request.user)
    income = q.filter(transaction_type="income").aggregate(x=Sum("amount"))["x"] or Decimal("0")
    expenses = q.filter(transaction_type="expense").aggregate(x=Sum("amount"))["x"] or Decimal("0")
    return Response({"income": income, "expenses": expenses, "balance": income - expenses, "currency": request.user.profile.currency})

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def monthly_breakdown(request):
    rows = (
        Transaction.objects.filter(user=request.user)
        .annotate(month=TruncMonth("transaction_date"))
        .values("month", "transaction_type")
        .annotate(total=Sum("amount"))
        .order_by("month")
    )
    # Pivot into {month, income, expenses}
    data = {}
    for r in rows:
        key = r["month"].strftime("%Y-%m")
        if key not in data:
            data[key] = {"month": key, "income": 0, "expenses": 0}
        data[key][r["transaction_type"] + ("s" if r["transaction_type"] == "expense" else "")] = float(r["total"])
    # fix key name: expense -> expenses
    for v in data.values():
        if "expense" in v:
            v["expenses"] = v.pop("expense")
    return Response(sorted(data.values(), key=lambda x: x["month"]))

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def category_breakdown(request):
    rows = (
        Transaction.objects.filter(user=request.user, transaction_type="expense")
        .values("category__name")
        .annotate(total=Sum("amount"))
        .order_by("-total")
    )
    return Response([{"name": r["category__name"] or "Uncategorised", "value": float(r["total"])} for r in rows])
