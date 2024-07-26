from rest_framework import serializers
from .models import Todo
from django.contrib.auth import get_user_model


User = get_user_model()


class TodoSerialazer(serializers.ModelSerializer):
    # using Serializer
    # id = serializers.IntegerField()   
    # title = serializers.CharField()
    class Meta:
        model = Todo
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    todos = TodoSerialazer(read_only=True, many=True)


    class Meta:
        model = User
        fields = '__all__'
