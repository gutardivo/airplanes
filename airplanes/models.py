from django.db import models

class User(models.Model):
    username = models.CharField(max_length=200,default="")
    password = models.CharField(max_length=32,default="")
    profpic = models.ImageField(upload_to='profile_pictures', null=True, blank=True)

    def __str__(self):
        return f'{self.username}'