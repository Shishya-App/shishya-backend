from django.urls import path
from adminpanel.views import PersonalDetailsViews,DocumentViews


urlpatterns = [
    path('personal-details/', PersonalDetailsViews.as_view(), name="personal-details"),
    path('document/', DocumentViews.as_view(), name="document"),
    path('document/<int:pk>', DocumentViews.as_view(), name="document"),
]
