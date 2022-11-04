from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from PIL import Image

class Instructor(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    def __str__(self):
        return str(self.name)

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
        return str(self.subject)

class Meeting(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    days = models.CharField(max_length=50) 
    start_time = models.CharField(max_length=50) 
    end_time = models.CharField(max_length=50)
    facility_description = models.CharField(max_length=50)
    def __str__(self):
        return str(self.end_time)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    major = models.CharField(max_length=50)
    year = models.CharField(max_length=10)
    bio = models.TextField()
    # schedule = ArrayField(models.CharField(max_length=500), blank=True)

    def __str__(self):
        return self.user.username, self.major, self.year

    # def save(self, *args, **kwargs):
    #     super().save()

    #     img = Image.open(self.avatar.path)

    #     if img.height > 100 or img.width > 100:
    #         new_img = (100, 100)
    #         img.thumbnail(new_img)
    #         img.save(self.avatar.path)

