from rest_framework import serializers

class StorySerializer(serializers.Serializer):
    Titulo = serializers.CharField(max_length=200)
    ID = serializers.IntegerField()
