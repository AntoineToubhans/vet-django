# Generated by Django 2.0 on 2018-01-14 18:50

from django.db import migrations, models
import vet_app.fields


class Migration(migrations.Migration):

    dependencies = [
        ('vet_app', '0002_auto_20180114_1838'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Cocher la case si la personne doit être visible sur la page contact', verbose_name='Personne visible'),
        ),
        migrations.AlterField(
            model_name='people',
            name='image',
            field=vet_app.fields.ContentTypeRestrictedFileField(blank=True, help_text='Uploader une image au format JPG, (!) taille maximale du fichier: 2Mio', null=True, upload_to='people/%Y-%m-%d', verbose_name='image de profile'),
        ),
    ]
