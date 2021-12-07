from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rememberwhenapi.models import Member, Comment
from rest_framework import serializers
from django.contrib.auth.models import User

@api_view(['GET'])
def member_profile(request):
    """Handle GET requests to profile resource
    Returns:
        Response -- JSON representation of user info and comments
    """
    member = Member.objects.get(user=request.auth.user)
    author = Comment.userId.get(user=request.auth.user)
