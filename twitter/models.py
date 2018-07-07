from django.db import models
from django.contrib.auth.models import User


class Tweet(models.Model):
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='fan', blank=True, null=True)

    def __str__(self):
        return self.content


class Reply(models.Model):
    content = models.TextField()
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name='comments')
    created_on = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.content

