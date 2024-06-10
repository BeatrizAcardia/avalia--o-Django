from django.db import models

class Inscription(models.Model):
    idEquipamento = models.CharField(max_length=100) # Campo de texto para o nome
    local = models.CharField(max_length=100) # Campo de email
    image = models.ImageField(upload_to='inscriptions/', null=True, blank=True) # Campo de imagem
def __str__(self):
    return self.name # Retorna o nome da inscrição quando o objeto é representado como string
# Create your models here.
