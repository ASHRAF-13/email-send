from rest_framework.routers import DefaultRouter
from .views import SendemailViewSet
from django.urls import path, include

router = DefaultRouter()
router.register('sendkar',SendemailViewSet)

urlpatterns = [
        path('api/', include(router.urls))
]