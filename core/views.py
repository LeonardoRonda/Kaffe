from django.shortcuts import redirect, render
from .models import PRODUCTOS, agregar_producto
from .forms import ProductoForm

def lista_productos(request):
    return render(request, "core/lista_productos.html", {"productos": PRODUCTOS})

def crear_producto(request):
    """Muestra el formulario (GET), valida y agrega el producto en memoria (POST)
    y redirige al listado para confirmar que el nuevo dato aparece."""
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            agregar_producto(
                nombre=datos["nombre"],
                categoria=datos["categoria"],
                precio=datos["precio"],
                descripcion=datos["descripcion"],
                disponible=datos["disponible"],
            )
            return redirect("lista_productos")
    else:
        form = ProductoForm()

    return render(request, "core/formulario_producto.html", {"form": form})