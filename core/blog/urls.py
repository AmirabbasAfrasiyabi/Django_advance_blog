from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

app_name = "blog"

urlpatterns = [
    # path("fbv_index" , views.indexView,name='fbv_index'),
    # path("cbv_index", TemplateView.as_view(template_name="index.html",)),
    # path("cbv_index" , views.HomePageView.as_view(),name='cbv_index'),
    # path("post/", views.PostList.as_view(), name="Post-list"),
    # # path("go-to-LinkedIn/" , views.RedirectToLinkedIn.as_view(),name='redirect to LinkedIn Page'),
    # path("post/<int:pk>", views.PostDetailView.as_view(),name='post_detail'),
    # path("post/create/", views.PostCreateView.as_view(),name='post_create'),
    # path("post/<int:pk>/edit", views.PostEditView.as_view(),name = 'post_edit'),
    # path("post/<int:pk>/delete", views.PostDeleteView.as_view(),name = 'post_delete'),
    path("post/", views.APIPostList, name="api-Post-list"),
]