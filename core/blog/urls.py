from django.urls import path
from django.views.generic import TemplateView
from . import views
urlpatterns = [
    path("fbv_index" , views.indexView,name='fbv_index'),
    # path("cbv_index", TemplateView.as_view(template_name="index.html",)),
    path("cbv_index" , views.HomePageView.as_view(),name='cbv_index'),
]