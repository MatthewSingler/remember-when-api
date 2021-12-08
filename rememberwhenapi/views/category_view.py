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
from rememberwhenapi.models import Member, Comment, FactCategory, Fact, Category, Year
from django.contrib.auth.models import User

class CategoryView(ViewSet):

    def list(self, request):
        """Get a list of categories
        """
        categories = Category.objects.all()
        category = self.request.query_params.get('category', None)
        if category is not None:
            categories = categories.filter(fact_category__id=category)
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class CategorySerializer(serializers.ModelSerializer):
    """JSON serializer for categories
    Arguments:
        serializer type
    """
    class Meta:
        model = Category
        fields = ('id', 'type')
        depth = 1
