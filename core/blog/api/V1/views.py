from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer
from blog.models import Post

data={
    'id':1,
    'title':"hello"
}

@api_view()
def PostList(request):
    return Response('OK')

@api_view()
def PostDetail(request,id):
    post = Post.objects.get(pk=id)
    Serializer = PostSerializer(post)
    print(Serializer.data)
    return Response(Serializer.data)