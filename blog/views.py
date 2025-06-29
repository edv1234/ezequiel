from django.shortcuts import render

def inicio(request):
    return render(request, "blog/inicio.html")

from .forms import AutorForm

def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "blog/autor_creado.html")
    else:
        form = AutorForm()
    return render(request, "blog/crear_autor.html", {'form': form})

from .forms import CategoriaForm
from django.shortcuts import render

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'blog/categoria_creada.html')
    else:
        form = CategoriaForm()
    return render(request, 'blog/crear_categoria.html', {'form': form})


from .forms import PostForm

def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'blog/post_creado.html')
    else:
        form = PostForm()
    return render(request, 'blog/crear_post.html', {'form': form})

from .models import Post

def buscar_post(request):
    consulta = request.GET.get('q')
    resultados = []

    if consulta:
        resultados = Post.objects.filter(titulo__icontains=consulta)

    return render(request, 'blog/buscar_post.html', {'resultados': resultados, 'consulta': consulta})