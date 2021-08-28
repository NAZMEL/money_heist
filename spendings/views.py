from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import SpendingSerializer, SpendingCategorySerializer
from .models import Spending, SpendingCategory
from .filters import SpendingFilter


class SpendingsViewSet(viewsets.ModelViewSet):

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

    permission_classes = (IsAuthenticated, )
    serializer_class = SpendingCategorySerializer

    def get_queryset(self):
        return SpendingCategory.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
