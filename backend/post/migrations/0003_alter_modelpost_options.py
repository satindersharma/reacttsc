# Generated by Django 4.1.3 on 2022-12-07 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_modelpost_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='modelpost',
            options={'ordering': ['id'], 'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
    ]
