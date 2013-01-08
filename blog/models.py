from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=80)
    body_raw = models.TextField()
    body_html = models.TextField()

class Comment(models.Model):
    blog = models.ForeignKey(Blog)
    body_raw = models.TextField()
    body_html = models.TextField()



# Create your models here.
