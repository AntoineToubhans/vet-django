from django.contrib import admin
from django.db import models
from image_cropping import ImageCroppingMixin
from image_cropping import ImageCropField
from image_cropping import ImageRatioField


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
      ('Stagiaire', 'Stagiaire'),
    ]

    role = models.CharField(
        max_length=100,
        verbose_name='role',
        choices=ROLES,
    )

    image = ImageCropField(
        null=True,
        blank=True,
        upload_to="people_profile_image",
        verbose_name='Image de profile',
        help_text='Uploader une image de profile pour la personne',
    )

    cropping_image = ImageRatioField(
        'image',
        '360x360',
        free_crop=False,
        verbose_name='Selection dans l\'image de profil',
        help_text='Choisissez la partie de l\'image à afficher',
    )

    is_active = models.BooleanField(
        verbose_name='Personne active à la clinique?',
        default=True,
        help_text='Cocher la case si la personne doit être visible sur la page contact de la clinique',
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Date de création de la rubrique',
    )

    class Meta:
        verbose_name = 'Personne'
        verbose_name_plural = 'L\'équipe'

    def __str__(self):
        return '{first_name} {last_name} ({role}) {is_active}'.format(
          role=self.role,
          first_name=self.first_name,
          last_name=self.last_name,
          is_active='' if self.is_active else '[INACTIF]'
        )


class PeopleAdmin(ImageCroppingMixin, admin.ModelAdmin):
    class Media:
        js = (
            'js/jquery.min.js',
        )
