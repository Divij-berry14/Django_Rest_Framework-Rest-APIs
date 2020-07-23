from django.db import models

# Create your models here.
class Book(models.Model):
    name=models.CharField(max_length=50)
    author=models.CharField(max_length=30,default="anonymous")
    email=models.EmailField(blank=True)
    picture=models.ImageField() #This ImageField is the reason why we installed pillow in
    # this virtual environment. Django by default uses pillow to handle Images in ImageField.
    describe=models.TextField(default="About the work")

    def __str__(self):
        return self.name
