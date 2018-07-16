from django.db import models
import datetime

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=25)
    image = models.ImageField(upload_to = 'images/')
    description = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title

    def description_mod(self):
        return self.description[:100]

    def date_mod(self):
        return self.date.strftime('%b %e %Y')
