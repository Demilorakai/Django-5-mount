from rest_framework import serializers
from .models import *


class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()
    class Meta:
        model = Director
        fields = 'id name movies_count'.split()

    def get_movies_count(self, director):
        return director.movies.count()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text stars stars_str'.split()


class MovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)
    class Meta:
        model = Movie
        fields = 'id title description duration director_id reviews rating '.split()


class DirectorValidateSerializers(serializers.Serializer):
    name = serializers.CharField(min_length=5, max_length=100)


class MovieValidateSerializers(serializers.Serializer):
    title = serializers.CharField(min_length=5, max_length=100)
    description = serializers.CharField(min_length=5, max_length=150)
    duration = serializers.IntegerField(min_value=50, max_value=500)


class ReviewsValidateSerializers(serializers.Serializer):
    text = serializers.CharField(min_length=5, max_length=270)
    stars = serializers.IntegerField(min_value=1, max_value=5)
