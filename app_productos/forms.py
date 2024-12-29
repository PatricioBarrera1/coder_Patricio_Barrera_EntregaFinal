from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image', 'is_available']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

    #en el futuro podemos agregar más validaciones (en views aparece una validación is.valid)