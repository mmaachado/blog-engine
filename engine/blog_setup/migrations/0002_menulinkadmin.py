# Generated by Django 5.0.4 on 2024-04-10 13:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_setup', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuLinkAdmin',
            fields=[
                ('menulink_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog_setup.menulink')),
            ],
            bases=('blog_setup.menulink',),
        ),
    ]
