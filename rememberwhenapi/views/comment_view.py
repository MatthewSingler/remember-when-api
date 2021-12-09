from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework import serializers
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.decorators import action
import datetime
from rememberwhenapi import models
from rememberwhenapi.models import Member, Comment, Fact, Category
from django.contrib.auth.models import User

from rememberwhenapi.views.fact_view import UserSerializer

class CommentView(ViewSet):
    def create(self, request):
        user = User.objects.get(pk=request.auth.user.id)
        fact = Fact.objects.get(pk=request.data['fact'])

        try:
            comment = Comment.objects.create(
                user = user,
                fact = fact,
                contents = request.data['contents']
            )
            serializer = CommentSerializer(comment, context={'request': request})
            return Response(serializer.data, status=201)
        except ValidationError as ex:
            return Response({'reason': ex.message}, status=status.HTTP_400_BAD_REQUEST)
        
    def list(self, request):
        comments = Comment.objects.all()
        fact = self.request.query_params.get('fact', None)
        if fact is not None:
            comments = comments.filter(fact__id=fact)
        serializer = CommentSerializer(
            comments, many=True, context={'request': request})
        return Response(serializer.data)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')
class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    class Meta:
        model = Comment
        fields = ('user', 'contents', 'fact')
        depth = 1
