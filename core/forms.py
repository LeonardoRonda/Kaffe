from django import forms

CATEGORIAS = [
    ("bebida", "Bebida"),
    ("postre", "Postre"),
    ("extra", "Extra"),
]

class ProductoForm(forms.Form):
    nombre = forms.CharField(
        max_length=100,
        label="Nombre",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Ej: Café Americano"})
    )
    categoria = forms.ChoiceField(
        choices=CATEGORIAS,
        label="Categoría",
        widget=forms.Select(attrs={"class": "form-control"})
    )
    precio = forms.DecimalField(
        max_digits=6,
        decimal_places=2,
        min_value=0.01,
        label="Precio (S/)",
        widget=forms.NumberInput(attrs={"class": "form-control", "step": "0.01", "placeholder": "Ej: 12.00"})
    )
    descripcion = forms.CharField(
        required=False,
        label="Descripción",
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 3, "placeholder": "Información adicional (opcional)"})
    )
    disponible = forms.BooleanField(
        required=False,
        initial=True,
        label="Disponible",
        widget=forms.CheckboxInput(attrs={"class": "checkbox-input"})
    )