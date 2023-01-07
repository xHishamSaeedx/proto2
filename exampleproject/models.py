from django.db import models
import uuid
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from datetime import timedelta
import json
# Create your models here.

class Classproject(models.Model):
    title = models.CharField(max_length=200) 
    featured_image = models.ImageField(null=True , blank = True , default= "default.jpg")
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return self.title





class semester(models.Model):
    name = models.CharField(max_length=200,)
    curriculum = models.ForeignKey(Classproject,on_delete=models.CASCADE)
    branches = models.ManyToManyField('branch',blank = True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False) 

    def __str__(self):
        return self.name


class branch(models.Model):
    name = models.CharField(max_length=400,)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)    #these 2 created and id r gonna be common for all
    def __str__(self):
        return self.name

class subject(models.Model):
    name = models.CharField(max_length=400,)
    branch = models.ForeignKey(branch,on_delete=models.CASCADE)
    units = models.ManyToManyField('unit',blank = True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)    #these 2 created and id r gonna be common for all
    def __str__(self):
        return self.name

class unit(models.Model):
    name = models.CharField(max_length=400,)
    topic = models.ManyToManyField('topic',blank = True)
    weightage = models.IntegerField(default=0,null=True,blank=True,validators=[MaxValueValidator(100),MinValueValidator(0)])
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)    #these 2 created and id r gonna be common for all
    def __str__(self):
        return self.name

class topic(models.Model):
    name = models.CharField(max_length=400,)
    created = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0,null=True,blank=True,validators=[MaxValueValidator(10),MinValueValidator(0)])
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)    #these 2 created and id r gonna be common for all
    def __str__(self):
        return self.name

class Timetable1(models.Model):
    start_date = models.CharField(max_length=400,)
    end_date = models.CharField(max_length=400,)
    num_subjects = models.IntegerField(default=0,null=True,blank=True)
    
   
    weekday_hrs = models.IntegerField(default=0,null=True,blank=True)
    weekend_hrs = models.IntegerField(default=0,null=True,blank=True)
    
class whatsubjects(models.Model):
    subjects = models.ManyToManyField('subject',blank = True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)    #these 2 created and id r gonna be common for all
    



    
class Timetable2(models.Model):
    custom_date = models.CharField(max_length=400,)
    custom_hrs = models.IntegerField(default=0,null=True,blank=True)
    


class Timetable3(models.Model):
    units = models.ManyToManyField('unit',blank = True)
  




class sumn(models.Model):
    units = models.ManyToManyField('unit',blank = True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)    #these 2 created and id r gonna be common for all
    



class subjecthrs(models.Model):
    subject_hrs = models.CharField(max_length=400)
    priority = models.CharField(max_length=400,default="0")
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)    #these 2 created and id r gonna be common for all
    

class FinalTT(models.Model):
    zefile = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False) 
