
from django.contrib import admin
from django.urls import path, include
from tracker.urls import router as tracker_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tracker/', include(tracker_router.urls))
]
