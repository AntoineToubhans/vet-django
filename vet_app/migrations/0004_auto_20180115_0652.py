# Generated by Django 2.0 on 2018-01-15 06:52

from django.db import migrations, models
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('vet_app', '0003_auto_20180114_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='cropping_image',
            field=image_cropping.fields.ImageRatioField('image', '360x360', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping image'),
        ),
        migrations.AlterField(
            model_name='people',
            name='image',
            field=models.ImageField(blank=True, help_text='Uploader une image au format JPG, (!) taille maximale du fichier: 2Mo', null=True, upload_to='people/%Y-%m-%d', verbose_name='image de profile'),
        ),
        migrations.AlterField(
            model_name='people',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Cocher la case si la personne doit être visible sur la page contact de la clinique', verbose_name='Personne active à la clinique?'),
        ),
    ]
