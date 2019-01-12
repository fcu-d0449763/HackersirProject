from . import models

from rest_framework import serializers


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Event
        fields = (
            'pk', 
            'name', 
            'token', 
            'created', 
            'last_updated', 
            'date', 
            'checkcode', 
        )


class CheckInSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CheckIn
        fields = (
            'pk', 
            'token', 
            'created', 
            'last_updated', 
            'nid', 
        )


class UrlSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Url
        fields = (
            'token', 
            'name', 
            'created', 
            'last_updated', 
            'link', 
        )


class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.File
        fields = (
            'token', 
            'name', 
            'created', 
            'last_updated', 
            'file', 
        )


class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Album
        fields = (
            'token', 
            'name', 
            'created', 
            'last_updated', 
        )


class AlbumImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.AlbumImage
        fields = (
            'token', 
            'created', 
            'last_updated', 
            'img', 
        )


class PollSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Poll
        fields = (
            'token', 
            'name', 
            'created', 
            'last_updated', 
            'context', 
            's_date', 
            'e_date', 
        )


class ChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Choice
        fields = (
            'token', 
            'name', 
            'created', 
            'last_updated', 
            'context', 
            'votes', 
        )


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Post
        fields = (
            'token', 
            'name', 
            'created', 
            'last_updated', 
            'context', 
        )


