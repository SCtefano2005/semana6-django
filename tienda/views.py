from django.shortcuts import get_object_or_404, render
from .models import Producto, Categoria

def index(request):
    lista_productos = Producto.objects.order_by('nombre')[:20]
    categorias = list(Categoria.objects.all())  
    context = {'lista_productos': lista_productos, 'categorias': categorias}
    return render(request, 'index.html', context)

def producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    categorias = list(Categoria.objects.all())
    return render(request, 'producto.html', {'producto': producto, 'categorias': categorias})

def productos_por_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    productos = Producto.objects.filter(categoria=categoria)
    categorias = list(Categoria.objects.all()) 
    context = {
        'productos': productos,
        'categoria': categoria,
        'categorias': categorias 
    }
    return render(request, 'productos_por_categoria.html', context)
