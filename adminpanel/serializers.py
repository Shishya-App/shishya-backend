from rest_framework import serializers
from adminpanel.models import PersonalDetails,DocumentModel

class PersonalDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model= PersonalDetails
        fields = "__all__"
        
class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model= DocumentModel
        fields = "__all__"
