from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()
def PostList(request):
    return Response('OK')