from django.http import Http404
from django.shortcuts import render
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from adminpanel.models import DocumentModel, PersonalDetails
from adminpanel.serializers import DocumentSerializer, PersonalDetailsSerializer


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
        print(data)
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
