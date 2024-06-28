
from django.urls import path
from .views import *
from .views import ResumeDataView  

urlpatterns = [
    path('resume_data/', ResumeDataView.as_view(), name='resume_data'),
]