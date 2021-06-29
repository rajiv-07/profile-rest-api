from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


from profiles_api import models
from profiles_api import serializers
from profiles_api import permissions



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



class HelloViewSet(viewsets.ViewSet):
    """test API viewset"""
    serializer_class = serializers.HelloSerializer


    def list(self, request):
        """Return a Hello Message"""
        a_viewset = [
        'uses actions (list, create, update, partial_update)',
        'automatically maps  to urls using routers',
        'provides more functionality with less code',
        ]
        return Response ({'message':'Hello' , 'a_viewset':a_viewset})

    def create(self,request):
        """create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message = f'HELLO {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrive (self, request,pk=None):
        """Handle getting an objects by its ID"""
        return Response({'http_method':'GET'})


    def update (self,request,pk=None):
        """Handle updating  an object"""
        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        """Handle updating a part of an object"""
        return Response({'http_method':'PATCH'})

    def destroy (self,request,pk=None):
        """Handle Removing an object"""
        return Response({'http_method':'DeLETE'})




class UserProfileViewSet(viewsets.ModelViewSet):
    """handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpadateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    """Handle and create user Authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
