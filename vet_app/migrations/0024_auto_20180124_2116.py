# Generated by Django 2.0 on 2018-01-24 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vet_app', '0023_galleryimage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='galleryimage',
            options={'ordering': ('order',), 'verbose_name': 'Image de la galerie', 'verbose_name_plural': 'Images de la galerie'},
        ),
    ]