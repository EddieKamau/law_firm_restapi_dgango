from rest_framework.serializers import ModelSerializer, SerializerMethodField
from chats.models import Messages, Chats
from django.contrib.auth.models import User
from rest_framework.serializers import CharField


class ChatsListSerializers(ModelSerializer):
    messages = SerializerMethodField()
    label = SerializerMethodField()
    users = SerializerMethodField()
    class Meta:
        model = Chats
        fields =[
            'id',
            'label',
            'users',
            'updated',
            'messages',
        ]

    def get_messages(self, obj):
        return MessagesSerializers(Messages.objects.filter(parent=obj), many=True).data

    def get_label(self, obj):
        return Chats.objects.get_label(obj)

    def get_users(self, obj):
        return [obj.users.all()[0].username, obj.users.all()[1].username]


class MessagesSerializers(ModelSerializer):
    sender = SerializerMethodField()
    recipient = SerializerMethodField()
    # parent = SerializerMethodField()

    class Meta:
        model = Messages
        fields = [
            'id',
            #'parent',
            'sender',
            'recipient',
            'content',
            'upload_date'
        ]

    def get_sender(self, obj):
        return str(obj.sender.username)

    def get_recipient(self, obj):
        return str(obj.recipient.username)

    # def get_parent(self, obj):
    #     return str(Messages.objects.get_parent_label(obj))


class MessagesCreateSerializers(ModelSerializer):
    class Meta:
        model = Messages
        fields = [
            'recipient',
            'content',
        ]


class MessagesDetailSerializers(ModelSerializer):
    sender = SerializerMethodField()
    recipient = SerializerMethodField()
    parent = SerializerMethodField()

    class Meta:
        model = Messages
        fields = [
            'id',
            'parent',
            'sender',
            'recipient',
            'content',
            'upload_date'
        ]

    def get_sender(self, obj):
        return str(obj.sender.username)

    def get_recipient(self, obj):
        return str(obj.recipient.username)

    def get_parent(self, obj):
        return str(Messages.objects.get_parent_label(obj))




#####################################################################################################################



class ChatMessages(ModelSerializer):
    sender = SerializerMethodField()
    class Meta:
        model = Messages
        fields = [
            'sender',
            'content',
            'upload_date'
        ]

    def get_sender(self, obj):
        return str(obj.sender.username)


class ChatListViewSerializer(ModelSerializer):
    buddy = SerializerMethodField()
    last_message = SerializerMethodField()
    class Meta:
        model = Chats
        fields = [
            'id',
            'buddy',
            'updated',
            'last_message',
        ]

    def get_buddy(self, obj):
        user1 = obj.users.all()[0].username
        user2 =obj.users.all()[1].username
        user = str(user1) if str(self.context.get("user")) == str(user2) else str(user2)
        buddy_id = User.objects.filter(username=user).first()
        buddy_id = buddy_id.id
        return user, buddy_id

    def get_last_message(self, obj):
        mess = Messages.objects.filter(parent=obj).last()

        return mess.content

class ChatMessagesSerializer(ModelSerializer):
    messages = SerializerMethodField()
    user = SerializerMethodField()
    buddy = SerializerMethodField()
    class Meta:
        model = Chats
        fields = [
            'user',
            'buddy',
            'messages',
        ]

    def get_messages(self, obj):
        mess = Chats.objects.filter(users__in=[self.context.get("user")]).filter(id=obj.id).first()
        if mess is not None:
         return ChatMessages(Messages.objects.filter(parent=obj), many=True).data

    def get_user(self, obj):
        return str(self.context.get("user"))

    def get_buddy(self, obj):
        user1 = obj.users.all()[0].username
        user2 =obj.users.all()[1].username
        buddy_name = str(user1) if str(self.context.get("user")) == str(user2) else str(user2)
        buddy_id = User.objects.filter(username=buddy_name).first()
        buddy_id = buddy_id.id
        return [buddy_name, buddy_id]



















