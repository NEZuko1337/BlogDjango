from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to="port/images/")
    URL = models.URLField(blank=True)
    

    def __str__(self):
        return self.title