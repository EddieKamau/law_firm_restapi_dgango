from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Documents(models.Model):
    sender = models.ForeignKey(User, on_delete=None, related_name="owner", unique=False, blank=True, null=True)
    recipient = models.ForeignKey(User, on_delete=None, related_name="target", unique=False, blank=True, null=True)
    subject = models.CharField(max_length=20, blank=True, null=True)
    file = models.FileField()
    upload_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-upload_date']

    def __str__(self):
        return str(self.subject)
