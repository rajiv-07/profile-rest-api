from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from profiles_api import serializers



class HelloApiView(APIView):
    """docstring for HelloApiView using for test"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """returns list APIView features"""
        an_apiview = [
            'Uses HTTP methods as function(get, post, patch, put,delete)',
            'Is similar to tarditional Django View',
            'Gives you control over your application logic',
            'IS mapped Manually URLs',
        ]
        return Response({'message': 'hello!', 'an_apiview': an_apiview})


    def post(self, request):
        """create a hello request with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message': message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating of an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle partial update of object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})
