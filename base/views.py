# from .utils import Util
import jwt
from adminpanel.models import Adhaar
from adminpanel.serializers import AdhaarSerializer
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from rest_framework import generics, permissions, status, views
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from .serializers import (EmailVerificationSerializer, LoginSerializer,
                          LogoutSerializer, RegisterSerializer)
from .mixins import *
import random

# Create your views here.

# class RegisterView(generics.GenericAPIView):
#     serializer_class = RegisterSerializer
#     def post(self,request):
#         user=request.data
#         serializer = self.serializer_class(data=user)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         user_data = serializer.data
#         user = User.objects.get(email=user_data['email'])
#         token = RefreshToken.for_user(user).access_token
        
#         current_site = get_current_site(request).domain
#         relativeLink = '/email-verify/'
#         absurl = 'http://'+current_site+relativeLink+"?token="+str(token)
#         # print(token)
#         email_body = 'Hi ' + user_data['username'] + ',\n'\
#             'Click the link below to verify your email \n' + absurl
#         data = {'email_body': email_body, 'to_email': user.email,
#                 'email_subject': 'no-reply: Verify your Shishya account'}

#         Util.send_email(data)
#         return Response(user_data, status=status.HTTP_201_CREATED)


""" Adhaar Verification"""

    
class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    
    def post(self,request):
        user=request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        # user = User.objects.get(email=user_data['email'])
        # print(user_data['adhaar_no'])
        phone_no  = Adhaar.objects.filter(adhaar_no= user_data['adhaar_no'])
        phone_no_data = AdhaarSerializer(phone_no, many=True).data
        # data = [*phone_no_data]
        r = dict()
        r= phone_no_data[0]
        phone_number = r['phone_no']
        otp = random.randint(1000,9999)
        user = User.objects.get(email=user_data['email'])
        
        message_handle = MessageHandler(phone_number,otp).send_otp_on_phone()
        
        user.otp= otp
        user.save()
        return Response(user_data, status=status.HTTP_201_CREATED)
        
class VerifyOTP(views.APIView):
    
    def post(self,request):
        data= request.data
        user = User.objects.get(id=data['id'])
        
        a = user.otp
        b= data['OTP']
        
        if a==b:
           user.is_verified = True
           user.save() 
           return Response({'otp': 'Successfully verified'}, status=status.HTTP_200_OK)
        
        else:
            return Response({'error': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)
        

class VerifyEmail(views.APIView):
    serializer_class = EmailVerificationSerializer

    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY,algorithms=['HS256'])
            user = User.objects.get(id=payload['user_id'])
            if not user.is_verified:
                user.is_verified = True
                user.save()
            return Response({'email': 'Successfully activated'}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as identifier:
            return Response({'error': 'Activation Expired'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)

class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        user_data = serializer.data
        user = User.objects.get(username=user_data['username'])
        try:
            if not user.is_verified:
                return Response({"status": "User not verified"}, status=status.HTTP_403_FORBIDDEN)
        except user.DoesNotExist:
            return Response({"status": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer.is_valid(raise_exception=True)
        data= serializer.data
        data["first_name"]= user.first_name
        data["last_name"]= user.last_name
        return Response(data,status=status.HTTP_200_OK)

class LogoutAPIView(generics.GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = (permissions.IsAuthenticated,)
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


""" Email Verification"""

