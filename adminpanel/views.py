from django.http import Http404
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from adminpanel.models import DocumentModel, Form, PersonalDetails, Question
from base.models import User

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
    
class FormView(APIView):
    
    serializer_class = FormSerializer
    permission_classes = [permissions.IsAuthenticated]
    # queryset = Form.objects.all()
    
    """View Form"""
    
    def get_object(self, pk):
        try:
            return Form.objects.get(pk=pk)
        except Form.DoesNotExist:
            raise Http404
        
    def get(self, pk):
        form = self.get_object(pk)
        serializer = FormSerializer(form)
        return Response(serializer.data)
    
    def get(self, request, format=None, **kwargs):
        form = Form.objects.all()
        serializer = FormSerializer(form, many=True)
        return Response(serializer.data,
            status = status.HTTP_200_OK)
        
    """Create Form"""
        
    def post(self, request, format=None):
        serializer = FormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FormQuestionText(generics.GenericAPIView):
    
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TextTypeQuestionSerializer
    queryset = Question.objects.all()
    
    """View all questions of form"""
    
    def get_object(self, pk):
        try:
            return Form.objects.get(pk=pk)
        except Form.DoesNotExist:
            raise Http404
        
    def get(self, pk):
        form = self.get_object(pk)
        serializer = TextTypeQuestionSerializer(form)
        return Response(serializer.data)
    
    def get(self, request, format=None, **kwargs):
        form = Question.objects.filter(technique='text')
        serializer = TextTypeQuestionSerializer(form, many=True)
        return Response(serializer.data,status = status.HTTP_200_OK)
    
    """Add questions to existing form"""
    
    def post(self, request, format=None):
        serializer = TextTypeQuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class FormQuestionMCQ(generics.GenericAPIView):
    
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = MCQTypeQuestionSerializer
    queryset = Question.objects.all()
    
    """View all questions of form"""
    
    def get_object(self, pk):
        try:
            return Form.objects.get(pk=pk)
        except Form.DoesNotExist:
            raise Http404
        
    def get(self, pk):
        form = self.get_object(pk)
        serializer = MCQTypeQuestionSerializer(form)
        return Response(serializer.data)
    
    def get(self, request, format=None, **kwargs):
        form = Question.objects.filter(technique='mcq_one')
        serializer = MCQTypeQuestionSerializer(form, many=True)
        return Response(serializer.data,status = status.HTTP_200_OK)
    
    """Add questions to existing form"""
    
    def post(self, request, format=None):
        serializer = MCQTypeQuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class FormQuestionFile(generics.GenericAPIView):
    
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FileTypeQuestionSerializer
    queryset = Question.objects.all()
    
    """View all questions of form"""
    
    def get_object(self, pk):
        try:
            return Form.objects.get(pk=pk)
        except Form.DoesNotExist:
            raise Http404
        
    def get(self, pk):
        form = self.get_object(pk)
        serializer = FileTypeQuestionSerializer(form)
        return Response(serializer.data)
    
    def get(self, request, format=None, **kwargs):
        form = Question.objects.filter(technique='file_upload')
        serializer = FileTypeQuestionSerializer(form, many=True)
        return Response(serializer.data,status = status.HTTP_200_OK)
    
    """Add questions to existing form"""
    
    def post(self, request, format=None):
        serializer = FileTypeQuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class FormQuestionPreVerified(generics.GenericAPIView):
    
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PreVerfiedQuestionTypeSerializer
    queryset = Question.objects.all()
    
    """View all questions of form"""
    
    def get_object(self, pk):
        try:
            return Form.objects.get(pk=pk)
        except Form.DoesNotExist:
            raise Http404
        
    def get(self, pk):
        form = self.get_object(pk)
        serializer = PreVerfiedQuestionTypeSerializer(form)
        return Response(serializer.data)
    
    def get(self, request, format=None, **kwargs):
        form = Question.objects.filter(technique='pre_verified')
        serializer = PreVerfiedQuestionTypeSerializer(form, many=True)
        return Response(serializer.data,status = status.HTTP_200_OK)
    
    """Add questions to existing form"""
    
    def post(self, request, format=None):
        serializer = PreVerfiedQuestionTypeSerializer(data=request.data)
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
        
        mcq = Question.objects.filter(technique='mcq', form= form)
        mcq_data =MCQTypeQuestionSerializer(mcq, many = True).data
        data["MCQ_questions"] = [*mcq_data] 
        
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
        
