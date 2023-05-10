from rest_framework import serializers

from adminpanel.models import *


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

class PreVerifiedAnswerSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = PreVerifiedAnswer
        fields = [
            'id',
            'answer_text',
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
        
class TextTypeQuestionSerializer(serializers.ModelSerializer):
    
    answer = TextTypeAnswerSerializer(many=True, read_only=True)

    class Meta:
    
        model = Question
        fields = [
            'id','form','title','answer','technique',
        ]
        
class PreVerfiedQuestionTypeSerializer(serializers.ModelSerializer):
    answer = PreVerifiedAnswerSerializer(many=True, read_only=True)

    class Meta:
    
        model = Question
        fields = [
            'id','form','title','answer','technique',
        ]

class JobAnswerSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = JobAnswer
        fields = [
            'id',
            'answer_text',
        ]
class JobTextTypeAnswerSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = JobTextAnswer
        fields = [
            'id',
            'answer_text',
        ]

class JobPreVerifiedAnswerSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = JobPreVerifiedAnswer
        fields = [
            'id',
            'answer_text',
        ]       
class JobFileTypeAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = JobFileUploadAnswer
        fields = [
            'id',
            'File',
        ]

class JobSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Job
        fields = "__all__"


class JobFileTypeQuestionSerializer(serializers.ModelSerializer):

    answer = JobFileTypeAnswerSerializer(many=True, read_only=True)

    class Meta:
    
        model = JobQuestion
        fields = [
            'id','job','title','answer','technique',
        ]
        
        
class JobTextTypeQuestionSerializer(serializers.ModelSerializer):
    
    answer = JobTextTypeAnswerSerializer(many=True, read_only=True)

    class Meta:
    
        model = JobQuestion
        fields = [
            'id','job','title','answer','technique',
        ]
        
class JobPreVerfiedQuestionTypeSerializer(serializers.ModelSerializer):
    answer = JobPreVerifiedAnswerSerializer(many=True, read_only=True)

    class Meta:
    
        model = JobQuestion
        fields = [
            'id','job','title','answer','technique',
        ]
        
class SSCSerializer(serializers.ModelSerializer):
    class Meta:
        model = SSC
        fields = "__all__"

class HSCSerializer(serializers.ModelSerializer):
    class Meta:
        model = HSC
        fields = "__all__"
        
class AdhaarFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdhaarFile
        fields = "__all__"
        
class MigrationCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MigrationCertificate
        fields = "__all__"

class JEEmarksheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = JEEmarksheet
        fields = "__all__"

class JEEallotmentLetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = JEEallotmentLetter
        fields = "__all__"
        
        
class DisabilityCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisabilityCertificate
        fields = "__all__"

class BirthCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BirthCertificate
        fields = "__all__"

class DomicileCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DomicileCertificate
        fields = "__all__"
        
class PANSerializer(serializers.ModelSerializer):
    class Meta:
        model = PAN
        fields = "__all__"

class PassportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passport
        fields = "__all__"

class SportsCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SportsCertificate
        fields = "__all__"
        
class TransferCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransferCertificate
        fields = "__all__"

class CasteCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CasteCertificate
        fields = "__all__"

class IncomeCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeCertificate
        fields = "__all__"

class MedicalCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalCertificate
        fields = "__all__"
        
class IncomeCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeCertificate
        fields = "__all__"

class CasteCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CasteCertificate
        fields = "__all__"
        
class NationalityCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = NationalityCertificate
        fields = "__all__"
        
class AdhaarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adhaar
        fields = "__all__"