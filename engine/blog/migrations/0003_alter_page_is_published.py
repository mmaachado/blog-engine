# Generated by Django 5.0.4 on 2024-04-11 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_page_is_published_alter_page_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='is_published',
            field=models.BooleanField(default=False, help_text='check to publish this content'),
        ),
    ]