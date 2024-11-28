from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm

def create_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm()
    return render(request, 'addMovie.html', {'form': form, 'action': 'add'})

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movieList.html', {'movies': movies})

def update_movie(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm(instance=movie)
    return render(request, 'addMovie.html', {'form': form, 'movie': movie, 'action': 'update'})

def delete_movie(request, pk):
    try:
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        return redirect('movie_list')
    except Movie.DoesNotExist:
        return redirect('movie_list')