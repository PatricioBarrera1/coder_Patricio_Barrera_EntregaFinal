from django.db import models

# Create your models here.
    
    #atributos
        #flotante = models.FloatField()
        #string = models.CharField(default="")
        #numero = models.IntegerField (default=0, blank=True, null=True)
        #verdadero o falso = models.BooleanField (default = False)
        # fecha = models.DateField()
        # fecha_y_hora = models.DateTimeField()
        # duracion = models.DurationField()
        
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    is_available = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
