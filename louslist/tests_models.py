from django.test import TestCase
from louslist.models import Section, Meeting, Profile, Course, User

class modelsTests(TestCase):
    def setUp(self):
        Course.objects.create(subject='WGS', 
                              catalog_number='7500', 
                              description='Topics in Gender and Sexuality Studies')
        Section.objects.create(course=Course.objects.get(subject='WGS'), 
                               instructor_name='Tiffany King',
                               instructor_email='tjk9b@virginia.edu',
                               course_number=13512, 
                               semester_code=1228, 
                               course_section='001', 
                               units='3', 
                               component='SEM', 
                               class_capacity=20, 
                               wait_list=0, 
                               wait_cap=199,
                               enrollment_total=13,
                               enrollment_available=7,
                               topic='Approaches to Gender & Sexuality Studies')
        Meeting.objects.create(section=Section.objects.get(instructor_name='Tiffany King'),
                               days='Mo',
                               start_time='15.30.00.000000-05:00',
                               end_time='18.00.00.000000-05:00',
                               facility_description='New Cabell Hall 415')
        User.objects.create(username='bob',
                            email_address = 'bob@virginia.edu')
        Profile.objects.create(user=User.objects.get(username='Bob'),
                               major='CS',
                               year='3rd',
                               bio='',
                               saved_courses=None,
                               saved_sections=None)
    def courses_test(self):
        wgs7500 = Course.objects.get(subject='WGS')
        self.assertEqual(wgs7500.subject, 'WGS')
        self.assertEqual(wgs7500.catalog_number, '7500')
    
    # def meetings_test(self):
    #     print("a")

    # def profiles_test(self):
    #     print("a")
    
    # def sections_test(self):
    #     print("a")

    

