from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(verbose_name='description')

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(verbose_name='name', max_length=200)
    description = models.TextField('description')
    image = models.ImageField(verbose_name='image', upload_to="project_image/%Y/%m/%d/", blank=True)
    owner = models.ForeignKey(User, verbose_name='owner', on_delete=models.PROTECT)
    content = RichTextUploadingField(verbose_name='content')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_qtd_posts(self):
        return self.posts.count()


class Post(models.Model):
    title = models.CharField(verbose_name='title', max_length=200)
    author = models.ForeignKey(User, verbose_name='author', on_delete=models.CASCADE)
    description = models.TextField(verbose_name='description', null=True, blank=True)
    content = RichTextUploadingField(verbose_name='content')
    image = models.ImageField(verbose_name='image', upload_to="post_image/%Y/%m/%d/", blank=True)
    categories = models.ManyToManyField(Category, verbose_name='category', blank=True)
    tags = models.ManyToManyField(Tag, verbose_name='tag', blank=True)
    project = models.ForeignKey(Project, verbose_name='project', related_name='posts', null=True, blank=True, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)
    views = models.PositiveIntegerField(default=0, editable=False)
    slug = models.SlugField(max_length=200, unique=True, editable=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.post.title}"


class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s bookmark: {self.post.title}"


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s like on {self.post.title}"
