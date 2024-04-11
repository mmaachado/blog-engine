# Generated by Django 5.0.4 on 2024-04-11 14:07

import utils.model_validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_setup', '0005_blogsetup_favicon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogsetup',
            name='favicon',
            field=models.ImageField(blank=True, default='', upload_to='assets/favicon/%Y/%m', validators=[utils.model_validators.validate_png]),
        ),
    ]
