from django.db import models

# Create your models here.
class user(models.Model):
    user_id=  models.AutoField(primary_key= True)
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username