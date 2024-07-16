from rest_framework import serializers
from .models import Todo

class TodoSerialazer(serializers.ModelSerializer):
    # using Serializer
    # id = serializers.IntegerField()   
    # title = serializers.CharField()
    class Meta:
        model = Todo
        fields = ['id', 'title', 'content']