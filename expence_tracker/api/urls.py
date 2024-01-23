# api/urls.py
from django.urls import path
from expenses.views import ExpenseListAPIView, ExpenseDetailAPIView

urlpatterns = [
    path('expenses/', ExpenseListAPIView.as_view(), name='expense-list'),
    path('expenses/<int:pk>/', ExpenseDetailAPIView.as_view(), name='expense-detail'),
]
