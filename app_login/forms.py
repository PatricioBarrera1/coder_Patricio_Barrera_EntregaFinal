#from django import form
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


from django.core.exceptions import ValidationError

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "password1", "password2", "first_name", "last_name")
        help_texts = {
            "email": "Por favor ingrese una dirección de correo válida.",
            "password1": "La contraseña debe tener al menos 8 caracteres y combinar letras y números.",
            "password2": "Repita la misma contraseña para confirmarla.",
            "first_name": "Ingrese su primer nombre.",
            "last_name": "Ingrese su apellido.",
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email is already in use.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = user.email  # Asegura que el username sea igual al email
        if commit:
            user.save()
        return user

class CustomUserChangeForm(UserChangeForm):
    password = None
    
    class Meta:
        model = User
        fields = ("email", "first_name", "last_name")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = user.email  # Asegura que el username sea igual al email
        if commit:
            user.save()
        return user