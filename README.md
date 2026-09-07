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
