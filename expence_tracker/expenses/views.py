# expenses/views.py
from rest_framework import generics
from .models import Expense
from .serializers import ExpenseSerializer

class ExpenseListAPIView(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class ExpenseDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
