from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from PIL import Image
from datetime import datetime
class Instructor(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    def __str__(self):
        return str(self.name)

# class Course(models.Model):
#     subject = models.CharField(max_length=4)
#     catalog_number = models.CharField(max_length=4)
#     description = models.TextField()
#     List of sections
    

class Section(models.Model):
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    course_number = models.IntegerField()
    semester_code = models.IntegerField()
    course_section = models.CharField(max_length=5)
    subject = models.CharField(max_length=4)
    catalog_number = models.CharField(max_length=4)
    description = models.TextField()
    units = models.CharField(max_length=20)
    component = models.CharField(max_length=10)
    class_capacity = models.IntegerField()
    wait_list = models.IntegerField()
    wait_cap = models.IntegerField()
    enrollment_total = models.IntegerField()
    enrollment_available = models.IntegerField()
    topic = models.CharField(max_length=50)
    def __str__(self):
        return self.subject

    def get_meetings(self):
        
        return Meeting.objects.filter(section=self)



class Meeting(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    days = models.CharField(max_length=50) 
    start_time = models.CharField(max_length=50) 
    end_time = models.CharField(max_length=50)
    facility_description = models.CharField(max_length=50)
    def __str__(self):
        #"08.30.00.000000-05:00"
        #start_time = datetime.strptime(self.start_time, "%H.%M.%S.%f-%z")
        start_time = self.start_time
        end_time = self.end_time
        return str(self.days) + " " + start_time[:-3] + "-" + end_time

        return "meeting" # str(self.days) + " " + start_time.hour + ":" + start_time.minute + "-" + end_time.hour + ":" + end_time.minute

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    major = models.CharField(max_length=50)
    year = models.CharField(max_length=10)
    bio = models.TextField()
    saved_courses = models.JSONField(default=list, blank=True, null=True)
    saved_sections = models.ManyToManyField(Section, blank=True)


    def __str__(self):
        return str(self.user.username) + ", " + str(self.major) + ", " + str(self.year) + ", " + str(self.saved_courses)