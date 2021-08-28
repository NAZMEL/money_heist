from rest_framework.routers import SimpleRouter

from spendings import views


app_name = "spendings"

router = SimpleRouter(trailing_slash=True)

router.register('categories', views.SpendingCategoryViewSet, basename='categories')
router.register('export', views.ExportViewSet, basename='export')
router.register('', views.SpendingsViewSet, basename='spendings')

urlpatterns = [] + router.urls
