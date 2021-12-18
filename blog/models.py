from django.db import models

class Post (models.Model):
    author=models.CharField(max_length=50,default='author')
    title = models.CharField(max_length=50)
    description = models.TextField()
    

    def __str__(self):
        return self.title