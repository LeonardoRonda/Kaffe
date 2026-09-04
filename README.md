# ☕ Kaffe

Proyecto base de Django construido bajo el patrón **MVT** (Model – View – Template).

## Problemática real

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

## Rutas de la aplicación

| Ruta        | Vista                  | Descripción                                      |
|-------------|-------------------------|--------------------------------------------------|
| `/`         | `lista_productos`       | Listado de productos del menú.                   |
| `/crear/`   | `crear_producto`        | Formulario para registrar un nuevo producto.     |

## Flujo MVT de la aplicación

1. **Request** → el usuario navega a `GET /` o `POST /crear/`.
2. **URL** → `kaffe/urls.py` enruta a la vista correspondiente de `core.views`.
3. **View** → la vista procesa la petición (lee o agrega datos).
4. **Model** → en este proyecto, el "modelo" es la lista estática `PRODUCTOS` de
   `core/models.py` (sin base de datos).
5. **Template** → la vista renderiza un template que hereda de `base.html`.
6. **Response** → se devuelve el HTML al navegador.

> **Nota sobre datos en memoria:** al no usar base de datos, los productos
> agregados se guardan en la lista `PRODUCTOS` en memoria y **se pierden al
> reiniciar el servidor**. Este comportamiento es esperado en este laboratorio.

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