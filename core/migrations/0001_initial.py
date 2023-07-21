# Generated by Django 4.0.4 on 2023-07-21 17:56

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
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, verbose_name='title')),
                ('bio', models.TextField(blank=True, verbose_name='bio')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/%Y/%m/%d/')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='birth date')),
                ('slug', models.SlugField(editable=False, max_length=200, unique=True)),
                ('linkedin', models.CharField(blank=True, max_length=250, null=True)),
                ('github', models.CharField(blank=True, max_length=250, null=True)),
                ('skills', models.TextField(blank=True, null=True)),
                ('education', models.TextField(blank=True, null=True)),
                ('location', models.TextField(blank=True, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
