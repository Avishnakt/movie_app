from django.shortcuts import render, redirect
from .models import Movies_table
from .forms import MovieForm


# Create your views here.

def moves(request):
    movies = Movies_table.objects.all()
    content = {
        'movie_list': movies
    }
    return render(request, 'index.html', content)


def details(request, movie_id):
    movie = Movies_table.objects.get(id=movie_id)
    return render(request, 'details.html', {'movie': movie})


def add_movie(request):
    if request.method == 'POST':
        name = request.POST.get('name', )
        desc = request.POST.get('desc', )
        img = request.FILES['img']
        movie = Movies_table(name=name, desc=desc, img=img, )
        movie.save()
        return redirect('/')
    return render(request, 'add.html')


def update(request, id):
    movie = Movies_table.objects.get(id=id)
    form = MovieForm(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'movie': movie, 'form': form})


def delete(request, id):
    if request.method == 'POST':
        movie = Movies_table.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request, 'delete.html')
