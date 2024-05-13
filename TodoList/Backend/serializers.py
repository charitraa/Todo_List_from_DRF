from rest_framework.serializers import ModelSerializer
from .models import Todo

class TodoSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = ['description', 'created_at']

    def create(self, validated_data):
        return  Todo.objects.create(**validated_data)