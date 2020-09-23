from rest_framework import serializers
from website.models import Website

class Bookserializer(serializers.ModelSerializer):
    class Meta:
        model=Website
        fields=('title','subtitle','author','isbn')