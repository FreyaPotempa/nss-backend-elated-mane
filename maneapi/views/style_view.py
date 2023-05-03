"""View module for handling requests about styles"""
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from django.contrib.auth.models import User
from maneapi.models import Style


class StyleView(ViewSet):
    """Viewset for styles"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for single game

        Returns:
            Response -- JSON serialized game instance
        """
        style = Style.objects.get(pk=pk)
        serialized = StyleSerializer(style)
        return Response(serialized.data)

    def list(self, request):
        """Handle GET requests to styles resource

        Returns:
            Response -- JSON serialized list of styles
        """
        styles = Style.objects.all()
        serialized = StyleSerializer(styles, many=True)
        return Response(serialized.data)


class StyleSerializer(serializers.ModelSerializer):
    """JSON serializer for style creator"""

    class Meta:
        """JSON serializer for style creator"""
        model = Style
        fields = ('id', 'label', 'clients')
