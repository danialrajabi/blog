from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils.crypto import get_random_string


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super(Category, self).save(*args, **kwargs)


class Tag(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super(Tag, self).save(*args, **kwargs)


number_of_random_char = 16;


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True, allow_unicode=True, editable=False)
    description = models.TextField()
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts', blank=True, null=True)
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)
    featured_image = models.ImageField(upload_to='post_image', blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None, *args, **kwargs):
        new_slug = slugify(self.title, allow_unicode=True)
        if self.slug[:-number_of_random_char + 1 ] != new_slug:
            self.slug = new_slug + '-' + get_random_string(number_of_random_char)
        super(Post, self).save(*args, **kwargs)

