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
