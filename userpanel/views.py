import json
from adminpanel.models import DocumentModel
from django.http import Http404
from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from userpanel.models import *
from userpanel.serializers import *
from adminpanel.serializers import DocumentSerializer

# Create your views here.

class ProfileDocumentView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProfileDocumentSerializer
    queryset = ProfileDocumentModel.objects.all()
    def get(self, request):
        
        serializer = self.serializer_class(data=request.data)
        
        # if not serializer.is_valid():
        #     return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
        
        data = dict()
        data["user"]= request.user
        r = request.user
        doc = DocumentModel.objects.filter(user=r)
        doc1 = DocumentModel.objects.get(user=r)
        doc_data =DocumentSerializer(doc, many = True).data
        cus = CustomDocumentUploadModel.objects.filter(user=r)
        cus_data = CustomDocumentSerializer(cus, many = True).data
        data["NAD_Documents"]= doc1
        """uncomment in post request"""
        # custom_document = ProfileDocumentModel.objects.create(**data)
        # custom_document.save()
        view_doc= dict()
        view_doc["user"]= request.user.id
        view_doc["NAD_Document"]= [*doc_data]
        view_doc["Custom_Document"]= [*cus_data]
        # print(data)
        return Response(
            view_doc,
            status=status.HTTP_200_OK
        )
        
    
class CustomDocumentView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CustomDocumentSerializer
    queryset =CustomDocumentUploadModel.objects.all()
    
    """View all documents of CustomDocument"""
    
    def get_object(self, pk):
        try:
            return CustomDocumentUploadModel.objects.get(pk=pk)
        except CustomDocumentUploadModel.DoesNotExist:
            raise Http404
        
    def get(self, pk):
        form = self.get_object(pk)
        serializer = CustomDocumentSerializer(form)
        return Response(serializer.data)
    
    def get(self, request, format=None, **kwargs):
        form = CustomDocumentUploadModel.objects.all()
        serializer = CustomDocumentSerializer(form, many=True)
        return Response(serializer.data,status = status.HTTP_200_OK)
    
    """Add documents to profile"""
    
    def post(self, request, format=None):
        serializer = CustomDocumentSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
        data = serializer.validated_data
        user = User.objects.get(id=request.user.id)
        data["user"]= user
        # print(request.user.id)
        cus = CustomDocumentUploadModel.objects.create(**data)
        cus.save()
        
        return Response(
            {"success": "File uploaded successfully"},
            status=status.HTTP_201_CREATED
        )

class RecentUpload(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProfileDocumentSerializer
    queryset = ProfileDocumentModel.objects.all()

    def get(self, request):
        
        data = dict()
        data["user"]= request.user
        r = request.user

        cus = CustomDocumentUploadModel.objects.filter(user=r).order_by('-upload_time')
        cus_data = CustomDocumentSerializer(cus , many = True).data
        view_doc= dict()
        
        view_doc["Recent Upload"]= [*cus_data]
        len_view_doc = len(view_doc["Recent Upload"])
        # print(len_view_doc)
        if len_view_doc<=5:
        
            return Response(
                view_doc,
                status=status.HTTP_200_OK
            )
        
        else:
            final_doc= list()
            for x in view_doc["Recent Upload"]:
                final_doc.append(x)
                if len(final_doc) ==5:
                    break

            return Response(
                final_doc,
                status=status.HTTP_200_OK
            )
            
# class SubmitAnswer(generics.GenericAPIView):
#     permission_classes = [permissions.IsAuthenticated]
    
class SubmitFileQuestionView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SubmitFileQuestionSerializer
    
    def post(self, request, format=None):
        serializer = SubmitFileQuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SubmitPreVerifiedQuestionView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SubmitPreVerifiedQuestionSerializer
    
    def post(self, request, format=None):
        serializer = SubmitPreVerifiedQuestionSerializer(data=request.data)
        data = serializer.data
        data["user"] = request.user
        data["answer"] = DocumentModel.object.get(user=request.user)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
