from rest_framework import serializers
from . import models


class AddNotesSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.NoteModel
        fields = ['title', 'notes']


class MyNotesSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.NoteModel
        fields = '__all__'

