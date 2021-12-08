from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Movie, Genre
from .serializers import MovieListSerializer, MovieSerializer, GenreListSerializer, GenreSerializer
from django.contrib.auth import get_user_model


@api_view(['GET'])
def movies(request):
    movie_list = get_list_or_404(Movie)
    serializer = MovieListSerializer(movie_list, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


# 음... 좋아요 기능
@api_view(['POST'])
def movie_like(request, my_pk, movie_title):
  movie = get_object_or_404(Movie, title=movie_title)
  me = get_object_or_404(get_user_model(), pk=my_pk)

  if me.like_movies.filter(pk=movie.pk).exists():
      me.like_movies.remove(movie.pk)
      liking = False
  else:
      me.like_movies.add(movie.pk)
      liking = True
  
  return Response(liking)


# 음... 싫어요 기능
@api_view(['POST'])
def movie_dislike(request, my_pk, movie_title):
  movie = get_object_or_404(Movie, title=movie_title)
  me = get_object_or_404(get_user_model(), pk=my_pk)

  if me.dislike_movies.filter(pk=movie.pk).exists():
      me.dislike_movies.remove(movie.pk)
      disliking = False
 
  else:
      me.dislike_movies.add(movie.pk)
      disliking = True
  
  return Response(disliking) 


# 나의 좋아요 목록
@api_view(['GET'])
def my_movie_like(request, my_pk):
    me = get_object_or_404(get_user_model(), pk=my_pk)
    data = []
    movies = request.data

    for movie_pk in movies:
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = MovieSerializer(movie)
        data.append(serializer.data)
    
    return Response(data)


# 나의 싫어요 목록
@api_view(['GET'])
def my_movie_dislike(request, my_pk):
    me = get_object_or_404(get_user_model(), pk=my_pk)
    data = []
    movies = request.data

    for movie_pk in movies:
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = MovieSerializer(movie)
        data.append(serializer.data)
    
    return Response(data)