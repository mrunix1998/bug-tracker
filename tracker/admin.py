from django.contrib import admin

from .models import Bug


class BugAdmin(admin.ModelAdmin):
    pass


admin.site.register(Bug, BugAdmin)
