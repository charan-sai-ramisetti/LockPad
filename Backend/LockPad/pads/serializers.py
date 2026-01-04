from rest_framework import serializers

class OpenPadSerializer(serializers.Serializer):
    key = serializers.CharField(min_length=4, max_length=128)


class SavePadSerializer(serializers.Serializer):
    key = serializers.CharField(min_length=4, max_length=128)
    content = serializers.CharField(allow_blank=True)
