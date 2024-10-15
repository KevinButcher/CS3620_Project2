from django.db import models

# Create your models here.
class MadLib(models.Model):
    title = models.CharField(max_length=100)
    template = models.TextField()

    def __str__(self):
        return self.title