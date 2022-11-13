from django.test import TestCase
from louslist.models import Course, Section, Meeting, User, Profile

class FeaturesTests(TestCase):
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
        self.user1 = User.objects.create_user(username='micah', password='test')
    
    # tests for features:

    # search for a course
    def test_search(self):
        response = self.client.get('/search/general?q=cs')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search_general_results.html')

    # search for an instructor
    def test_search(self):
        response = self.client.get('/search/general?q=bloomfield')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search_general_results.html')

    # updating profile
    # def test_updating_profile(self):
    #     user = self.user1
    #     self.client.force_login(user)
    #     self.client.post('/profile',{'username': 'keivon'},)
    #     user.refresh_from_db()
    #     self.assertEqual(user.username, 'keivon')

    # saving a course
    # unsaving a course
    # adding a friend
    # unadding a friend