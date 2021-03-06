# Generated by Django 2.0 on 2018-01-22 06:56

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vet_app', '0021_clinicconfiguration_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False)),
                ('title', models.CharField(max_length=200, verbose_name='Titre')),
                ('is_active', models.BooleanField(default=True, help_text="Decocher cette case pour cacher l'actualité", verbose_name='Actualité visible')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date de création du service')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Date de modification')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
            options={
                'verbose_name_plural': 'Actualités',
                'verbose_name': 'Actualité',
            },
        ),
    ]
