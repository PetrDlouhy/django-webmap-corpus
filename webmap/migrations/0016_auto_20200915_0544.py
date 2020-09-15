# Generated by Django 2.2.16 on 2020-09-15 05:44

from django.db import migrations, models
import django.db.models.deletion
import webmap.utils


class Migration(migrations.Migration):

    dependencies = [
        ('webmap', '0015_auto_20161130_1753'),
    ]

    operations = [
        migrations.AddField(
            model_name='layer',
            name='icon_height',
            field=models.IntegerField(default=20),
        ),
        migrations.AddField(
            model_name='layer',
            name='icon_width',
            field=models.IntegerField(default=20),
        ),
        migrations.AddField(
            model_name='marker',
            name='default_icon_height',
            field=models.IntegerField(default=20),
        ),
        migrations.AddField(
            model_name='marker',
            name='default_icon_width',
            field=models.IntegerField(default=20),
        ),
        migrations.AddField(
            model_name='marker',
            name='menu_icon_height',
            field=models.IntegerField(default=20),
        ),
        migrations.AddField(
            model_name='marker',
            name='menu_icon_width',
            field=models.IntegerField(default=20),
        ),
        migrations.AddField(
            model_name='property',
            name='default_icon_height',
            field=models.IntegerField(default=20),
        ),
        migrations.AddField(
            model_name='property',
            name='default_icon_width',
            field=models.IntegerField(default=20),
        ),
        migrations.AlterField(
            model_name='layer',
            name='icon',
            field=models.ImageField(blank=True, height_field='icon_height', null=True, storage=webmap.utils.SlugifyFileSystemStorage(), upload_to='layer_icons', verbose_name='layer icon', width_field='icon_width'),
        ),
        migrations.AlterField(
            model_name='mappreset',
            name='overlay_layers',
            field=models.ManyToManyField(blank=True, limit_choices_to={'status__show_to_mapper': 'True'}, to='webmap.OverlayLayer', verbose_name='overlay layers'),
        ),
        migrations.AlterField(
            model_name='marker',
            name='default_icon',
            field=models.ImageField(blank=True, height_field='default_icon_height', null=True, storage=webmap.utils.SlugifyFileSystemStorage(), upload_to='icons', verbose_name='default icon', width_field='default_icon_width'),
        ),
        migrations.AlterField(
            model_name='marker',
            name='menu_icon',
            field=models.ImageField(blank=True, height_field='menu_icon_height', null=True, storage=webmap.utils.SlugifyFileSystemStorage(), upload_to='icons/marker/menu', verbose_name='menu icon', width_field='menu_icon_width'),
        ),
        migrations.AlterField(
            model_name='poi',
            name='marker',
            field=models.ForeignKey(help_text='Select icon, that will be shown in map', limit_choices_to={'layer__status__show_to_mapper': 'True', 'status__show_to_mapper': 'True'}, on_delete=django.db.models.deletion.PROTECT, related_name='pois', to='webmap.Marker', verbose_name='marker'),
        ),
        migrations.AlterField(
            model_name='poi',
            name='properties',
            field=models.ManyToManyField(blank=True, help_text='POI properties', limit_choices_to={'status__show_to_mapper': 'True'}, to='webmap.Property', verbose_name='properties'),
        ),
        migrations.AlterField(
            model_name='property',
            name='default_icon',
            field=models.ImageField(blank=True, height_field='default_icon_height', null=True, storage=webmap.utils.SlugifyFileSystemStorage(), upload_to='icons', verbose_name='default icon', width_field='default_icon_width'),
        ),
    ]