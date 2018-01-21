from django import forms
from django.db import models
from djgeojson.fields import PointField
from leaflet.admin import LeafletGeoAdmin
from multiselectfield import MultiSelectField
from phonenumber_field.modelfields import PhoneNumberField as ModelPhoneNumberField
from phonenumber_field.formfields import PhoneNumberField as FormPhoneNumberField
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget
from solo.admin import SingletonModelAdmin
from solo.models import SingletonModel


class ClinicOpeningHour(models.Model):
    DAYS = [
        (0, 'Lundi'),
        (1, 'Mardi'),
        (2, 'Mercredi'),
        (3, 'Jeudi'),
        (4, 'Vendredi'),
        (5, 'Samedi'),
        (6, 'Dimanche'),
    ]

    opening = models.TimeField(
        verbose_name='Ouverture',
    )

    closing = models.TimeField(
        verbose_name='Fermeture',
    )

    days = MultiSelectField(
        choices=DAYS,
        verbose_name='Jours',
        min_choices=1,
    )

    def __str__(self):
        decoded_days = ', '.join([self.DAYS[int(day)][1] for day in self.days])

        return '{days} de {opening:%H}h{opening:%M} à {closing:%H}h{closing:%M}'.format(
            days=decoded_days,
            opening=self.opening,
            closing=self.closing,
        )

    class Meta:
        verbose_name = 'Horaîres d\'ouverture'



class ClinicConfiguration(SingletonModel):
    name = models.CharField(
        max_length=300,
        verbose_name='Nom de la clinique',
        help_text='Le nom de la clinique apparaît dans le titre du site',
        default='Clinique Vétérinaire',
    )

    phone_number = ModelPhoneNumberField(
        verbose_name='Numéro de téléphone de la clinique',
        blank=True,
    )

    email = models.EmailField(
        verbose_name='Email de la clinique',
        blank=True,
    )

    opening_hours = models.ManyToManyField(
        ClinicOpeningHour,
        verbose_name='Horaires d\'ouverture',
        blank=True,
    )

    address = models.CharField(
        max_length=300,
        verbose_name='Adresse de la clinique',
        blank=True,
    )

    map_marker = PointField(
        blank=True,
        null=True,
        verbose_name='Position de la clinique sur la carte',
    )

    class Meta:
        verbose_name = 'Paramètres de la clinique'



class ClinicConfigurationAdminForm(forms.ModelForm):
    phone_number = FormPhoneNumberField(
        label='Numéro de téléphone de la clinique',
        widget=PhoneNumberInternationalFallbackWidget(),
    )

    class Meta:
        model = ClinicConfiguration
        fields = "__all__"


class ClinicConfigurationAdmin(SingletonModelAdmin, LeafletGeoAdmin):
    form = ClinicConfigurationAdminForm
