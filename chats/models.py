from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_save
import datetime
from django.utils import timezone



# Create your models here.


class ChatsManager(models.Manager):
    def get_label(self, obj):
        return obj.__str__()

class MessagesManager(models.Manager):
    def get_parent_label(self, obj):
        chat = obj.parent
        return str(chat)


class Chats(models.Model):
    users = models.ManyToManyField(User)
    updated = models.DateTimeField()

    objects = ChatsManager()

    class Meta:
        ordering = ['-updated']

    def __str__(self):
        return str(self.users.all()[0]) + '-' + str(self.users.all()[1])

    def save(self, *args, **kwargs):
        self.updated = timezone.now()
        return super(Chats, self).save(*args, **kwargs)


class Messages(models.Model):
    sender = models.ForeignKey(User, on_delete=None, related_name="sender", unique=False)
    recipient = models.ForeignKey(User, on_delete=None, related_name="recipient", unique=False)
    parent = models.ForeignKey(Chats, on_delete=models.CASCADE)
    content = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)

    objects =MessagesManager()

    class Meta:
        ordering = ['upload_date']

    def __str__(self):
        return str(self.upload_date)


def pre_save_messages_receiver(sender, instance, *args, **kwargs):
    chat = Chats.objects.filter(users__in=[instance.recipient]).filter(users__in=[instance.sender])
    if chat.exists():
        instance.parent = chat[0]
        chat[0].save()
        chat[0].updated = timezone.now
    else:
        chat = Chats()
        chat.save()
        chat.updated=timezone.now
        chat.users.set([instance.sender, instance.recipient])
        instance.parent = chat

pre_save.connect(pre_save_messages_receiver, sender=Messages)
