from __future__ import unicode_literals
from django.db import models

# Create your models here.
class testmodel(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    content = models.TextField()
    cdate = models.DateTimeField(auto_now_add=True)


