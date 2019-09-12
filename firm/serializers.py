from rest_framework.serializers import ModelSerializer, SerializerMethodField, ValidationError
from rest_framework.serializers import EmailField, CharField, IntegerField

from django.contrib.auth.models import User
from firm.models import Client, ActivationKeys
from cases.models import Cases

from django.core.mail import EmailMessage

def send_mail(subject, body, to):
    email = EmailMessage(subject, body, to=to)
    email.send()


class ClientSerializerView(ModelSerializer):
    phone_no = SerializerMethodField()
    address = SerializerMethodField()
    case_no = SerializerMethodField()
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'phone_no',
            'address',
            'case_no',
        ]

    def get_address(self, obj):
        client = Client.objects.filter(client_id=obj.id)
        if client.exists():
            address = client[0].address
        else: address = None

        return address

    def get_case_no(self, obj):
        client = Client.objects.filter(client_id=obj.id).first()
        case = Cases.objects.filter(client=client)
        if case.exists():
            case_no = case[0].case_no
        else: case_no = ""

        return case_no


    def get_phone_no(self, obj):
        client = Client.objects.filter(client_id=obj.id)
        if client.exists():
            phone_no = client[0].phone_no
        else: phone_no = None

        return phone_no

import random
def create_activation_key(owner):
    items = ['1','2','3','4','5','6','7','8','9','0',
             'a','b','c','d','e','f','g','h','i','j',
             'k','l','m','n','o','p','q','r','s','t',
             'u','v','w','x','y','z','0','1','2','3',
             '4','5','6','7','8','9']
    gen= random.choices(items, k=8)
    key = ''.join(map(str, gen))

    key_qs = ActivationKeys.objects.filter(key=key)
    while key_qs.exists():
        key = create_activation_key()
        key_qs = ActivationKeys.objects.filter(key=key)

    activation_key = ActivationKeys(
        owner=owner,
        key=key,
        active=True
    )
    activation_key.save()

    return key


class ClientCreateSerializer(ModelSerializer):
    username = CharField(label="Username", required=True)
    first_name = CharField(label="Fist Name", required=True)
    last_name = CharField(label="Last Name", required=True)
    email = EmailField(label="Email address", required=True)
    c_email = EmailField(label="Confirm Email", required=True)
    phone_no = IntegerField(required=True)
    address = CharField(label="Postal address", required=False)
    class Meta:
        model = Client
        fields = [
            'username',
            'first_name',
            'last_name',
            'phone_no',
            'address',
            'email',
            'c_email'
        ]

    def validate_username(self, data):
        user = User.objects.filter(username=data)
        if user.exists():
            raise ValidationError("User Exists")

        return data

    def validate_c_email(self, c_email):
        data = self.get_initial()
        email = data.get("email")
        if email != c_email:
            raise ValidationError("Email must much.")
        return c_email


    def create(self, data):
        username = data["username"]
        first_name = data["first_name"]
        last_name = data["last_name"]
        phone_no = data["phone_no"]
        address = data["address"]
        email = data["email"]

        user = User(
            username = username,
            first_name = first_name,
            last_name = last_name,
            email = email,
            is_active=False
        )
        user.save()
        client = Client(
            client_id=user,
            phone_no=phone_no,
            address=address
        )
        client.save()

        key = create_activation_key(user)


        send_mail("Hi, Welcome to KNM.", "You have been created an account, input the following key as your activation key " +  key, [user.email])


        return data


class SignUp(ModelSerializer):
    username = CharField(max_length=20, required=True)
    activation_key = CharField(max_length=20, required=True)
    password = CharField(max_length=20, required=True)
    c_password = CharField(max_length=20, required=True, label='Confirm Password')
    class Meta:
        model = Client
        fields =[
            "username",
            "activation_key",
            "password",
            "c_password"
        ]

    def get_c_password(self, c_password):
        data = self.initial()
        password = data.get("password")
        if password != c_password:
            return ValidationError("Password should much.")

        return c_password

    def validate(self, data):
        activation_key = data["activation_key"]
        username = data["username"]
        key_is_active = ActivationKeys.objects.filter(key=activation_key)
        if not key_is_active[0].active:
            raise ValidationError("Activation key is out of use. Kindly request another one.")
        user = User.objects.filter(username=username)
        if not user.exists():
            raise ValidationError("Username does not exist")
        return data

    def create(self, validated_data):
        username = validated_data["username"]
        activation_key = validated_data["activation_key"]
        password = validated_data["password"]

        # key = ActivationKeys.objects.filter(owner__client_id__username="fromApi3").first()
        key = ActivationKeys.objects.filter(key=activation_key).first()
        user = User.objects.filter(client__activationkeys__key=activation_key).first()
        if str(username)==str(user.username):
            user = User.objects.filter(username=username).first()
            user.is_active = True
            user.set_password(password)
            user.save()
            key.active = False
            key.save()
        else:raise ValidationError("Invalid activation key")

        return validated_data


class ResetPasswordSerializer(ModelSerializer):
    username = CharField(max_length=20, required=True)
    activation_key = CharField(max_length=20, required=True, label='Reset Code')
    password = CharField(max_length=20, required=True)
    c_password = CharField(max_length=20, required=True, label='Confirm Password')
    class Meta:
        model = Client
        fields =[
            "username",
            "activation_key",
            "password",
            "c_password"
        ]

    def get_c_password(self, c_password):
        data = self.initial()
        password = data.get("password")
        if password != c_password:
            return ValidationError("Password should much.")

        return c_password

    def validate(self, data):
        activation_key = data["activation_key"]
        username = data["username"]
        key_is_active = ActivationKeys.objects.filter(key=activation_key)
        if not key_is_active[0].active:
            raise ValidationError("Activation key is out of use. Kindly request another one.")
        user = User.objects.filter(username=username)
        if not user.exists():
            raise ValidationError("Username does not exist")
        return data

    def create(self, validated_data):
        username = validated_data["username"]
        activation_key = validated_data["activation_key"]
        password = validated_data["password"]

        # key = ActivationKeys.objects.filter(owner__client_id__username="fromApi3").first()
        key = ActivationKeys.objects.filter(key=activation_key).first()
        user = User.objects.filter(client__activationkeys__key=activation_key).first()
        if str(username) == str(user.username):
            user = User.objects.filter(username=username).first()
            user.is_active = True
            user.set_password(password)
            user.save()
            key.active = False
            key.save()
        else:
            raise ValidationError("Invalid activation key")

        return validated_data


class ClientForgottenPasswordSerializer(ModelSerializer):
    username = CharField(label="Username")
    email = EmailField(label="Email Address")
    class Meta:
        model = User
        fields = [
            'username',
            'email',
        ]

    def validate(self, data):
        username = data['username']
        email = data['email']

        user = User.objects.filter(username=username).filter(email=email)
        if not user.exists():
            raise ValidationError("Wrong Credentials")

        return data

    def create(self, validated_data):
        username = validated_data['username']

        # client = Client.objects.filter(client_id__username=username).first()
        user = User.objects.filter(username=username).first()

        key = create_activation_key(user)

        print(key, user)
        send_mail("Hi, your request to reset password was processed.", "Input the following key as reset key " + key, [user.email])

        return validated_data


#
# class ClientCreateSerializer(ModelSerializer):
#     c_email = EmailField(label="Confirm Email")
#     class Meta:
#         model = User
#         fields = [
#             'username',
#             'first_name',
#             'last_name',
#             'email',
#             'c_email'
#         ]
#


class UsernameSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'is_staff',
        ]






















