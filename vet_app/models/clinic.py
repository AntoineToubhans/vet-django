from django import forms
from django.db import models
from solo.admin import SingletonModelAdmin
from solo.models import SingletonModel
from phonenumber_field.modelfields import PhoneNumberField as ModelPhoneNumberField
from phonenumber_field.formfields import PhoneNumberField as FormPhoneNumberField
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget

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

    class Meta:
        verbose_name = 'Paramètre de la clinique'



class ClinicConfigurationAdminForm(forms.ModelForm):
    phone_number = FormPhoneNumberField(
        label='Numéro de téléphone de la clinique',
        widget=PhoneNumberInternationalFallbackWidget(),
    )

    class Meta:
        model = ClinicConfiguration
        fields = "__all__"


class ClinicConfigurationAdmin(SingletonModelAdmin):
    form = ClinicConfigurationAdminForm
