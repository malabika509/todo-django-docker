# CREATING THE ViewSet WITH FILTERING AND SEARCH OPERATIONS

from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Task
from .serializers import TaskSerializer


# Viewset handles the CRUD operations via DRF for Task
class TaskViewSet(viewsets.ModelViewSet):
    queryset=Task.objects.all().order_by('date') # default
    serializer_class=TaskSerializer
    
    # Enabling filtering and searching in API
    filter_backends=[DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Allowing filtering by date using ?search_date=2024-05-04
    filterset_fields=['date']

    # Allowing searching by title using ?search=Buy
    search_fields=['title']

    # Allowing ordering by date using ?ordering=date
    ordering_fields= ['date']
