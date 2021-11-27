from django.db import models
from datetime import datetime   

GENDER_CHOUCE           = (('MALE','MALE'), ('FEMALE','FEMALE'), ('GAY','GAY'))
MERITAL_STATE_CHOICE    = (('UNMARRIED','UNMARRIED'), ('MARRIED','MARRIED'))
TIPE_OF_EMPLOYEE_CHOIE  = (('FULL TIME','FULL TIME'), ('PARTTIME','PARTTIME'), ('TRAINEE','TRAINEE'))

# Create your models here.
class Employees(models.Model):
    name                = models.CharField(max_length = 30, default='None')
    username            = models.CharField(max_length = 30, default='None',unique=True)
    password            = models.CharField(max_length = 30, default='None')
    image               = models.ImageField(default = 'default.JPG')
    discription         = models.CharField(max_length = 1000, default='Discription about the employee here')
    first_name          = models.CharField(max_length = 30, default='add first name')
    last_name           = models.CharField(max_length = 30, default='no last name')
    middle_name         = models.CharField(max_length = 30, default='no middle name')
    date_of_birth       = models.DateField(default=datetime.now(), blank=True)
    phone               = models.IntegerField(max_length = 30, default='0')
    email               = models.EmailField(max_length = 30, default='email',)
    gender              = models.CharField(max_length = 30, default = 'MALE', choices = GENDER_CHOUCE)
    merita_state        = models.CharField(max_length = 30, default = 'UNMARRIED', choices = MERITAL_STATE_CHOICE)
    emailid             = models.CharField(max_length = 30, default='None') 
    pojession           = models.CharField(max_length = 30, default='None')
    enrollment_id       = models.CharField(max_length = 30, default='None') 
    date_of_joining     = models.DateField(default=datetime.now(), blank=True)
    company_email       = models.EmailField(max_length = 30, default='email@gmail.com')
    tipe_of_employee    = models.CharField(max_length = 30, default = 'TRAINEE', choices = TIPE_OF_EMPLOYEE_CHOIE)
    reportingto         = models.CharField(max_length = 30, default="")



STATUS_CHOICES = (('Not assigned','Not assigned'),('Close','Close'),('IN PROGRESS','IN PROGRESS'),('Open','Open'),('In Hold','In Hold'),('Testing','Testing'))

class Project(models.Model):
    manager             = models.ForeignKey('Employees', on_delete=models.CASCADE, default=True)
    project_name        = models.CharField(max_length = 30, default='None',unique=True)
    #employee_name       = models.CharField(max_length = 30, default='None')
    projedct_start_time = models.DateField(default=datetime.now(), blank=True)
    project_end_time    = models.DateField(default=datetime.now(), blank=True) 
    project_status      = models.CharField(max_length = 30, default = 'Not assigned' ,choices = STATUS_CHOICES)
    
class ProjectAssignment1(models.Model):
    project_name        = models.CharField(max_length = 100, default='None') 
    employee_name       = models.CharField(max_length = 100, default='None') 







