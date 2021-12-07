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
from rememberwhenapi.models import Member, Comment, FactCategory
from django.contrib.auth.models import User

class FactView(ViewSet)

    def create(self, request):
        """Handle POST operations
        Returns:
            Response -- JSON serialized fact instance
        """
        user = User.objects.get(user=request.auth.user)
        category = FactCategory.objects.get(pk=request.data["category"])
        
        try:
            comment = Comment.objects.create(
                
            )
