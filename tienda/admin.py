from django.contrib import admin
from .models import Categoria, Producto
from django.utils.html import format_html


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio', 'stock', 'mostrar_imagen', 'pub_date')  
    search_fields = ('nombre', 'categoria__nombre')
    list_filter = ('categoria', 'pub_date')
    list_editable = ('precio', 'stock')
    ordering = ('nombre',)

    def mostrar_imagen(self, obj):
        if obj.imagen:
            return format_html('<img src="{}" width="50" height="50" />', obj.imagen.url)
        return "Sin imagen"
    
    mostrar_imagen.short_description = 'Vista previa'
    
admin.site.register(Categoria)
admin.site.register(Producto, ProductoAdmin)