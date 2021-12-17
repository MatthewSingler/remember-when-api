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

class FactView(ViewSet):

    def create(self, request):
        """Handle POST operations
        Returns:
            Response -- JSON serialized fact instance
        """
        user = User.objects.get(pk=request.auth.user.id)
        category = Category.objects.get(pk=request.data["category"])
        year = Year.objects.get(year_number=request.data['year'])
        try:
            fact = Fact.objects.create(
                user = user,
                year = year,
                contents = request.data['contents'],
                is_approved= True
            )
            fact.category.add(category)
            serializer = FactSerializer(fact, context={'request': request})
            return Response(serializer.data, status=201)
        except ValidationError as ex:
            return Response({'reason': ex.message}, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        """Handle GET requests for single fact
        Returns:
            Response -- JSON serialized fact instance
        """
        try:
            fact = Fact.objects.get(pk=pk)
            serializer = FactSerializer(fact, context={'request': request})
            return Response(serializer.data)
        except Fact.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return HttpResponseServerError(ex)
        
    def update(self, request, pk=None):
        """Handle PUT requests for a fact
        Returns:
            Response -- Empty body with 204 status code
        """
        fact = Fact.objects.get(pk=pk)
        year_number = Year.objects.get(request.data['year'])
        fact.year_number = year_number
        fact.contents = request.data['contents']
        category = FactCategory.objects.get(pk=request.data["factCategoryId"])
        fact.category = category
        fact.save()
        return Response({}, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single fact
        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            fact = Fact.objects.get(pk=pk)
            fact.delete()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except Fact.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def list(self, request):
        """Handle GET requests to facts resource
        Returns:
            Response -- JSON serialized list of facts
        """
        facts = Fact.objects.order_by('year__year_number')
        year = self.request.query_params.get('year', None)
        category = self.request.query_params.get('category', None)
        if category is not None:
            facts = facts.filter(fact_category__id=category)
        if year is not None:
            facts = facts.filter(year__year_number=year)
            
        serializer = FactSerializer(
            facts, many=True, context={'request': request})
        return Response(serializer.data)
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')
        
class FactSerializer(serializers.ModelSerializer):
    """JSON serializer for facts
    Arguments:
        serializer type
    """
    user = UserSerializer(many = False)
    class Meta:
        model = Fact
        fields = ('id', 'category', 'contents', 'year', 'is_approved', 'user')
        depth = 1
