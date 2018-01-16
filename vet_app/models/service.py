from django.db import models


class Service(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Titre',
        help_text='Titre tel qu\'il apparaîtra sur le menu de gauche',
    )

    CATEGORY = [
      (0, 'Animaux de compagnie'),
      (1, 'Rurale'),
      (2, 'Equine'),
    ]

    category_int = models.IntegerField(
        verbose_name='categorie',
        choices=CATEGORY,
    )

    @property
    def category(self):
        return self.CATEGORY[self.category_int][1]

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Date de création de la rubrique',
    )

    class Meta:
        verbose_name = 'Fiche service'
        verbose_name_plural = 'Fiches service'

    def __str__(self):
        return '{title} ({category})'.format(
          title=self.title,
          category=self.category,
        )
