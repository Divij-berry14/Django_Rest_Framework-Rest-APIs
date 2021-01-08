from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth import authenticate
from rest_framework import exceptions
from django.contrib.auth.models import User

class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance

# class SnippetSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Snippet
#         fields = ['id', 'title', 'code', 'linenos', 'language', 'style']


# class LoginViewSerializer(serializers.Serializer):
#     username=serializers.CharField()
#     password=serializers.CharField()
#
#     def validate(self,data):
#         username=data.get("username")
#         password=data.get("password")
#         if username and password:
#             user=authenticate(username=username,password=password)
#             if user:
#                 if user.is_active:
#                     data['user']=user
#                 else:
#                     msg="user is deactivated"
#                     exceptions.ValidationError(msg)
#             else:
#                 msg="Unable to login"
#                 raise exceptions.ValidationError(msg)
#         else:
#             msg="provide credentials"
#             raise exceptions.ValidationError(msg)
#         return data
#
