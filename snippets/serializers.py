from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth import authenticate
from rest_framework import exceptions
from django.contrib.auth.models import User

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']


class LoginViewSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()

    def validate(self,data):
        username=data.get("username")
        password=data.get("password")
        if username and password:
            user=authenticate(username=username,password=password)
            if user:
                data['user']=user
            else:
                msg="Unable to login"
                raise exceptions.ValidationError(msg)
        else:
            msg="provide credentials"
            raise exceptions.ValidationError(msg)
        return data

