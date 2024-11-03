from django.urls import path
from django.views.generic import TemplateView
from .views import indexView
urlpatterns = [
    path("fbv_index" , indexView,name='fbv_index'),
    path("cbv_index", TemplateView.as_view(template_name="index.html",)),
]