# Generated by Django 4.1.3 on 2022-12-07 04:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date and time when this entry was created in the system')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Date and time when the table data was last updated in the system')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, help_text='Unique identification number for the user.', unique=True)),
                ('title', models.CharField(help_text='Post Title', max_length=100)),
                ('body', models.CharField(help_text='Post Body', max_length=250)),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
