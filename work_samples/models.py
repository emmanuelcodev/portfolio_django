from django.db import models

# Create your models here.
class WorkSamples(models.Model):

    main_image = models.ImageField(upload_to = 'work_samples/images/')
    alt_main_image = models.CharField(max_length = 200)

    project_name = models.CharField(max_length = 200)
    objective = models.CharField(max_length = 200)
    challenges =  models.CharField(max_length = 200)
    accomplishments = models.CharField(max_length = 200)
    technology_used = models.CharField(max_length = 200)
    after_thought = models.CharField(max_length = 200)

    image2 = models.ImageField(upload_to = 'work_samples/images/')
    image3 = models.ImageField(upload_to = 'work_samples/images/')
    image4 = models.ImageField(upload_to = 'work_samples/images/')

    alt_image2 = models.CharField(max_length = 200)
    alt_image3 = models.CharField(max_length = 200)
    alt_image4 = models.CharField(max_length = 200)



    github_or_url_title = models.CharField(max_length = 200)
    github_or_url = models.CharField(max_length = 200)
    category1 = models.CharField(max_length = 200)
    category2 = models.CharField(max_length = 200)
    category3 = models.CharField(max_length = 200)

    def __str__(self):
        return self.project_name
