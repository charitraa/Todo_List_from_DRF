from rest_framework import serializers
from .models import Todo

class TodoViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'

    def create(self, validated_data):
        return Todo.objects.create(**validated_data)
