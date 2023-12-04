from django.db import models

class Employee(models.Model):
    uname=models.CharField(max_length=30)
    email=models.EmailField(null=True)
    age=models.PositiveIntegerField()
    place=models.CharField(max_length=30)
    def __str__(self):
        return self.uname

class Emp(models.Model):
    name=models.CharField(max_length=30)
    place=models.CharField(max_length=30)
    salary=models.PositiveBigIntegerField()
    contact=models.CharField(max_length=30)

class Book(models.Model):
    title=models.CharField(max_length=30)      
    author=models.CharField(max_length=30)
    publication_year=models.PositiveIntegerField()
    genre=models.CharField(max_length=30)

class Details(models.Model):
    name=models.CharField(max_length=20)
    course=models.CharField(max_length=20)
    email=models.EmailField(null=True)

    def __str__(self):
        return self.name
    
class Students(models.Model):
    name=models.CharField(max_length=30)
    place=models.CharField(max_length=30)
    email=models.EmailField(null=True)
    age=models.PositiveIntegerField()
    gender=models.CharField(max_length=30)

