from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from ordered_model.models import OrderedModel
from ordered_model.admin import OrderedModelAdmin


class GalleryImage(OrderedModel):
    description = models.CharField(
        max_length=300,
        verbose_name='Description',
    )

    image = models.ImageField(
        upload_to='gallery',
        verbose_name='Image',
    )

    class Meta(OrderedModel.Meta):
        verbose_name = 'Image de la galerie'
        verbose_name_plural = 'Images de la galerie'


class GalleryImageAdmin(OrderedModelAdmin):
    list_display = ('description', 'move_up_down_links')
