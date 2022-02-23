from django.db import models

# Create your models here.


class Contact(models.Model):
    num = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)

    
    def __str__(self):
        return self.name
    