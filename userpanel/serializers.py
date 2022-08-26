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
        
class SubmitFileQuestionSerializer(serializers.ModelSerializer):
    class Meta: 
        model= SubmitFileQuestion
        fields = "__all__"
class SubmitPreVerifiedQuestionSerializer(serializers.ModelSerializer):
    class Meta: 
        model= SubmitPreVerifiedQuestion
        fields = "__all__"
class SubmitTextQuestionSerializer(serializers.ModelSerializer):
    class Meta: 
        model= SubmitTextQuestion
        fields = "__all__"