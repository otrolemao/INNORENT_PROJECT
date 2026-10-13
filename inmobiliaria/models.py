from django.db import models


class Comuna(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    region = models.CharField(max_length=100)
    activa = models.BooleanField(default=True)
    codigo_clasificacion = models.CharField(max_length=10, unique=True)

    class Meta:
        verbose_name = "Comuna"
        verbose_name_plural = "Comunas"
        ordering = ['nombre']

    def __str__(self):
        return f'{self.nombre} ({self.codigo_clasificacion})'


class Propiedad(models.Model):
    TIPOS = [
        ('DEPARTAMENTO', 'Departamento'),
        ('CASA', 'Casa'),
        ('OFICINA', 'Oficina'),
    ]

    codigo_propiedad = models.CharField(max_length=10, unique=True)
    direccion = models.CharField(max_length=200)
    tipo_propiedad = models.CharField(max_length=20, choices=TIPOS)
    precio_arriendo = models.IntegerField()
    dormitorios = models.IntegerField()
    banos = models.IntegerField()
    disponible = models.BooleanField(default=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    comuna = models.ForeignKey(
        Comuna,
        on_delete=models.CASCADE,
        related_name='propiedades'
    )

    class Meta:
        verbose_name = "Propiedad"
        verbose_name_plural = "Propiedades"
        ordering = ['-fecha_publicacion']

    def __str__(self):
        return f'{self.codigo_propiedad} - {self.direccion}'