from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer
from blog.models import Post
from rest_framework import status
from django.shortcuts import get_object_or_404



@api_view(["POST","GET"])
def PostList(request):
    if request.method =="GET":
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data)
    elif request.method =="POST":
        Serializer = PostSerializer(data = request.data)
        Serializer.is_valid(raise_exception=True)
        Serializer.save()
        return Response (Serializer.data)

@api_view()
def PostDetail(request,id):
    post = get_object_or_404(Post,pk=id,status=True)
    Serializer = PostSerializer(post)
    return Response(Serializer.data)