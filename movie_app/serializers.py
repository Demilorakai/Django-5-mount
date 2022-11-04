from rest_framework import serializers
from .models import Director, Movie, Review


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id name'.split()


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'id title description duration director '.split()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text stars stars_str'.split()


class MoviSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)
    filter_reviews = ReviewSerializer(many=True)
    category = DirectorSerializer()
    category_name_copy = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = 'id title reviews filter_reviews rating category category_name category_name_copy'.split()

    def get_category_name_copy(self, movie):
        try:
           return movie.category.name
        except:
            return ''