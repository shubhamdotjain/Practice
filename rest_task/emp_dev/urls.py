from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
import views

router = DefaultRouter(trailing_slash=True)
router.include_format_suffixes = False
router.register('device', views.DeviceViewSet)
router.register('employee', views.EmployeeViewSet)


urlpatterns = [
        url(r"v1/", include(router.urls)),
    ]