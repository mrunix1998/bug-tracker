from rest_framework.routers import DefaultRouter
from .views import BugViewSet, UsersViewSet


router = DefaultRouter()
router.register(r'bugs', BugViewSet, basename='bugs')
router.register(r'users', UsersViewSet, basename='users')
