from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers
from adminpanel.views import *

router = routers.DefaultRouter()
# router.register(r'document', DocumentViews, basename='document')
router.register(r'questions/pre-verified', FormQuestionPreVerified, basename='pre-verified')
router.register(r'questions/text', FormQuestionText, basename='text')
router.register(r'questions/file', FormQuestionFile, basename='file')
router.register(r'form', FormView, basename='form')


urlpatterns = [
    path('questions/<int:pk>', AllQuestionsView.as_view(), name="allq"),
    path('personal-details/', PersonalDetailsViews.as_view(), name="personal-details"),
    path('document/', DocumentViews.as_view(), name="document"),
    # path('document/<int:pk>/', DocumentViews.as_view(), name="document"),
    path('all-questions/<int:pk>', AllQuestionsView.as_view(), name="all-questions"),
    path('nad-docs/', NADdocumet.as_view(),  name= "nad-docs"),
    path('bool-docs/', DocumentBool.as_view(),  name= "bool-docs"),
    path('view-responses/', viewResponses.as_view(), name = "view-responses"),
    path('', include(router.urls))
]
