from django.db import models


# Create your models here.
class Tweet(models.Model):
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:20]
