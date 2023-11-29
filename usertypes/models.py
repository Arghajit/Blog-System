from django.db import models


#created three user levels-Superadmin,Teacher,Student
class User(models.Model):
    id=models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=30,default="")
    lastname = models.CharField(max_length=30,default="")
    picture=models.ImageField(upload_to='images')
    username = models.CharField(max_length=30,default="")
    email = models.CharField(max_length=30,default="")
    password = models.CharField(max_length=30,default="")
    address = models.CharField(max_length=30,default="")
    type = models.CharField(max_length=30,default="")

    def __str__(self):
        return self.username
    
class Blog(models.Model):
    id=models.AutoField(primary_key=True)
    title = models.CharField(max_length=30,default="")
    image=models.ImageField(upload_to='blogs')
    category = models.CharField(max_length=30,default="")
    summary = models.CharField(max_length=100,default="")
    content = models.CharField(max_length=100,default="")
    url= models.CharField(max_length=100,default="")

    def __str__(self):
        return self.title

    

# Create your models here.
