from django.db import models

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key =True)
    name = models.CharField( max_length=255)
    email = models.CharField( max_length=100)
    phone = models.CharField( max_length=13)
    content = models.TextField()
    timeStamp = models.DateTimeField( blank=True, auto_now_add=True)

    def __str__(self):
        return self.name

class Login(models.Model):
    email = models.CharField( max_length=100)
    password = models.CharField( max_length=13)
    timeStamp = models.DateTimeField( blank=True, auto_now_add=True)

    def __str__(self):
        return self.email
    
class Signup(models.Model):
    sno = models.AutoField(primary_key =True)
    name = models.CharField( max_length=255)
    email = models.CharField( max_length=100)
    phone = models.CharField( max_length=13)
    content = models.TextField()
    timeStamp = models.DateTimeField( blank=True, auto_now_add=True)

    def __str__(self):
        return self.name