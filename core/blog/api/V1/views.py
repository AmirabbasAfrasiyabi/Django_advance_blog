from rest_framework.decorators import api_view
from rest_framework.response import Response

data={
    'id':1,
    'title':"hello"
}

@api_view()
def PostList(request):
    return Response('OK')

@api_view()
def PostDetail(request,id):
    return Response(data)