# Generated by Django 4.2.13 on 2024-06-26 15:15

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('purpose', models.TextField()),
                ('mockup_image', cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='image')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('details', models.TextField()),
                ('issues', models.TextField(blank=True)),
                ('progress', models.IntegerField(choices=[(0, 'Still an Idea'), (1, 'Working on prototypes'), (2, 'Ready for production'), (3, 'This idea is now a reality!')], default=0)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ideas', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
