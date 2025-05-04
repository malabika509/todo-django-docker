# SETTING UP URL ROUTING

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

# For automatically generating URLS for CRUd operations by Router
router= DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls)),
]