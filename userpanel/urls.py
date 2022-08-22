from django.contrib import admin
from django.urls import path

from userpanel.views import CustomDocumentView, ProfileDocumentView

urlpatterns = [
    path('custom-document/', CustomDocumentView.as_view(), name="custom-document"),
    path('profile-documents/',ProfileDocumentView.as_view(), name= "profile-documents"),
    # path('profile-documents/<int:pk>',ProfileDocumentView.as_view(), name= "profile-documents"),
]
