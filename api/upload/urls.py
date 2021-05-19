from django.urls import path
from .views import FileViewSet
from rest_framework import routers
from django.urls import path, include

app_name = "upload"

router = routers.DefaultRouter()
router.register('file', FileViewSet)

urlpatterns = [
    path('', include(router.urls))
]


