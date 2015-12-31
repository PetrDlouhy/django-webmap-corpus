# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-31 06:53
from __future__ import unicode_literals

import colorful.fields
from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import webmap.utils


class Migration(migrations.Migration):

    replaces = [('webmap', '0001_initial'), ('webmap', '0002_layer_icon'), ('webmap', '0003_marker_order'), ('webmap', '0004_auto_20150112_0935'), ('webmap', '0005_auto_20150607_1533'), ('webmap', '0006_auto_20150607_1534'), ('webmap', '0007_auto_20150616_1606'), ('webmap', '0008_mappreset_status'), ('webmap', '0009_mappreset_desc'), ('webmap', '0010_auto_20151231_0651')]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Layer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text='Name of the layer', max_length=255, verbose_name='name')),
                ('slug', models.SlugField(unique=True, verbose_name='name in URL')),
                ('desc', models.TextField(blank=True, help_text='Layer description.', null=True, verbose_name='description')),
                ('order', models.IntegerField(default=0, verbose_name='order')),
                ('remark', models.TextField(blank=True, help_text='Internal information about layer.', null=True, verbose_name='internal remark')),
                ('enabled', models.BooleanField(default=True, help_text='True = the layer is enabled on map load', verbose_name='Enabled by defalut')),
                ('icon', models.ImageField(blank=True, null=True, storage=webmap.utils.SlugifyFileSystemStorage(), upload_to='layer_icons', verbose_name='layer icon')),
            ],
            options={
                'verbose_name': 'layer',
                'verbose_name_plural': 'layers',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Legend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='name')),
                ('slug', models.SlugField(unique=True, verbose_name='name in URL')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='description')),
                ('image', models.ImageField(storage=webmap.utils.SlugifyFileSystemStorage(), upload_to='ikony', verbose_name='image')),
            ],
            options={
                'verbose_name': 'legend item',
                'verbose_name_plural': 'legend items',
            },
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='License name', max_length=255, verbose_name='name')),
                ('desc', models.TextField(blank=True, help_text='License description.', null=True, verbose_name='description')),
            ],
            options={
                'verbose_name': 'license',
                'verbose_name_plural': 'licenses',
            },
        ),
        migrations.CreateModel(
            name='MapPreset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of preset', max_length=255, verbose_name='name')),
                ('desc', models.TextField(blank=True, help_text='Map preset description.', null=True, verbose_name='description')),
                ('order', models.IntegerField(default=0, verbose_name='order')),
                ('icon', models.ImageField(storage=webmap.utils.SlugifyFileSystemStorage(), upload_to='preset_icons', verbose_name='preset icon')),
            ],
            options={
                'verbose_name': 'map preset',
                'verbose_name_plural': 'map presets',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Marker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the marker.', max_length=255, unique=True, verbose_name='name')),
                ('slug', models.SlugField(null=True, unique=True, verbose_name='name in URL')),
                ('desc', models.TextField(blank=True, help_text='Detailed marker descrption.', null=True, verbose_name='description')),
                ('remark', models.TextField(blank=True, help_text='Internal information about layer.', null=True, verbose_name='internal remark')),
                ('default_icon', models.ImageField(blank=True, null=True, storage=webmap.utils.SlugifyFileSystemStorage(), upload_to='icons', verbose_name='default icon')),
                ('menu_icon', models.ImageField(blank=True, null=True, storage=webmap.utils.SlugifyFileSystemStorage(), upload_to='icons/marker/menu', verbose_name='menu icon')),
                ('minzoom', models.PositiveIntegerField(default=1, help_text='Minimal zoom in which the POIs of this marker will be shown on the map.', verbose_name='Minimal zoom')),
                ('maxzoom', models.PositiveIntegerField(default=10, help_text='Maximal zoom in which the POIs of this marker will be shown on the map.', verbose_name='Maximal zoom')),
                ('line_width', models.FloatField(default=2, verbose_name='line width')),
                ('line_color', colorful.fields.RGBColorField(default='#ffc90e', verbose_name='line color')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('last_modification', models.DateTimeField(auto_now=True, verbose_name='last modification at')),
                ('order', models.IntegerField(default=0, verbose_name='order')),
            ],
            options={
                'verbose_name': 'marker',
                'verbose_name_plural': 'markers',
                'ordering': ['order'],
                'permissions': [('can_only_view', 'Can only view')],
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='Photo name', max_length=255, verbose_name='name')),
                ('desc', models.TextField(blank=True, help_text='Photo description.', null=True, verbose_name='description')),
                ('order', models.IntegerField(default=0, verbose_name='order')),
                ('photographer', models.CharField(blank=True, help_text='Full name of the author of the photography', max_length=255, verbose_name='Photography author')),
                ('photo', models.ImageField(help_text='Upload photo in full resolution.', storage=webmap.utils.SlugifyFileSystemStorage(), upload_to='photo', verbose_name='photo')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='created at')),
                ('last_modification', models.DateTimeField(auto_now=True, null=True, verbose_name='last modification at')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photo_create', to=settings.AUTH_USER_MODEL, verbose_name='author')),
                ('license', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='webmap.License', verbose_name='license')),
            ],
            options={
                'verbose_name': 'photo',
                'verbose_name_plural': 'photographies',
                'ordering': ['order'],
                'permissions': [('can_view_photo_list', 'Can view photo list')],
            },
        ),
        migrations.CreateModel(
            name='Poi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Exact place name', max_length=255, verbose_name='name')),
                ('importance', models.SmallIntegerField(default=0, help_text='Minimal zoom modificator (use 20+ to show always).<br/>', verbose_name='importance')),
                ('geom', django.contrib.gis.db.models.fields.GeometryField(help_text='Add point: Select pencil with plus sign icon and place your point to the map.<br/>\n            Add line: Select line icon and by clicking to map draw the line. Finish drawing with double click.<br/>\n            Add area: Select area icon and by clicking to mapy draw the area. Finish drawing with double click.<br/>\n            Object edition: Select the first icon and then select object in map. Draw points in map to move them, use points in the middle of sections to add new edges.', srid=4326, verbose_name='place geometry')),
                ('desc', models.TextField(blank=True, help_text='Text that will be shown after selecting POI.', null=True, verbose_name='description')),
                ('desc_extra', models.TextField(blank=True, help_text='Text that extends the description.', null=True, verbose_name='detailed description')),
                ('url', models.URLField(blank=True, help_text='Link to the web page of the place.', null=True, verbose_name='URL')),
                ('address', models.CharField(blank=True, help_text='Poi address (street, house number)', max_length=255, null=True, verbose_name='adress')),
                ('remark', models.TextField(blank=True, help_text='Internal information about POI.', null=True, verbose_name='Internal remark')),
                ('properties_cache', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('last_modification', models.DateTimeField(auto_now=True, verbose_name='last modification at')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='poi_create', to=settings.AUTH_USER_MODEL, verbose_name='author')),
                ('marker', models.ForeignKey(help_text='Select icon, that will be shown in map', on_delete=django.db.models.deletion.PROTECT, related_name='pois', to='webmap.Marker', verbose_name='marker')),
            ],
            options={
                'verbose_name': 'place',
                'permissions': [('can_only_own_data_only', 'Can only edit his own data'), ('can_edit_advanced_fields', 'Can edit importance status')],
                'verbose_name_plural': 'places',
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Status name', max_length=255, verbose_name='name')),
                ('as_filter', models.BooleanField(default=False, help_text='Show as a filter in right map menu?', verbose_name='as filter?')),
                ('order', models.IntegerField(default=0, verbose_name='order')),
                ('slug', models.SlugField(unique=True, verbose_name='Name in URL')),
                ('desc', models.TextField(blank=True, help_text='Property description.', null=True, verbose_name='description')),
                ('remark', models.TextField(blank=True, help_text='Internal information about the property.', null=True, verbose_name='Internal remark')),
                ('default_icon', models.ImageField(blank=True, null=True, storage=webmap.utils.SlugifyFileSystemStorage(), upload_to='icons', verbose_name='default icon')),
            ],
            options={
                'verbose_name': 'property',
                'verbose_name_plural': 'properties',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('slug', models.SlugField(unique=True, verbose_name='name in URL')),
                ('geom', django.contrib.gis.db.models.fields.PolygonField(help_text='Sector area', srid=4326, verbose_name='area')),
            ],
            options={
                'verbose_name': 'sector',
                'verbose_name_plural': 'sectors',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Status name', max_length=255, unique=True, verbose_name='name')),
                ('desc', models.TextField(blank=True, help_text='Status description.', null=True, verbose_name='description')),
                ('show', models.BooleanField(default=False, help_text='Show to map user', verbose_name='show')),
                ('show_to_mapper', models.BooleanField(default=False, help_text='Show to mapper', verbose_name='show to mapper')),
            ],
            options={
                'verbose_name': 'status',
                'verbose_name_plural': 'statuses',
            },
        ),
        migrations.CreateModel(
            name='BaseLayer',
            fields=[
                ('layer_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='webmap.Layer')),
                ('url', models.URLField(blank=True, help_text='Base layer tiles url. e.g. ', null=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'base layer',
                'verbose_name_plural': 'base layers',
            },
            bases=('webmap.layer',),
        ),
        migrations.CreateModel(
            name='OverlayLayer',
            fields=[
                ('layer_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='webmap.Layer')),
            ],
            options={
                'verbose_name': 'overlay layer',
                'verbose_name_plural': 'overlay layers',
            },
            bases=('webmap.layer',),
        ),
        migrations.AddField(
            model_name='property',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='webmap.Status', verbose_name='status'),
        ),
        migrations.AddField(
            model_name='poi',
            name='properties',
            field=models.ManyToManyField(blank=True, help_text='POI properties', to='webmap.Property', verbose_name='properties'),
        ),
        migrations.AddField(
            model_name='poi',
            name='status',
            field=models.ForeignKey(default=0, help_text='POI status, determinse if it will be shown in map', on_delete=django.db.models.deletion.SET_DEFAULT, to='webmap.Status', verbose_name='status'),
        ),
        migrations.AddField(
            model_name='poi',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='poi_update', to=settings.AUTH_USER_MODEL, verbose_name='last updated by'),
        ),
        migrations.AddField(
            model_name='photo',
            name='poi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='photos', to='webmap.Poi', verbose_name='poi'),
        ),
        migrations.AddField(
            model_name='photo',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photo_update', to=settings.AUTH_USER_MODEL, verbose_name='last updated by'),
        ),
        migrations.AddField(
            model_name='marker',
            name='layer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='webmap.Layer', verbose_name='layer'),
        ),
        migrations.AddField(
            model_name='marker',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='webmap.Status', verbose_name='status'),
        ),
        migrations.AddField(
            model_name='mappreset',
            name='status',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='webmap.Status', verbose_name='status'),
        ),
        migrations.AddField(
            model_name='layer',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='webmap.Status', verbose_name='status'),
        ),
        migrations.AddField(
            model_name='mappreset',
            name='base_layer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='webmap.BaseLayer', verbose_name='base layer'),
        ),
        migrations.AddField(
            model_name='mappreset',
            name='overlay_layers',
            field=models.ManyToManyField(blank=True, to='webmap.OverlayLayer', verbose_name='overlay layers'),
        ),
    ]