from django.db import models

# Create your models here.
from django.db import models
import datetime
from django.utils.text import slugify
# Create your models here.


class Profile(models.Model):

     name = models.CharField(max_length=100)
     email = models.EmailField(max_length=150)
     phone = models.CharField(max_length=13, blank=True)
     message = models.TextField(max_length=500)
     lokaci = models.DateTimeField(auto_now_add=True)

class Meta:
        ordering = ['lokaci']

        def __str__(self):
            return f"Name: {self.name}"


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
          return self.name


class Post(models.Model):
    headline = models.CharField(max_length=200)
    sub_headline = models.CharField(max_length=200, null=True, blank=True)
    body = models.TextField(max_length=1000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, null=True)
    thumbnail = models.ImageField(
            null=True, blank=True, upload_to='', default="/images/placeholder.png")
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
            return self.headline

    def save(self, *args, **kwargs):
           
        if self.slug == None:
                                slug = slugify(self.headline)

                                has_slug = Post.objects.filter(slug=slug).exists()
                                count = 1
                                while has_slug:
                                        count += 1
                                        slug = slugify(self.headline) + '-' + str(count) 
                                        has_slug = Post.objects.filter(slug=slug).exists()

                                self.slug = slug
        super().save(*args, **kwargs)
class Subscribers(models.Model):
        subscriber=models.EmailField(max_length=200)
        def __str__(self):
                return self.subscriber