from django.http import Http404
from rest_framework import generics, permissions, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from adminpanel.models import DocumentModel, Form, PersonalDetails, Question
from base.models import User
from userpanel.models import SubmitFileQuestion, SubmitPreVerifiedQuestion
from userpanel.serializers import SubmitFileQuestionSerializer, SubmitPreVerifiedQuestionSerializer
from rest_framework.decorators import action

from .serializers import *

from operator import itemgetter

# Create your views here.

class PersonalDetailsViews(APIView):
    
    serializer_class = PersonalDetailsSerializer
    queryset = PersonalDetails.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ["get"]
    def get(self, request, format=None):
        account = request.user
        data = dict()
        personal_detail = PersonalDetails.objects.filter(user=account)
        personal_detail_data = PersonalDetailsSerializer(personal_detail, many = True).data
        data["personal_details"] = [*personal_detail_data]

        return Response(
            data,
            status = status.HTTP_200_OK
        )
        
class DocumentViews(APIView):
    
    def get(self, request, format=None):
        doc = DocumentModel.objects.filter(user=request.user)
        serializer = DocumentSerializer(doc, many=True).data
        
        return Response(serializer)

class DocumentBool(APIView):
    
    def get(self,request,format=None):
        doc = DocumentModel.objects.filter(user=request.user)
        serializer = DocumentSerializer(doc, many=True).data
        data= dict()
        data = [*serializer]
        sample = dict()
        for key,value in data[0].items():
            # if value=='null':
            # print(key)
            # print(value)
            if value == None:
                sample[key] = False
            else:
                sample[key] = True
        sample.pop("id")
        sample.pop("user")
        return Response(sample)         
    
class FormView(viewsets.ModelViewSet):
    
    permission_classes = [permissions.IsAuthenticated]
    action_serializers = {
        'job': JobSerializer,
        'college': FormSerializer
    }
    queryset = Form.objects.all()
    
    def get_serializer_class(self):
        if hasattr(self, 'action_serializers'):
            return self.action_serializers.get(self.action, self.serializer_class)

        return super(FormQuestionPreVerified, self).get_serializer_class()
    
    @action(detail=False, methods=['post', 'get'],url_path='job')
    def job(self, request, format=None):
        if request.method == 'GET':
            job= Job.objects.filter(owner = request.user)
            form_data = self.get_serializer_class()(job, many=True).data
            return Response(form_data,
                status = status.HTTP_200_OK)
            
        serializer = self.get_serializer_class()(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['post', 'get'],url_path='college')
    def college(self, request, format=None):
        if request.method == 'GET':
            form = Form.objects.filter(owner = request.user)
            form_data = self.get_serializer_class()(form, many=True).data
            return Response(form_data,status = status.HTTP_200_OK)
        
        serializer = self.get_serializer_class()(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FormQuestionText(viewsets.ModelViewSet):
    
    permission_classes = [permissions.IsAuthenticated]
    action_serializers = {
        'job': JobTextTypeQuestionSerializer,
        'college': TextTypeQuestionSerializer
    }
    
    def get_serializer_class(self):
        if hasattr(self, 'action_serializers'):
            return self.action_serializers.get(self.action, self.serializer_class)

        return super(FormQuestionText, self).get_serializer_class()
    
    """Add questions to existing form"""
    
    @action(detail=False, methods=['post', 'get'],url_path='college')
    def college(self, request, format=None,**kwargs):
        serializer = self.get_serializer_class()(data=request.data)
        if request.method == 'GET':
            form_id = request.query_params.get('form')
            
            if form_id:
                form = Question.objects.filter(form=form_id, technique='text')
                serializer = self.get_serializer_class()(form, many=True)
                return Response(serializer.data,status = status.HTTP_200_OK)
            else:
                form = Question.objects.filter(technique='text')
                serializer = self.get_serializer_class()(form, many=True)
                return Response(serializer.data,status = status.HTTP_200_OK)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    @action(detail=False, methods=['post', 'get'],url_path='job')
    def job(self,request):
        serializer = self.get_serializer_class()(data=request.data)
        if request.method == 'GET':
            job_id = request.query_params.get('job')
            if job_id:
                job = JobQuestion.objects.filter(job=job_id, technique='text')
                serializer = self.get_serializer_class()(job, many=True)
                return Response(serializer.data,status = status.HTTP_200_OK)
            else:
                job = JobQuestion.objects.filter(technique='text')
                serializer = self.get_serializer_class()(job, many=True)
                return Response(serializer.data,status = status.HTTP_200_OK)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class FormQuestionFile(viewsets.ModelViewSet):
    queryset = Question.objects.filter(technique='file_upload')
    action_serializers = {
        'job': JobFileTypeQuestionSerializer,
        'college': FileTypeQuestionSerializer
    }
    permission_classes = [permissions.IsAuthenticated]
    
    def get_serializer_class(self):
        if hasattr(self, 'action_serializers'):
            return self.action_serializers.get(self.action, self.serializer_class)

        return super(FormQuestionFile, self).get_serializer_class()
    
    @action(detail=False, methods=['post', 'get'],url_path='college')
    def college(self, request, format=None,**kwargs):
        serializer = self.get_serializer_class()(data=request.data)
        if request.method == 'GET':
            form_id = request.query_params.get('form')
            if form_id:
                form = Question.objects.filter(form=form_id, technique='file_upload')
                serializer = self.get_serializer_class()(form, many=True)
                return Response(serializer.data,status = status.HTTP_200_OK)
            else:
                form = Question.objects.filter(technique='file_upload')
                serializer = self.get_serializer_class()(form, many=True)
                return Response(serializer.data,status = status.HTTP_200_OK)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['post', 'get'],url_path='job')
    def job(self,request):
        serializer = self.get_serializer_class()(data=request.data)
        if request.method == 'GET':
            job_id = request.query_params.get('job')
            if job_id:
                job = JobQuestion.objects.filter(job=job_id, technique='file_upload')
                serializer = self.get_serializer_class()(job, many=True)
                return Response(serializer.data,status = status.HTTP_200_OK)
            else:
                job = JobQuestion.objects.filter(technique='file_upload')
                serializer = self.get_serializer_class()(job, many=True)
                return Response(serializer.data,status = status.HTTP_200_OK)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class FormQuestionPreVerified(viewsets.ModelViewSet):
    queryset = Question.objects.filter(technique='pre_verified')
    action_serializers = {
        'job': JobPreVerfiedQuestionTypeSerializer,
        'college': PreVerfiedQuestionTypeSerializer
    }
    permission_classes = [permissions.IsAuthenticated]
    
    def get_serializer_class(self):
        if hasattr(self, 'action_serializers'):
            return self.action_serializers.get(self.action, self.serializer_class)

        return super(FormQuestionPreVerified, self).get_serializer_class()
    """Add questions to existing form"""
    
    @action(detail=False, methods=['post', 'get'],url_path='college')
    def college(self, request, format=None,**kwargs):
        serializer = self.get_serializer_class()(data=request.data)
        
        if request.method == 'GET':
            form_id = request.query_params.get('form')
            print(form_id)
            if form_id:
                form = Question.objects.filter(form=form_id, technique='pre_verified')
                serializer = self.get_serializer_class()(form, many=True)
                return Response(serializer.data,status = status.HTTP_200_OK)
            else:
                form = Question.objects.filter(technique='pre_verified')
                serializer = self.get_serializer_class()(form, many=True)
                return Response(serializer.data,status = status.HTTP_200_OK)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['post', 'get'],url_path='job')
    def job(self,request):
        serializer = self.get_serializer_class()(data=request.data)
        if request.method == 'GET':
            job_id = request.query_params.get('job')
            if job_id:
                job = JobQuestion.objects.filter(job=job_id, technique='pre_verified')
                serializer = self.get_serializer_class()(job, many=True)
                return Response(serializer.data,status = status.HTTP_200_OK)
            else:
                job = JobQuestion.objects.filter(technique='pre_verified')
                serializer = self.get_serializer_class()(job, many=True)
                return Response(serializer.data,status = status.HTTP_200_OK)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class AllQuestionsView(generics.GenericAPIView):
    
    
    def get(self,request,pk, **kwargs):
        data= dict()
        form = Form.objects.get(pk=pk)
        
        text = Question.objects.filter(technique='text', form= form)
        text_data =TextTypeQuestionSerializer(text, many = True).data
        data["text_questions"] = [*text_data] 
        
        file = Question.objects.filter(technique='file_upload', form= form)
        file_data =FileTypeQuestionSerializer(file, many = True).data
        data["file_questions"] = [*file_data] 
        
        pre = Question.objects.filter(technique='pre_verified', form= form)
        pre_data = PreVerfiedQuestionTypeSerializer(pre, many = True).data
        data["pre_verified"] = [*pre_data] 
        
        return Response(
            data,
            status = status.HTTP_200_OK
        )
        
        
