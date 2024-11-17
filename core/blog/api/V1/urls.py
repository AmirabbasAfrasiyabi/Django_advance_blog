from django.urls import path , include
from . import views
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

app_name = "api_V1"

urlpatterns = [
    path("post/", views.PostList ,name="Post-list"), 
]