# ☕ Kaffe

Proyecto base de Django construido bajo el patrón **MVT** (Model – View – Template).

## Problemática

La cafetería **Kaffe** maneja su menú de productos (bebidas, postres y extras)
de forma manual, registrando los datos en papel o en hojas de cálculo que se
desactualizan rápidamente. Esto genera errores de precios, información
duplicada y dificultad para saber qué productos están disponibles. El problema
lo atraviesan directamente los empleados del mostrador y el administrador del
local, quienes necesitan consultar y actualizar el menú constantemente.

La solución es una aplicación web sencilla en Django que permita registrar y
consultar los productos del menú de forma ordenada y en un solo lugar.

**Usuarios:** empleados y administradores de la cafetería Kaffe.

## Funcionalidades del sistema

1. **registrar un nuevo producto** del menú (nombre, categoría, precio,
   descripción y disponibilidad).
2. **visualizar el listado** de todos los productos registrados, mostrando la
   información principal de cada uno.
3. **identificar la categoría** de cada producto (bebida, postre, extra) para
   organizar mejor el menú.
4. **indicar el precio** de cada producto para tener un control de costos
   exacto.
5. **marcar la disponibilidad** de cada producto, de modo que se sepa si puede
   venderse o está agotado.
6. **validar los datos ingresados** en el formulario de creación antes de
   guardar el producto.

## Modelo de datos

**Entidad principal:** `Producto`

| Campo        | Tipo | Obligatorio | Justificación                                             |
|--------------|------|-------------|-----------------------------------------------------------|
| `nombre`     | str  | Sí          | Identifica el producto dentro del listado.                |
| `categoria`  | str  | Sí          | Permite agrupar los productos del menú.                   |
| `precio`     | float| Sí          | Control de costos y cobro al cliente.                     |
| `descripcion`| str  | No          | Información adicional opcional para el cliente.           |
| `disponible` | bool | Sí          | Indica si el producto puede venderse o está agotado.      |

## La App creada: `core`

Dentro del proyecto base se desarrolla la aplicación **`core`**, que concentra la
lógica de la cafetería (datos estáticos, vistas, formulario y templates). Está
registrada en `INSTALLED_APPS` de `kaffe/settings.py`:

```python
INSTALLED_APPS = [
    ...
    'core',
]
```

Estructura de la App:

```
core/
├── models.py    # Lista estática PRODUCTOS (5 registros) + agregar_producto()
├── views.py     # lista_productos y crear_producto
├── forms.py     # ProductoForm (forms.Form, sin ModelForm ni base de datos)
├── urls.py      # Rutas de la App (/ y /crear/)
├── admin.py
└── templates/
    ├── base.html
    └── core/
        ├── lista_productos.html
        └── formulario_producto.html
```

## Código de la App

### `core/models.py` — datos estáticos (sin base de datos)

```python
# Datos estáticos de productos (sin base de datos)
PRODUCTOS = [
    {
        "nombre": "Café Americano",
        "categoria": "bebida",
        "precio": 8.00,
        "descripcion": "Café negro clásico",
        "disponible": True
    },
    {
        "nombre": "Latte",
        "categoria": "bebida",
        "precio": 12.00,
        "descripcion": "Café con leche vaporizada",
        "disponible": True
    },
    {
        "nombre": "Croissant",
        "categoria": "postre",
        "precio": 9.00,
        "descripcion": "Croissant de mantequilla",
        "disponible": True
    },
    {
        "nombre": "Brownie",
        "categoria": "postre",
        "precio": 10.00,
        "descripcion": "Brownie de chocolate",
        "disponible": False
    },
    {
        "nombre": "Leche de almendra",
        "categoria": "extra",
        "precio": 4.00,
        "descripcion": "Alternativa vegetal",
        "disponible": True
    },
]


def agregar_producto(nombre, categoria, precio, descripcion="", disponible=True):
    """Agrega un nuevo producto a la lista en memoria.
    Al no haber base de datos, los datos se pierden al reiniciar el servidor."""
    PRODUCTOS.append({
        "nombre": nombre,
        "categoria": categoria,
        "precio": precio,
        "descripcion": descripcion,
        "disponible": disponible,
    })
    return PRODUCTOS[-1]
```

### `core/views.py` — listado y creación

```python
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
```

### `core/forms.py` — formulario (forms.Form)

```python
from django import forms

CATEGORIAS = [
    ("bebida", "Bebida"),
    ("postre", "Postre"),
    ("extra", "Extra"),
]

class ProductoForm(forms.Form):
    nombre = forms.CharField(max_length=100, label="Nombre")
    categoria = forms.ChoiceField(choices=CATEGORIAS, label="Categoría")
    precio = forms.DecimalField(
        max_digits=6, decimal_places=2, min_value=0.01, label="Precio (S/)"
    )
    descripcion = forms.CharField(required=False, label="Descripción")
    disponible = forms.BooleanField(required=False, initial=True, label="Disponible")
```

### `core/urls.py` — rutas de la App

```python
from django.urls import path

from . import views

urlpatterns = [
    path("", views.lista_productos, name="lista_productos"),
    path("crear/", views.crear_producto, name="crear_producto"),
]
```

### `core/templates/core/lista_productos.html` — listado

```html
{% extends "base.html" %}
{% block content %}
<h1>Menú de Productos</h1>
<p><a href="{% url 'crear_producto' %}" class="btn">+ Agregar producto</a></p>
<table>
    <thead>
        <tr><th>Nombre</th><th>Categoría</th><th>Precio</th><th>Descripción</th><th>Disponible</th></tr>
    </thead>
    <tbody>
        {% for producto in productos %}
        <tr>
            <td>{{ producto.nombre }}</td>
            <td>{{ producto.categoria|title }}</td>
            <td>S/ {{ producto.precio|floatformat:2 }}</td>
            <td>{{ producto.descripcion }}</td>
            <td>{% if producto.disponible %}Sí{% else %}No{% endif %}</td>
        </tr>
        {% endfor %}
    </tbody>
</table>
{% endblock %}
```

