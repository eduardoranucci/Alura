from django.db import models
from django.utils.translation import gettext_lazy as _

class ClasseViagem(models.TextChoices):
        ECONOMICA = 'Econômica', _('Econômica')
        EXECUTIVA = 'Executiva', _('Executiva')
        PRIMEIRA_CLASSE = 'Primeira Classe', _('Primeira Classe')