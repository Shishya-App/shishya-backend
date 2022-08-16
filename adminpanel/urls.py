from rest_framework import routers
from django.urls import path
from adminpanel.views import PersonalDetailsViews,DocumentViews, FormView, FormQuestion


urlpatterns = [
    path('form/', FormView.as_view(), name='form'),
    path('form/<int:pk>', FormView.as_view(), name='form'),
    path('questions/<str:title>/', FormQuestion.as_view(), name='questions' ),
    path('personal-details/', PersonalDetailsViews.as_view(), name="personal-details"),
    path('document/', DocumentViews.as_view(), name="document"),
    path('document/<int:pk>', DocumentViews.as_view(), name="document"),
]
