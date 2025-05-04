# CREATING SERIALIZER FOR THE Task MODEL

from rest_framework import serializers
from .models import Task

# Serializer translates the Task Model into JSON 
# Also validates new dat, i.e., creating and updating tasks
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model= Task # our Task model
        fields='__all__' # includes fields (title, description, date)

