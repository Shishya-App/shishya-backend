from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from adminpanel.views import (AllQuestionsView, DocumentViews,
                              FormQuestionFile, FormView, PersonalDetailsViews)

urlpatterns = [
    path('form/', FormView.as_view(), name='form'),
    path('form/<int:pk>', FormView.as_view(), name='form'),
    path('questions/file_type/<int:pk>/', FormQuestionFile.as_view(), name='questions' ),
    path('questions/file_type/', FormQuestionFile.as_view(), name='questions' ),
    path('personal-details/', PersonalDetailsViews.as_view(), name="personal-details"),
    path('document/', DocumentViews.as_view(), name="document"),
    path('document/<int:pk>/', DocumentViews.as_view(), name="document"),
    path('all-questions/<int:pk>', AllQuestionsView.as_view(), name="all-questions"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
