# Generated by Django 5.0.4 on 2024-04-11 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='is_published',
            field=models.BooleanField(default=False, help_text='Este campo precisará estar marcado para a página ser exibida publicamente.'),
        ),
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=255, unique=True),
        ),
    ]
