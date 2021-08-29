from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_csv.renderers import CSVRenderer

from spendings.serializers import SpendingSerializer, SpendingCategorySerializer
from spendings.models import Spending, SpendingCategory
from spendings.filters import SpendingFilter


class SpendingsViewSet(viewsets.ModelViewSet):
    """
    Takes JWT token for authorization.
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = SpendingSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = SpendingFilter

    def get_queryset(self):
        return Spending.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class SpendingCategoryViewSet(viewsets.ModelViewSet):
    """
    Takes JWT token for authorization.
    Returns list of all categories
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = SpendingCategorySerializer

    def get_queryset(self):
        return SpendingCategory.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ExportViewSet(viewsets.ModelViewSet):
    """
    Takes JWT token for authorization.
    Returns file .csv with all user's spendings
    """
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Spending.objects.filter(user=self.request.user)

    class SpendingRenderer(CSVRenderer):
        header = ['Amount', 'User', 'Category', 'Description', 'Created at']

    renderer_classes = (SpendingRenderer,)

    @action(methods=['GET'], detail=False, url_path='export-csv', url_name='export-csv')
    def export_csv(self, request):
        spendings = Spending.objects.filter(user=self.request.user)
        content = [{
            'Amount': spending.amount,
            'Category': spending.category.name,
            'Description': spending.description,
            'User': spending.user.email,
            'Created at': spending.created_at.strftime('%d, %b %Y - %Hh %Mm')
        } for spending in spendings]
        return Response(content)
