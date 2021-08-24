
from django.urls import path
from rest_framework.routers import SimpleRouter
from spendings import views

app_name = "spendings"
router = SimpleRouter(trailing_slash=True)

router.register('', views.SpendingsViewSet, basename='spendings')
router.register('category/', views.SpendingCategoryViewSet, basename="category")

urlpatterns = [] + router.urls
