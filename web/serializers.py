from rest_framework import serializers
from web.models import *

class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=800)
    slug = serializers.CharField(max_length=800)

    class Meta:
        model = Category

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=800)
    slug = serializers.CharField(max_length=800)
    url = serializers.CharField(max_length=800)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Movie

class MovieDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    description = serializers.CharField(max_length=800)
    rating = serializers.DecimalField(decimal_places=2, max_digits=8)
    year = serializers.IntegerField()
    age = serializers.IntegerField()
    duration = serializers.CharField(max_length=800)
    movie = MovieSerializer(read_only=True)

    class Meta:
        model = MovieDetail

class BlockSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=800)
    order = serializers.IntegerField()
    movies = MovieSerializer(read_only=True, many=True)

    class Meta:
        model = Block