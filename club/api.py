from . import models
from . import serializers
from rest_framework import viewsets, permissions


class EventViewSet(viewsets.ModelViewSet):
    """ViewSet for the Event class"""

    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer
    permission_classes = [permissions.IsAuthenticated]


class CheckInViewSet(viewsets.ModelViewSet):
    """ViewSet for the CheckIn class"""

    queryset = models.CheckIn.objects.all()
    serializer_class = serializers.CheckInSerializer
    permission_classes = [permissions.IsAuthenticated]


class UrlViewSet(viewsets.ModelViewSet):
    """ViewSet for the Url class"""

    queryset = models.Url.objects.all()
    serializer_class = serializers.UrlSerializer
    permission_classes = [permissions.IsAuthenticated]


class FileViewSet(viewsets.ModelViewSet):
    """ViewSet for the File class"""

    queryset = models.File.objects.all()
    serializer_class = serializers.FileSerializer
    permission_classes = [permissions.IsAuthenticated]


class AlbumViewSet(viewsets.ModelViewSet):
    """ViewSet for the Album class"""

    queryset = models.Album.objects.all()
    serializer_class = serializers.AlbumSerializer
    permission_classes = [permissions.IsAuthenticated]


class AlbumImageViewSet(viewsets.ModelViewSet):
    """ViewSet for the AlbumImage class"""

    queryset = models.AlbumImage.objects.all()
    serializer_class = serializers.AlbumImageSerializer
    permission_classes = [permissions.IsAuthenticated]


class PollViewSet(viewsets.ModelViewSet):
    """ViewSet for the Poll class"""

    queryset = models.Poll.objects.all()
    serializer_class = serializers.PollSerializer
    permission_classes = [permissions.IsAuthenticated]


class ChoiceViewSet(viewsets.ModelViewSet):
    """ViewSet for the Choice class"""

    queryset = models.Choice.objects.all()
    serializer_class = serializers.ChoiceSerializer
    permission_classes = [permissions.IsAuthenticated]


class PostViewSet(viewsets.ModelViewSet):
    """ViewSet for the Post class"""

    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticated]


