from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from datetime import datetime, date
# from django_extensions.db.fields import AutoSlugField
# from django.utils.text import slugify
from django.template.defaultfilters import slugify
from django.utils.timezone import now

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("home")



class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption


class Post(models.Model):
    title = models.CharField(max_length=60)
    image = models.ImageField(upload_to="posts-images", null=True)
    date = models.DateField(default=now())
    visitors = models.PositiveIntegerField(default=0)
    body = RichTextField(blank=True, null=True)
    # body = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True)
    tags = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    promote = models.BooleanField(default=False, null=True)


    def __str__(self):
        return self.title + " | " + str(self.author)

    def get_absolute_url(self):
        return reverse("home")

    def true_comment_count(self):
        return Comment.objects.filter(post_id=self.id, status=True).count()

    def all_comment_count(self):
        return Comment.objects.filter(post_id=self.id).count()
    # def snippet(self):
    #     return self.body[:265] + " . . ."

    
class Comment(models.Model):
    name = models.CharField(max_length=120)
    text = models.TextField(max_length=400)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    date_added = models.DateField(default=now())
    status = models.BooleanField(default=False)
    child = models.ManyToManyField(
        'self', null=True, related_name="some", blank=True)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, related_name="more", blank=True)

    def __str__(self):
        return self.post.title + " -- " + self.name

    def get_absolute_url(self):
        return reverse("article-detail", args=[str(self.post.id)])