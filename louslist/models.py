from django.db import models

class Instructor(models.Model):

    name = models.CharField(max_length=50)
    email = models.EmailField()


class Section(models.Model):
    instructor = models.ForeignKey(Instructor)
    course_number = models.IntegerField()
    semester_code = models.IntegerField()
    course_section = models.CharField(max_length=5)
    subject = models.CharField(max_length=4)
    catalog_number = models.CharField(max_length=4)
    description = models.TextField()
    units = models.IntegerField()
    component = models.CharField(max_length=10)
    class_capacity = models.IntegerField()
    wait_list = models.IntegerField()
    wait_cap = models.IntegerField()
    enrollment_total = models.IntegerField()
    enrollment_available = models.IntegerField()
    topic = models.CharField()

class Meeting(models.Model):
    
    section = models.ForeignKey(Section)
    days = models.CharField() 
    start_time = None 
    end_time = None
    faculty_description = None

