from django.db import models

# Create your models here.
class Certificate(models.Model):
    title  =  models.CharField(max_length = 200)
    authors =  models.CharField(max_length = 200)
    authority_source =  models.CharField(max_length = 200)
    date = models.DateTimeField()
    category1 =  models.CharField(max_length = 200)
    category2 =  models.CharField(max_length = 200)
    category3 =  models.CharField(max_length = 200)
    image  =  models.ImageField(upload_to= "certifications")
    image_alt =  models.CharField(max_length = 200)
    url_proof =  models.CharField(max_length = 200)
    Summary =  models.CharField(max_length = 200)

    def date_mod(self):
        return self.date.strftime('%b %e %Y')
    def __str__(self):
        return self.title
