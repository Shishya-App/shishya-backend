from django.http import Http404
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from adminpanel.models import DocumentModel, PersonalDetails,Form, Question
from .serializers import (DocumentSerializer, FormSerializer,
                                    PersonalDetailsSerializer, 
                                    QuestionSerializer,
                                    RandomQuestionSerializer)

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
        # serializer = PersonalDetailsSerializer(data, many=True)
        # print(data)
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
    # queryset = Form.objects.all()
    
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
        # form = Form.objects.filter(form = kwargs['pk'])
        # serializer = FormSerializer(form, many=True)
        # data = dict()
        # personal_detail_data = QuestionSerializer(form, many = True).data
        # data["questions"] = [*personal_detail_data]
        return Response(serializer.data,
            status = status.HTTP_200_OK)

class RandomQuestion(APIView):

    def get(self, request, format=None, **kwargs):
        question = Question.objects.filter(form__title=kwargs['topic']).order_by('?')[:1]
        serializer = RandomQuestionSerializer(question, many=True)
        return Response(serializer.data)

class FormQuestion(APIView):
    
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None, **kwargs):
        form = Question.objects.filter(form__title=kwargs['title'])
        serializer = QuestionSerializer(form, many=True)
        return Response(serializer.data)