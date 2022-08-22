from django.http import Http404
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from adminpanel.models import DocumentModel, Form, PersonalDetails, Question

from .serializers import (DocumentSerializer, FileTypeAnswerSerializer, FormSerializer, MCQTypeQuestionSerializer,
                          PersonalDetailsSerializer, TextTypeQuestionSerializer)

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
    
    def get_object(self, pk):
        try:
            return DocumentModel.objects.get(pk=pk)
        except DocumentModel.DoesNotExist:
            raise Http404
    
    def get(self, request, format=None):
        doc = DocumentModel.objects.all()
        serializer = DocumentSerializer(doc, many=True)
        return Response(serializer.data)
    
    def get(self, request, pk):
        snippet = self.get_object(pk)
        serializer = DocumentSerializer(snippet)
        return Response(serializer.data)
    
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
        form = Question.objects.all()
        serializer = TextTypeQuestionSerializer(form, many=True)
        return Response(serializer.data,status = status.HTTP_200_OK)
    
    """Add questions to existing form"""
    
    def post(self, request, format=None):
        serializer = QuestionSerializer(data=request.data)
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
        form = Question.objects.all()
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
    serializer_class = FileTypeAnswerSerializer
    queryset = Question.objects.all()
    
    """View all questions of form"""
    
    def get_object(self, pk):
        try:
            return Form.objects.get(pk=pk)
        except Form.DoesNotExist:
            raise Http404
        
    def get(self, pk):
        form = self.get_object(pk)
        serializer = FileTypeAnswerSerializer(form)
        return Response(serializer.data)
    
    def get(self, request, format=None, **kwargs):
        form = Question.objects.all()
        serializer = FileTypeAnswerSerializer(form, many=True)
        return Response(serializer.data,status = status.HTTP_200_OK)
    
    """Add questions to existing form"""
    
    def post(self, request, format=None):
        serializer = FileTypeAnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    