from rest_framework.routers import SimpleRouter
from spendings import views

app_name = "spendings"
router = SimpleRouter(trailing_slash=True)

router.register('', views.SpendingsViewSet, basename='spendings')

urlpatterns = [] + router.urls
