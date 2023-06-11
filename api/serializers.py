from rest_framework import serializers
from .models import Public,Name

class PublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Public
        fields=("name","picture")


class NameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Name
        fields = ('__all__')