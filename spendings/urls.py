from rest_framework.routers import SimpleRouter
from spendings import views

app_name = "spendings"
router = SimpleRouter(trailing_slash=True)

router.register('create', views.SpendingsViewSet, basename='create-spending')
router.register('update', views.SpendingsViewSet, basename='update-spending')
router.register('category', views.SpendingCategoryViewSet, basename='category')
