
from django.db import models

# Create your models here.



class Event(models.Model):

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return self.name