from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAdminUser,IsAuthenticated
from rest_framework.response import Response
from .serializers import PostSerializer
from blog.models import Post
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import authentication, permissions


# @api_view(["POST","GET"])
# @permission_classes([IsAuthenticated])
# def PostList(request):
#     if request.method =="GET":
#         posts = Post.objects.filter(status=True)
#         Serializer = PostSerializer(posts,many=True)
#         return Response(Serializer.data)
#     elif request.method =="POST":
#         Serializer = PostSerializer(data = request.data)
#         Serializer.is_valid(raise_exception=True)
#         Serializer.save()
#         return Response (Serializer.data)

    
class PostList(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    """getting a list of post and creating a new post"""
    def get(self, request):

        """
        Return a list of all users.
        """
        posts = Post.objects.filter(status=True)
        Serializer = PostSerializer(posts,many=True)
        return Response(Serializer.data)
    

    """retrieving a list of post"""
    def post(self, request):

        """
        created a post with provided.
        """

        Serializer = PostSerializer(data = request.data)
        Serializer.is_valid(raise_exception=True)
        Serializer.save()
        return Response (Serializer.data)
    
    
        
# @api_view(["PUT","GET","DELETE"])
# @permission_classes([IsAuthenticatedOrReadOnly])
# def PostDetail(request,id):
#     post = get_object_or_404(Post,pk=id,status=True)
#     if request.method =="GET":
#         Serializer = PostSerializer(post)
#         return Response(Serializer.data)
#     elif request.method =="PUT":
#         Serializer = PostSerializer(post,data=request.data)
#         Serializer.is_valid(raise_exception=True)
#         Serializer.save()
#         return Response (Serializer.data)

#     elif request.method =="DELETE":
#         post.delete()
#         return Response({"detail":"Item removed successfully"},status=status.HTTP_204_NO_CONTENT)
    

class PostDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    """retrieving the post data"""
    def get(self, request,id):
        post = get_object_or_404(Post,pk=id,status=True)
        Serializer = PostSerializer(post)
        return Response(Serializer.data)
    
    """editing the post data"""
    def put(self, request,id):
        post = get_object_or_404(Post,pk=id,status=True)
        Serializer = PostSerializer(post,data=request.data)
        Serializer.is_valid(raise_exception=True)
        Serializer.save()
        return Response (Serializer.data)
    
    """delete the post"""
    def delete(self, request,id):
        post = get_object_or_404(Post,pk=id,status=True)
        post.delete()
        return Response({"detail":"Item removed successfully"},status=status.HTTP_204_NO_CONTENT)