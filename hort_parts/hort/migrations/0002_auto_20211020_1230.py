# Generated by Django 3.2.8 on 2021-10-20 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hort', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='info',
            field=models.TextField(blank=True, null=True, verbose_name='Info'),
        ),
        migrations.AddField(
            model_name='category',
            name='info_de',
            field=models.TextField(blank=True, null=True, verbose_name='Info'),
        ),
        migrations.AddField(
            model_name='category',
            name='info_en',
            field=models.TextField(blank=True, null=True, verbose_name='Info'),
        ),
        migrations.AddField(
            model_name='category',
            name='info_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Info'),
        ),
        migrations.AddField(
            model_name='category',
            name='info_uk',
            field=models.TextField(blank=True, null=True, verbose_name='Info'),
        ),
    ]