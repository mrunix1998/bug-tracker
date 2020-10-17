from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model
from .models import Bug


class BugSerializer(ModelSerializer):
    class Meta:
        model = Bug
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['pk', 'username']
