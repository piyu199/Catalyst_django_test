from django.db import models

# Create your models here.
class FileUpload(models.Model):
    file=models.FileField(upload_to='files')


    def __str__(self):
        return self.file
    
class Person(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=300)
    domain=models.CharField(max_length=300)
    year_founded=models.IntegerField()
    industry=models.CharField(max_length=300)
    locality=models.CharField(max_length=300)
    country=models.CharField(max_length=300)

    def __str__(self):
        return self.name,self.country,self.year_founded