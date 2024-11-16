from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here. Se crea la tabla usuarios
class Usuarios(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=150, unique=True)
    correo = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=120)

    def save(self, *args, **kwargs):
        if not self.pk or 'contraseña' in self.get_dirty_fields():
            self.contraseña = make_password(self.contraseña)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.usuario