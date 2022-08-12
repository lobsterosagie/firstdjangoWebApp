from django.urls import path
from . import views

app_name = "studentapiapplication"

urlpatterns = [
    path('v1/', views.student_list, name="myapifunction")
]


