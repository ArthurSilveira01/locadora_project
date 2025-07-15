from django.db import models
from django.template.defaultfilters import length
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone

class Automovel(models.Model):
    placa = models.TextField(max_length=10, null=False, blank=False)

    marca = models.TextField(max_length=100, blank=False, null=False)

    modelo = models.TextField(max_length=100, blank=False, null=False)

    ano = models.IntegerField(blank=False, null=False, validators=[MinValueValidator(1900), MaxValueValidator(timezone.now().year)] )

    cor = models.TextField(max_length=50, blank=True, null=True)

    valor_diaria = models.DecimalField(blank=False, null=False, max_digits=8, decimal_places=2)

    disponivel = models.BooleanField(True)

    data_cadastro = models.DateTimeField(blank=False, null=False)

    def __str__(self):
        return f'Placa: {self.placa}, Marca: {self.marca}, Modelo: {self.modelo}'


