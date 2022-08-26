from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from userpanel.views import *

urlpatterns = [
    path('custom-document/', CustomDocumentView.as_view(), name="custom-document"),
    path('profile-documents/',ProfileDocumentView.as_view(), name= "profile-documents"),
    path('recent-upload/', RecentUpload.as_view(), name= "recent-upload"),
    path('submit-file-question/',SubmitFileQuestionView.as_view(), name = "submit-file-question"),
    path('submit-preverified-question/',SubmitPreVerifiedQuestionView.as_view(), name = "submit-preverified-question"),
    # path('profile-documents/<int:pk>',ProfileDocumentView.as_view(), name= "profile-documents"),
]
