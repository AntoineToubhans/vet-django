from django.db import models
from .fields import ContentTypeRestrictedFileField


class People(models.Model):
    first_name = models.CharField(
        max_length=200,
        verbose_name='Prénom',
    )

    last_name = models.CharField(
        max_length=200,
        verbose_name='Nom de famille',
    )

    ROLES = [
      ('Docteur Vétérinaire', 'Docteur Vétérinaire'),
      ('ASV', 'ASV'),
      ('Secrétaire comptable', 'Secrétaire comptable'),
    ]

    role = models.CharField(
        max_length=100,
        verbose_name='role',
        choices=ROLES,
    )

    image = ContentTypeRestrictedFileField(
        content_types=['image/jpeg'],
        max_upload_size=2097152,
        upload_to="people/%Y-%m-%d",
        null=True,
        blank=True,
        verbose_name='image de profile',
        help_text='Uploader une image au format JPG, (!) taille maximale du fichier: 2Mio'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Date de création de la rubrique',
    )

    class Meta:
        verbose_name = 'Personne'
        verbose_name_plural = 'L\'equipe'

    def __str__(self):
        return '{first_name} {last_name} ({role})'.format(
          role=self.role,
          first_name=self.first_name,
          last_name=self.last_name,
        )
