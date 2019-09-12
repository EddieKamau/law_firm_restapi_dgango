from django.db import models
#from django.conf import settings

from django.contrib.auth.models import User


class Lawyer(models.Model):
    lawyer_id = models.OneToOneField(User, on_delete=models.CASCADE)
    l_type = models.CharField(max_length=20)
    phone_no = models.IntegerField()
    address = models.CharField(max_length=30)

    def __str__(self):
        return str(self.lawyer_id.username)


class Client(models.Model):
    client_id = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_no = models.IntegerField()
    address = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return str(self.client_id.username)

class ActivationKeys(models.Model):
    owner = models.ForeignKey(User, unique=False, on_delete=None)
    key = models.CharField(max_length=10)
    active = models.BooleanField()

    def __str__(self):
        return str(self.key)


