from rest_framework import serializers
from adminpanel.models import PersonalDetails,DocumentModel,Form, Question, Answer

class PersonalDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model= PersonalDetails
        fields = "__all__"
        
class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model= DocumentModel
        fields = "__all__"

class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Answer
        fields = [
            'id',
            'answer_text',
        ]

class RandomQuestionSerializer(serializers.ModelSerializer):

    answer = AnswerSerializer(many=True, read_only=True)

    class Meta:
    
        model = Question
        fields = [
            'title','answer',
        ]
        
class FormSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Form
        fields = "__all__"


class QuestionSerializer(serializers.ModelSerializer):

    answer = AnswerSerializer(many=True, read_only=True)
    # form = FormSerializer(read_only=True)
    form_id = Form.id

    class Meta:
    
        model = Question
        fields = [
            'id','form_id','title','answer','technique',
        ]
        

