from django.contrib import admin
from django.urls import path

from userpanel.views import CustomDocumentView, ProfileDocumentView, RecentUpload

urlpatterns = [
    path('custom-document/', CustomDocumentView.as_view(), name="custom-document"),
    path('profile-documents/',ProfileDocumentView.as_view(), name= "profile-documents"),
    path('recent-upload/', RecentUpload.as_view(), name= "recent-upload")
    # path('profile-documents/<int:pk>',ProfileDocumentView.as_view(), name= "profile-documents"),
]