### `core/templates/core/formulario_producto.html` — formulario

```html
{% extends "base.html" %}
{% block content %}
<h1>Registrar nuevo producto</h1>
<form method="post">
    {% csrf_token %}
    {% for field in form %}
    <div class="form-group">
        <label for="{{ field.id_for_label }}">{{ field.label }}</label>
        {{ field }}
        {% for error in field.errors %}
            <ul class="errorlist"><li>{{ error }}</li></ul>
        {% endfor %}
    </div>
    {% endfor %}
    <button type="submit" class="btn">Guardar producto</button>
    <a href="{% url 'lista_productos' %}" class="btn-secondary">← Volver al menú</a>
</form>
{% endblock %}
```

## Rutas de la aplicación

| Ruta        | Vista                  | Descripción                                      |
|-------------|-------------------------|--------------------------------------------------|
| `/`         | `lista_productos`       | Listado de productos del menú.                   |
| `/crear/`   | `crear_producto`        | Formulario para registrar un nuevo producto.     |

## Flujo MVT de la aplicación

1. **Request** → el usuario navega a `GET /` o `POST /crear/`.
2. **URL** → `core/urls.py` (incluido desde `kaffe/urls.py`) enruta a la vista correspondiente de `core.views`.
3. **View** → la vista procesa la petición (lee o agrega datos).
4. **Model** → en este proyecto, el "modelo" es la lista estática `PRODUCTOS` de
   `core/models.py` (sin base de datos).
5. **Template** → la vista renderiza un template que hereda de `base.html`.
6. **Response** → se devuelve el HTML al navegador.

**Ejemplo concreto — alta del producto "Mocachino" (S/ 13.00):**

1. **Request** → `POST /crear/` con `nombre=Mocachino`, `categoria=bebida`, `precio=13.00`, `descripcion=...`, `disponible=True`.
2. **URL** → `core/urls.py` empareja `crear/` y llama a `crear_producto`.
3. **View** → `crear_producto` valida el `ProductoForm` y, al ser válido, llama `agregar_producto(...)`.
4. **Model** → `agregar_producto` agrega el diccionario a la lista `PRODUCTOS` (memoria, sin base de datos).
5. **Template** → la vista redirige (`redirect`) a `lista_productos`, que renderiza `lista_productos.html` heredando `base.html`.
6. **Response** → el navegador recibe el HTML con la tabla de **6 productos** (los 5 iniciales + Mocachino).

## Capturas del flujo

### 1. Listado de productos
Página principal que muestra todos los productos del menú registrados.

![Listado de productos](listado.png)

### 2. Formulario de registro
Formulario para agregar un producto nuevo con sus datos (nombre, categoría, precio, descripción y disponibilidad).

![Formulario de registro](formulario.png)

### 3. Producto registrado
El listado vuelve a mostrarse con el nuevo producto reflejado.

![Producto registrado](nuevo-producto.png)

## Casos de prueba

Casos ejecutados y verificados contra la aplicación corriendo (`python manage.py runserver`).

| # | Caso | Acción | Resultado esperado | Resultado |
|---|---|---|---|---|
| 1 | Crear producto válido | POST `/crear/` con datos correctos | Redirige al listado y muestra el producto | ✔ Aceptado |
| 2 | Nombre vacío | POST con `nombre=""` | Rechazado, muestra error en el campo | ✔ Aceptado |
| 3 | Precio negativo | POST con `precio=-5` | Rechazado (mínimo 0.01) | ✔ Aceptado |
| 4 | Precio no numérico | POST con `precio=abc` | Rechazado, error de valor | ✔ Aceptado |
| 5 | Categoría inválida | POST con `categoria=naranja` | Rechazado, opción no válida | ✔ Aceptado |
| 6 | Descripción vacía | POST sin descripción (opcional) | Aceptado y agregado al listado | ✔ Aceptado |

## Evidencia del laboratorio

### Integrante 1
- **Nombre:** Yamil Aaron Ochoa
- **Título:** App de menú para la cafetería Kaffe
- **Capturas:**
  - Listado de productos: `listado.png`
  - Formulario de creación: `formulario.png`
  - Nuevo producto reflejado: `nuevo-producto.png`
- **Código:** `core/models.py`, `core/views.py`, `core/forms.py`, `core/urls.py`, `core/templates/*`
- **Explicación:** la App `core` implementa el patrón MVT con datos estáticos en memoria; se conecta con el proyecto `kaffe` mediante el registro en `INSTALLED_APPS` y el `include('core.urls')` en `kaffe/urls.py`.
- **Casos de prueba:** ver tabla anterior (6 casos verificados).

### Integrante 2
- **Nombre:** Leonardo Favio Ronda
- **Título:** App de menú para la cafetería Kaffe
- **Capturas:**
  - Listado de productos: `listado.png`
  - Formulario de creación: `formulario.png`
  - Nuevo producto reflejado: `nuevo-producto.png`
- **Código:** `core/models.py`, `core/views.py`, `core/forms.py`, `core/urls.py`, `core/templates/*`
- **Explicación:** la App `core` implementa el patrón MVT con datos estáticos en memoria; se conecta con el proyecto `kaffe` mediante el registro en `INSTALLED_APPS` y el `include('core.urls')` en `kaffe/urls.py`.
- **Casos de prueba:** ver tabla anterior (6 casos verificados).
