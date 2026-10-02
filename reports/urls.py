from django.urls import path
from .views import personal_summary, monthly_breakdown, category_breakdown

urlpatterns = [
    path("personal-summary/", personal_summary),
    path("monthly-breakdown/", monthly_breakdown),
    path("category-breakdown/", category_breakdown),
]
