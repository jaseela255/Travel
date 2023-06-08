from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

    def __str__(self):
        return self.name
    
class team(models.Model):
    img1=models.ImageField(upload_to='pics1')
    name1=models.CharField(max_length=250)
    about=models.TextField()

    def __str__(self):
        return self.name1

    
