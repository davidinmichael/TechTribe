from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='uploads/')
    content = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
