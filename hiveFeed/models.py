from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class hivePost(models.Model):
    post_title = models.CharField(max_length = 50, default ='title')
    post_body = models.TextField(default='body')
    post_author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name="feed_post")


    def __str__(self):
        return self.post_title