class NADdocumet(APIView):
    
    def get(self, request):
        data = dict()
        user = User.objects.get(id=2)
        
        datadict= DocumentModel.objects.filter(user=user)
        datadict_data = DocumentSerializer(datadict, many = True).data
        data = [*datadict_data]
        
        sample_dict= dict()
        sample_dict= data[0]

        final_list= list(sample_dict.keys())
        final_list.pop(0)
        final_list.pop(0)
        
        return Response(
            final_list,
            status = status.HTTP_200_OK
        )

        
class viewResponses(APIView):
    
    def get(self,request):
        data = dict()
        forms = Form.objects.filter(owner=request.user)
        
        # get all responses from submitfile question model and sumit pre verified question model of forms created by request.user
        
        for form in forms:
            FileResponses =  SubmitFileQuestion.objects.filter(form=form)
            FileResponses_data =  SubmitFileQuestionSerializer(FileResponses, many=True).data
            data['custom_upload']= FileResponses_data
            
            PreResponses =  SubmitPreVerifiedQuestion.objects.filter(form=form)
            PreResponses_data =  SubmitPreVerifiedQuestionSerializer(PreResponses, many=True).data
            data['Pre Verified']= PreResponses_data
        

            
        return Response(
            data,
            status=status.HTTP_200_OK
        )
    
    def post(self,request):
       data = dict()
       data_input = request.data
       FileResponses =  SubmitFileQuestion.objects.filter(form=data_input["form"])
       FileResponses_data =  SubmitFileQuestionSerializer(FileResponses, many=True).data
       
       PreResponses =  SubmitPreVerifiedQuestion.objects.filter(form=data_input["form"])
       PreResponses_data =  SubmitPreVerifiedQuestionSerializer(PreResponses, many=True).data
       
       data["Custom_Upload"]= FileResponses_data
       data["Pre Verified"] = PreResponses_data
       
       return Response(
           data,
           status=status.HTTP_200_OK
       )