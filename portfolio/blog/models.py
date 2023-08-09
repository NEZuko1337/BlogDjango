from django.db import models

class BlogModel(models.Model):
    title = models.CharField(max_length=40)
    date = models.DateField(auto_now=True)
    description = models.TextField(max_length=150)

    def __str__(self) -> str:
        return self.title
