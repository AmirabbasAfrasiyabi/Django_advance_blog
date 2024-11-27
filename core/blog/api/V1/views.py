from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAdminUser,IsAuthenticated
from rest_framework.response import Response
from .serializers import PostSerializer
from blog.models import Post
from rest_framework import status
from django.shortcuts import get_object_or_404



@api_view(["POST","GET"])
@permission_classes([IsAuthenticated])
def PostList(request):
    if request.method =="GET":
        posts = Post.objects.filter(status=True)
        Serializer = PostSerializer(posts,many=True)
        return Response(Serializer.data)
    elif request.method =="POST":
        Serializer = PostSerializer(data = request.data)
        Serializer.is_valid(raise_exception=True)
        Serializer.save()
        return Response (Serializer.data)
    

@api_view(["PUT","GET","DELETE"])
@permission_classes([IsAuthenticatedOrReadOnly])
def PostDetail(request,id):
    post = get_object_or_404(Post,pk=id,status=True)
    if request.method =="GET":
        Serializer = PostSerializer(post)
        return Response(Serializer.data)
    elif request.method =="PUT":
        Serializer = PostSerializer(post,data=request.data)
        Serializer.is_valid(raise_exception=True)
        Serializer.save()
        return Response (Serializer.data)

    elif request.method =="DELETE":
        post.delete()
        return Response({"detail":"Item removed successfully"},status=status.HTTP_204_NO_CONTENT)