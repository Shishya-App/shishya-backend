from rest_framework import serializers

from userpanel.models import *


class CustomDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomDocumentUploadModel
        fields = "__all__"
        
class ProfileDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileDocumentModel
        fields = "__all__"