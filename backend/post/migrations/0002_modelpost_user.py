# Generated by Django 4.1.3 on 2022-12-07 07:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelpost',
            name='user',
            field=models.ForeignKey(default=3, help_text='The user associated with this post.', on_delete=django.db.models.deletion.CASCADE, related_name='user_post', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
