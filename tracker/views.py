from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model
from .models import Bug
from .serializers import BugSerializer, UserSerializer


class BugViewSet(ModelViewSet):
    queryset = Bug.objects.all()
    serializer_class = BugSerializer


class UsersViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
