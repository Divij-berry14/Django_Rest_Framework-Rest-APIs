from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import *
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import login as django_login, logout as django_logout
from rest_framework.authentication import TokenAuthentication

class SnippetList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self,request):
        snippet=Snippet.objects.all()
        serializer=SnippetSerializer(snippet,many=True)
        # token=request.META['HTTP_AUTHORIZATION']
        print(request.COOKIES)
        # token1 = request.COOKIES['token']
        data={
            "data": serializer.data,
            # "token": token,
            "userId":request.user.id,
            "user":request.user.username,
            "password":request.user.password
            # "token1": token1
        }
        response=Response(data=data,status=status.HTTP_200_OK)
        print(type(response))
        # response.set_cookie("token",token)
        return response
    def post(self,request):
        print(request.data)
        serializer=SnippetSerializer(data=request.data)
        # token = request.META['HTTP_AUTHORIZATION']
        # token1 = request.COOKIES['token']
        if 'HTTP_REQUESTFROM' in request.META:
            print("cookie")
            token = request.COOKIES['token']
        # print(request.COOKIES)
        # token = request.COOKIES['token']
        else:
            print("header")
            token = request.META['HTTP_AUTHORIZATION']
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()
            print(serializer.data)
            data = {
                "data": serializer.data,
                "token": token,
                # "token1":token1
            }
            return Response(data=data, status=status.HTTP_200_OK)
        return Response(serializer.error_messages,status=status.HTTP_400_BAD_REQUEST)

# class SnippetList(generics.RetrieveAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)


class SnippetDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class LoginView(APIView):
    def post(self,request):
        serializer=LoginViewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.validated_data['user']
        print(user)
        django_login(request,user)   # default session logout in django
        token,created=Token.objects.get_or_create(user=user)
        data={
            "name":user.pk,
            "token":token.key
        }
        return Response(data=data,status=status.HTTP_200_OK)

class LogoutView(APIView):
    authentication_classes = (TokenAuthentication,)
    def post(self,request):
        django_logout(request)   # default session logout in django
        return Response(status=status.HTTP_204_NO_CONTENT)

def res(request):
    return HttpResponse("Welcome user")
