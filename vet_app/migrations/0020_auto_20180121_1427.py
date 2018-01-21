# Generated by Django 2.0 on 2018-01-21 14:27

from django.db import migrations
import djgeojson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('vet_app', '0019_auto_20180121_0851'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clinicconfiguration',
            options={'verbose_name': 'Paramètres de la clinique'},
        ),
        migrations.AddField(
            model_name='clinicconfiguration',
            name='map_marker',
            field=djgeojson.fields.PointField(blank=True, null=True, verbose_name='Position de la clinique sur la carte'),
        ),
    ]
