from rest_framework import generics, parsers
from .models import *
from .serializers import *

class OwnedListCreate(generics.ListCreateAPIView):
    def perform_create(self, s): s.save(user=self.request.user)

class OwnedDetail(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self): return self.model.objects.filter(user=self.request.user)

class CategoryList(OwnedListCreate):
    serializer_class = CategorySerializer
    def get_queryset(self): return Category.objects.filter(user=self.request.user)

class CategoryDetail(OwnedDetail): model=Category; serializer_class=CategorySerializer

class TransactionList(OwnedListCreate):
    serializer_class = TransactionSerializer
    def get_queryset(self): return Transaction.objects.filter(user=self.request.user)

class TransactionDetail(OwnedDetail): model=Transaction; serializer_class=TransactionSerializer

class BudgetList(OwnedListCreate):
    serializer_class = BudgetSerializer
    def get_queryset(self): return Budget.objects.filter(user=self.request.user)

class BudgetDetail(OwnedDetail): model=Budget; serializer_class=BudgetSerializer

class GoalList(OwnedListCreate):
    serializer_class = GoalSerializer
    def get_queryset(self): return SavingsGoal.objects.filter(user=self.request.user)

class GoalDetail(OwnedDetail): model=SavingsGoal; serializer_class=GoalSerializer

class RecurringList(OwnedListCreate):
    serializer_class = RecurringSerializer
    def get_queryset(self): return RecurringTransaction.objects.filter(user=self.request.user)

class RecurringDetail(OwnedDetail): model=RecurringTransaction; serializer_class=RecurringSerializer

class BillList(OwnedListCreate):
    serializer_class = BillSerializer
    def get_queryset(self): return Bill.objects.filter(user=self.request.user)

class BillDetail(OwnedDetail): model=Bill; serializer_class=BillSerializer

class DebtList(OwnedListCreate):
    serializer_class = DebtSerializer
    def get_queryset(self): return Debt.objects.filter(user=self.request.user)

class DebtDetail(OwnedDetail): model=Debt; serializer_class=DebtSerializer

class AttachmentList(generics.ListCreateAPIView):
    serializer_class = AttachmentSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
    def get_queryset(self): return Attachment.objects.filter(user=self.request.user)
    def perform_create(self, s): s.save(user=self.request.user, original_name=self.request.FILES['file'].name)

class AttachmentDetail(generics.RetrieveDestroyAPIView):
    serializer_class = AttachmentSerializer
    def get_queryset(self): return Attachment.objects.filter(user=self.request.user)

class GoalContributionList(generics.ListCreateAPIView):
    serializer_class = GoalContributionSerializer
    def get_queryset(self): return GoalContribution.objects.filter(goal__user=self.request.user)
    def perform_create(self, s):
        goal = SavingsGoal.objects.get(pk=self.kwargs['goal_pk'], user=self.request.user)
        contribution = s.save(goal=goal)
        goal.current_amount = (goal.current_amount or 0) + s.validated_data['amount']
        if goal.current_amount >= goal.target_amount: goal.status = 'completed'
        goal.save()

class DebtPaymentList(generics.ListCreateAPIView):
    serializer_class = DebtPaymentSerializer
    def get_queryset(self): return DebtPayment.objects.filter(debt__user=self.request.user)
    def perform_create(self, s):
        debt = Debt.objects.get(pk=self.kwargs['debt_pk'], user=self.request.user)
        s.save(debt=debt)
        debt.outstanding_amount = max(0, (debt.outstanding_amount or 0) - s.validated_data['amount'])
        if debt.outstanding_amount == 0: debt.status = 'settled'
        debt.save()
