from django.db import models
from solo.models import SingletonModel


class ClinicConfiguration(SingletonModel):
    name = models.CharField(
        max_length=300,
        verbose_name='Nom de la clinique',
        help_text='Le nom de la clinique apparaît dans le titre du site',
        default='Clinique Vétérinaire',
    )

    class Meta:
        verbose_name = 'Paramètre de la clinique'
