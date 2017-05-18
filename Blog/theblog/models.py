from django.db import models


class Post(models.Model):
    slug = models.CharField(max_length=255)
    author = models.CharField(max_length=50)

    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    # picture = models.CharField(max_length=255)
    image = models.FileField(upload_to="photos/%Y/%m/%d",
                             null=True,
                             blank=True)

    body = models.TextField()
    views = models.IntegerField(default=0)
    shares = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    created_at = models.DateTimeField('date published', auto_now_add=True)
