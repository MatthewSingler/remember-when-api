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
        # For models with related fields you want to use select_related and prefetch_related to minimize database queries. 
        # I would spend *a lot* of time reading about, trying to understand, testing using these two methods as they are HUGE 
        # difference between beginner and intermediate and something that's pretty pass/fail for us when hiring product engineer. 
        comments = Comment.objects.all()
        fact = self.request.query_params.get('facts', None)
        if fact is not None:
            comments = comments.filter(fact__id=fact)
        serializer = CommentSerializer(
            comments, many=True, context={'request': request})
        return Response(serializer.data)
    
    def destroy(self, request, pk=None):
        try:
            comment = Comment.objects.get(pk=pk)
            comment.delete()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except Fact.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')
class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    class Meta:
        model = Comment
        fields = ('user', 'contents', 'fact', 'id')
        depth = 1
