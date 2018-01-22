from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from ordered_model.models import OrderedModel
from ordered_model.admin import OrderedModelAdmin


class News(OrderedModel):
    title = models.CharField(
        max_length=200,
        verbose_name='Titre',
    )

    is_active = models.BooleanField(
        verbose_name='Actualité visible',
        default=True,
        help_text='Decocher cette case pour cacher l\'actualité',
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Date de création du service',
    )

    modified_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Date de modification',
    )

    content = RichTextUploadingField()

    class Meta:
        verbose_name = 'Actualité'
        verbose_name_plural = 'Actualités'


class NewsAdmin(OrderedModelAdmin):
    list_display = ('title', 'is_active', 'created_at', 'modified_at')
