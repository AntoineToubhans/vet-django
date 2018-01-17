from django.contrib import admin
from django.db import models
from ordered_model.models import OrderedModel
from image_cropping import ImageCroppingMixin
from image_cropping import ImageCropField
from image_cropping import ImageRatioField


class PeopleManager(models.Manager):
    def get_ordered_people(self):
        return self.filter(is_active=True).order_by('role_int', 'name')


class People(OrderedModel):
    name = models.CharField(
        max_length=200,
        verbose_name='Prénom, Nom de famille',
        help_text='Nom tel qu\'il apparaîtra sur la page equipe',
    )

    ROLES = [
      (0, 'Docteur Vétérinaire Associé(e)'),
      (1, 'Docteur Vétérinaire'),
      (2, 'ASV'),
      (3, 'Secrétaire comptable'),
      (4, 'Stagiaire'),
    ]

    role_int = models.IntegerField(
        verbose_name='role',
        choices=ROLES,
    )

    @property
    def role(self):
        return self.ROLES[self.role_int][1]

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

    objects = PeopleManager()

    class Meta(OrderedModel.Meta):
        verbose_name = 'Personne'
        verbose_name_plural = 'L\'équipe'

    def __str__(self):
        return '{name} ({role}) {is_active}'.format(
          role=self.role,
          name=self.name,
          is_active='' if self.is_active else '[INACTIF]'
        )


class PeopleAdmin(ImageCroppingMixin, admin.ModelAdmin):
    class Media:
        js = (
            'js/jquery.min.js',
        )
