from rest_framework import serializers
from models import Snippet, Error


class SnippetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Snippet
        fields = ('pk', 'username')


class ErrorSerializer(serializers.ModelSerializer):

    class Meta:
        model=Error
        fields=('pk','error')
