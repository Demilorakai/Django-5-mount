from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
def test_view(request):
    dict_ = {
        'int': 1000,
        'float': 999.99,
        'bool': True,
        'text': 'Hello World',
        'dict': {
            'int': 1000
        },
        'list': [1, 2, 3]
    }
    return Response(data=dict_)


@api_view(['GET', 'POST'])
def director_view(request):
    if request.method == "GET":
        director = Director.objects.all()
        serializer = DirectorSerializer(director, many=True).data
        return Response(data=serializer)
    elif request.method == "POST":
        serializers = DirectorValidateSerializers(data=request.data)
        if not serializers.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
                            data={'errors': serializers.errors})
        name = request.data.get('name')
        Director.objects.create(
            name=name
        )
        return Response()


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def movie_view(request):
    if request.method == "GET":
        movie = Movie.objects.all()
        serializer = MovieSerializer(movie, many=True).data
        return Response(data=serializer)
    elif request.method == "POST":
        serializers = MovieValidateSerializers(data=request.data)
        if not serializers.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
                            data={'errors': serializers.errors})
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director_id = request.data.get('director_id')
        Movie.objects.create(
            title=title,
            description=description,
            duration=duration,
            director_id=director_id
        )
        return Response()


@api_view(['GET', 'POST'])
def review_view(request):
    if request.method == "GET":
        review = Review.objects.all()
        serializer = ReviewSerializer(review, many=True).data
        return Response(data=serializer)
    elif request.method == "POST":
        serializers = ReviewsValidateSerializers(data=request.data)
        if not serializers.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
                            data={'errors': serializers.errors})
        text = request.data.get('text')
        stars = request.data.get('stars')
        movie_id = request.data.get('movie_id')
        Review.objects.create(
            text=text,
            stars=stars,
            movie_id=movie_id,
        )
        return Response()


@api_view(["GET", "PUT", "DELETE"])
def director_item(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        data = DirectorSerializer(director).data
        return Response(data=data)
    elif request.method == "DELETE":
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PUT":
        serializers = DirectorValidateSerializers(data=request.data)
        if not serializers.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
                            data={'errors': serializers.errors})
        name = request.data.get('name')
        director.name = name
        director.save()
        return Response(data=DirectorSerializer(director).data)


@api_view(["GET", "PUT", "DELETE"])
def movie_item(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        data = MovieSerializer(movie).data
        return Response(data=data)
    elif request.method == "DELETE":
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PUT":
        serializers = DirectorValidateSerializers(data=request.data)
        if not serializers.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
                            data={'errors': serializers.errors})
        movie.title = request.data.get('title')
        movie.description = request.data.get('description')
        movie.duration = request.data.get('duration')
        movie.director_id = request.data.get('director_id')
        movie.save()

        return Response(data=MovieSerializer(movie).data)


@api_view(["GET", "PUT", "DELETE"])
def review_item(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        data = ReviewSerializer(review).data
        return Response(data=data)
    elif request.method == "DELETE":
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PUT":
        serializers = ReviewsValidateSerializers(data=request.data)
        if not serializers.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
                            data={'errors': serializers.errors})
        text = request.data.get('text')
        stars = request.data.get('stars')
        movie_id = request.data.get('movie_id')
        text.save()
        stars.save()
        movie_id.save()
        return Response(data=ReviewSerializer(review).data)


