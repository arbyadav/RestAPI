from django.db import models

# Create your models here.

class UsersD (models.Model):
    employee_id= models.CharField(max_length=10, unique=True)
    name= models.CharField(max_length=100) #Amit
    age= models.IntegerField() #32
    ranking=models.FloatField() #2.5

    def upload_photo(self,filename):
        path='hrm/photo/{}'.format(filename)
        return path
    
    photo=models.ImageField(upload_to='upload_photo', null=True, blank=True)

    def upload_file(self,filename):
        path='hrm/file/{}'.format(filename)
        return path
    
    resume=models.ImageField(upload_to='upload_file', null=True, blank=True)

    def __str__(self):
        return f"{self.employee_id}-{self.name}" #to modify look in db objectss