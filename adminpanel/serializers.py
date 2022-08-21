from rest_framework import serializers

from adminpanel.models import (Answer, DocumentModel, FileUploadAnswer, Form,
                               McqOneAnswer, PersonalDetails, Question,
                               TextAnswer)


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
class TextTypeAnswerSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = TextAnswer
        fields = [
            'id',
            'answer_text',
        ]
class MCQTypeAnswerSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = McqOneAnswer
        fields = [
            'id',
            'choice',
        ]
class FileTypeAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = FileUploadAnswer
        fields = [
            'id',
            'File',
        ]

class FormSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Form
        fields = "__all__"


class FileTypeQuestionSerializer(serializers.ModelSerializer):

    answer = FileTypeAnswerSerializer(many=True, read_only=True)

    class Meta:
    
        model = Question
        fields = [
            'id','form','title','answer','technique',
        ]
        
class MCQTypeQuestionSerializer(serializers.ModelSerializer):
    
    answer = MCQTypeAnswerSerializer(many=True, read_only=True)

    class Meta:
    
        model = Question
        fields = [
            'id','form','title','answer','technique',
        ]
        
class TextTypeQuestionSerializer(serializers.ModelSerializer):
    
    answer = TextTypeAnswerSerializer(many=True, read_only=True)

    class Meta:
    
        model = Question
        fields = [
            'id','form','title','answer','technique',
        ]
        

