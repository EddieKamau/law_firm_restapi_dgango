from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Events(models.Model):
    owner = models.ForeignKey(User, on_delete=None, related_name="event_owner", unique=False)
    title = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    notes = models.CharField(max_length=70)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return str(self.title) + ' - ' + str(self.start_date)