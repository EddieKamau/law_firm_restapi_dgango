from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Documents
from rest_framework.serializers import CharField, FileField



class DocumentsListSerializers(ModelSerializer):
    doc_name = SerializerMethodField()
    class Meta:
        model = Documents
        fields = [
            'id',
            'recipient',
            'subject',
            'file',
            'doc_name',
        ]

    def get_doc_name(self, obj):
        return str(obj.file)


class DocumentsCreateSerializers(ModelSerializer):
    # file = Base64ImageField()
    class Meta:
        model = Documents
        fields = [
            'recipient',
            'subject',
            'file'
        ]


