from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse 
from louslist.models import Instructor, Section, Meeting

# class SISAPITests(TestCase):
#     # Get this error: raise NotSupportedError(django.db.utils.NotSupportedError: DISTINCT ON fields is not supported by this database backend
#     # add 'name='dept_page'' to urls.py path
#     # def test_deptpage(self):
#     #     response = self.client.get(reverse('dept_page', kwargs={'dept': 'ANTH'}))
#     #     self.assertEqual(response.status_code, 200)
#     # test coursepage
    
#     def test_homepage(self):
#         response = self.client.get(reverse('homepage'))
#         self.assertEqual(response.status_code, 200)

#     def test_deptpage_url(self):
#         response = reverse('dept_page', kwargs={'dept': 'ANTH'})
#         self.assertEqual(response, '/departments/ANTH')

#     def test_coursepage_url(self):
#         anth_1010 = {'dept': 'ANTH', 'cn': '1010', 'desc': 'Introduction to Anthropology'}
#         response = reverse('course_page', kwargs=anth_1010)
#         self.assertEqual(response, '/departments/ANTH/1010/Introduction%20to%20Anthropology/info')

#     def test_instructor_model(self):
#         inst = Instructor.objects.create(name='Rachel Apone')
#         self.assertEquals(str(inst), 'Rachel Apone')

#     def test_section_model(self):
#         inst = Instructor(name='Rachel Apone')
#         inst.save()
#         sect = Section.objects.create(instructor=inst, course_number='10309',
#                                       semester_code='1228', course_section="001",
#                                     subject="ANTH",
#                                     catalog_number="1010",
#                                     description="Introduction to Anthropology",
#                                     units="3",
#                                     component="LEC",
#                                     class_capacity=25,
#                                     wait_list=0,
#                                     wait_cap=30,
#                                     enrollment_total=23,
#                                     enrollment_available=2,
#                                     topic="")
#         self.assertEquals(str(sect), '10309')

    # def test_meeting_model(self):
    #     inst = Instructor(name='Rachel Apone')
    #     inst.save()
    #     sect = Section(instructor=inst, course_number='10309',
    #                                   semester_code='1228', course_section="001",
    #                                 subject="ANTH",
    #                                 catalog_number="1010",
    #                                 description="Introduction to Anthropology",
    #                                 units="3",
    #                                 component="LEC",
    #                                 class_capacity=25,
    #                                 wait_list=0,
    #                                 wait_cap=30,
    #                                 enrollment_total=23,
    #                                 enrollment_available=2,
    #                                 topic="")
    #     sect.save()
    #     meet = Meeting.objects.create(section=sect, days="TuTh",
    #                                 start_time="11.00.00.000000-05:00",
    #                                 end_time="12.15.00.000000-05:00",
    #                                 facility_description="Clemons Library 320")
    #     self.assertEquals(str(meet), sect + "TuTh")