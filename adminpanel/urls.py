from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from adminpanel.views import *

urlpatterns = [
    path('form/', FormView.as_view(), name='form'),
    path('form/<int:pk>', FormView.as_view(), name='form'),
    path('questions/file/<int:pk>/', FormQuestionFile.as_view(), name='questions' ),
    path('questions/file/', FormQuestionFile.as_view(), name='questions' ),
    path('questions/mcq/<int:pk>/', FormQuestionMCQ.as_view(), name='questions' ),
    path('questions/mcq/', FormQuestionMCQ.as_view(), name='questions' ),
    path('questions/pre-verified/<int:pk>/', FormQuestionPreVerified.as_view(), name='questions' ),
    path('questions/pre-verified/', FormQuestionPreVerified.as_view(), name='questions' ),
    path('questions/text/<int:pk>/', FormQuestionText.as_view(), name='questions' ),
    path('questions/text/', FormQuestionText.as_view(), name='questions' ),
    path('personal-details/', PersonalDetailsViews.as_view(), name="personal-details"),
    path('document/', DocumentViews.as_view(), name="document"),
    path('document/<int:pk>/', DocumentViews.as_view(), name="document"),
    path('all-questions/<int:pk>', AllQuestionsView.as_view(), name="all-questions"),
    path('nad-docs/', NADdocumet.as_view(),  name= "nad-docs"),
]
