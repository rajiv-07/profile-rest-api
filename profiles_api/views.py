from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """docstring for HelloApiView using for test"""

    def get(self, request, format=None):
        """returns list APIView features"""
        an_apiview = [
            'Uses HTTP methods as function(get, post, patch, put,delete)',
            'Is similar to tarditional Django View',
            'Gives you control over your application logic',
            'IS mapped Manually URLs',
        ]
        return Response({'message': 'hello!', 'an_apiview': an_apiview})
