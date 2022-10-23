from .views import ReportViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'stadistics', ReportViewSet, basename='stadistics')
urlpatterns = router.urls