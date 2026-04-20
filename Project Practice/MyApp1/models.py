from django.db import models

# Create your models here.
class teacher(models.Model):
     Name = models.CharField(max_length=25)
     Area = models.CharField(max_length=30)
     def __str__(self):
         return self.Name
class assessment(models.Model):
    Name = models.CharField(max_length=100)
    Topic = models.CharField(max_length=50)

    teacher = models.ForeignKey(teacher, on_delete=models.CASCADE)
    def __str__(self):
       return self.Name