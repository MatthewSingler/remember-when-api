from rest_framework import viewsets
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
from rememberwhenapi.models import Year, Comment, Fact, Category
from django.contrib.auth.models import User

class YearView(ViewSet):
    def list(self, request):
        years = Year.object.all()
        fact = self.request.query_params.get('fact', None)
        
