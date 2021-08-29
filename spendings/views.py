from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_csv.renderers import CSVRenderer

from spendings.serializers import SpendingSerializer, SpendingCategorySerializer
from spendings.models import Spending, SpendingCategory
from spendings.filters import SpendingFilter


@swagger_auto_schema()
class SpendingsViewSet(viewsets.ModelViewSet):
    """
    Takes JWT token for authorization.
    list:
    Get the list of all spendings for a specific user
    retrieve:
    Get the spending by its id
    create:
    Takes a set of spending details: amount, category, description.
    Returns a created spending
    update:
    Update the spending by its id
    Takes a set of spending details: amount, category, description.
    partial_update:
    Update the spending by its id
    Takes a set of spending details: amount or category or description.
    delete:
    Delete the spending by its id
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
    list:
    Get the list of all categories for a specific user
    retrieve:
    Get the spending category by its id
    create:
    Takes the category name (unique name for a specific user)
    Returns a created category
    update:
    Update the spending category by its id
    Takes a new category name
    partial_update:
    Update the spending category by its id
    Takes a new category name
    delete:
    Delete the spending category by its id
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = SpendingCategorySerializer

    def get_queryset(self):
        return SpendingCategory.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ExportViewSet(viewsets.GenericViewSet):
    """
    Takes JWT token for authorization.
    Returns file .csv with all user's spendings
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = SpendingSerializer

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
