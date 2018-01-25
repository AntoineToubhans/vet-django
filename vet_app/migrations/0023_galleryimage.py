# Generated by Django 2.0 on 2018-01-24 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vet_app', '0022_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False)),
                ('description', models.CharField(max_length=300, verbose_name='Description')),
                ('image', models.ImageField(upload_to='gallery', verbose_name='Image')),
            ],
            options={
                'verbose_name_plural': 'Images de la galerie',
                'verbose_name': 'Image de la galerie',
            },
        ),
    ]
