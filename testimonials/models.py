from django.db import models

# Create your models here.

class Testimonial(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    pic_image = models.ImageField(upload_to = 'testimonials/images')
    testimony = models.CharField(max_length = 700)
