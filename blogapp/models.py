from django.db import models

# Create your models here.

class Blog(models.Model):
    Title = models.CharField(max_length=50)
    Description = models.CharField(max_length=1000)
    Date = models.CharField(max_length=20,null=True)
    Author_Name = models.CharField(max_length=20)
    class Meta:
        db_table = "blog"
       