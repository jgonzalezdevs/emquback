from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import DeviceLogApiView, RegisterView, DeviceViewSet
router = DefaultRouter()
router.register(r'api/devices', DeviceViewSet, basename='devices')

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/user/registration/', RegisterView.as_view(), name='auth_register'),
    path('api/devices/ping/', DeviceLogApiView.as_view()), 
]

urlpatterns += router.urls