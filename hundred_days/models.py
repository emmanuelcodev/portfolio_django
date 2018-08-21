from django.db import models

# Create your models here.
class HProject(models.Model):
    title  =  models.CharField(max_length = 200)
    date = models.DateTimeField()
    category1 =  models.CharField(max_length = 50)
    category2 =  models.CharField(max_length = 50)
    category3 =  models.CharField(max_length = 50)
    image  =  models.ImageField(upload_to= "certifications")
    image_alt =  models.CharField(max_length = 200)
    url_proof =  models.CharField(max_length = 200)
    Summary =  models.CharField(max_length = 450)
    source = models.CharField(max_length = 50)

    def date_mod(self):
        return self.date.strftime('%b %e %Y')
    def __str__(self):
        return self.title
