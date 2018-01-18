from django.contrib import admin
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


CATEGORY = [
    (0, 'Animaux de compagnie'),
    (1, 'Rurale'),
    (2, 'Equine'),
]


class ServiceManager(models.Manager):
    def get_service(self, category_int):
        return self.filter(category_int=category_int).order_by('title')

    def get_services(self):
        return [{
            'category': category,
            'services': self.get_service(category_int),
        } for (category_int, category) in CATEGORY ]


class Service(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Titre',
        help_text='Titre tel qu\'il apparaîtra sur le menu de gauche',
    )

    category_int = models.IntegerField(
        verbose_name='categorie',
        choices=CATEGORY,
    )

    @property
    def category(self):
        return CATEGORY[self.category_int][1]

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Date de création du service',
    )

    modified_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Date de modification',
    )

    content = RichTextUploadingField()

    objects = ServiceManager()

    class Meta:
        verbose_name = 'Fiche service'
        verbose_name_plural = 'Fiches service'

    def __str__(self):
        return '{title} ({category})'.format(
          title=self.title,
          category=self.category,
        )


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'modified_at')
    ordering = ['title', 'category_int']
