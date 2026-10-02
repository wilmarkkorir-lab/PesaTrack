from django.urls import path
from .views import BusinessList,BusinessDetail
urlpatterns=[path("businesses/",BusinessList.as_view()),path("businesses/<int:pk>/",BusinessDetail.as_view())]
