from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(verbose_name='title', max_length=200, blank=True)
    bio = models.TextField(verbose_name='bio', blank=True)
    avatar = models.ImageField(upload_to='avatars/%Y/%m/%d/', blank=True, null=True)
    birth_date = models.DateField(verbose_name='birth date', blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True, editable=False)

    linkedin = models.CharField(max_length=250, null=True, blank=True)
    github = models.CharField(max_length=250, null=True, blank=True)

    skills = models.TextField(null=True, blank=True)
    education = models.TextField(null=True, blank=True)
    location = models.TextField(null=True, blank=True)
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'profile {self.user.get_full_name()}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.get_full_name())
        super().save(*args, **kwargs)
