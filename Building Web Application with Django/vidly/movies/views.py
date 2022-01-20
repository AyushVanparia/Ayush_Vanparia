from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Movie


def index(request):
    # with this statement we get all movie object in our database
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'movies': movies})


def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})
