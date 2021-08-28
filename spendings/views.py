from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from spendings.serializers import SpendingSerializer, SpendingCategorySerializer
from spendings.models import Spending, SpendingCategory
from spendings.filters import SpendingFilter


class SpendingsViewSet(viewsets.ModelViewSet):
    """
    Takes JWT token for authorization.
    """
    permission_classes = (IsAuthenticated, )
    serializer_class = SpendingSerializer
    filter_backends = (DjangoFilterBackend, )
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
    permission_classes = (IsAuthenticated, )
    serializer_class = SpendingCategorySerializer

    def get_queryset(self):
        return SpendingCategory.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
