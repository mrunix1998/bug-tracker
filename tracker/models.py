from django.db import models
from django.contrib.auth import get_user_model


class Bug(models.Model):
    added_on = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=120)
    assigned_to = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    due_date = models.DateTimeField(null=True)
    description = models.TextField(null=True, blank=True)
    closed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
