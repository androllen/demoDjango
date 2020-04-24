from datetime import datetime
from django.db import models

# Create your models here.
class Product(models.Model):
    class Meta():
        ordering = ['-created']

    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, default='')
    description = models.CharField(max_length=500, default='')
    price = models.FloatField()
    isDelete = models.BooleanField(default=False)


class Comment(object):
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()


comment = Comment(email='leila@example.com', content='foo bar')
