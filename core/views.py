from django.shortcuts import render
from .models import PRODUCTOS

def lista_productos(request):
    return render(request, "core/lista_productos.html", {"productos": PRODUCTOS})
