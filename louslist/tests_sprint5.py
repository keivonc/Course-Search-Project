from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse 
from louslist.models import Instructor, Section, Meeting, Profile

class Sprint5Tests(TestCase):

#def test_deptpage_url(self):
#         response = reverse('dept_page', kwargs={'dept': 'ANTH'})
#         self.assertEqual(response, '/departments/ANTH')

# def test_deptpage(self):
#     #     response = self.client.get(reverse('dept_page', kwargs={'dept': 'ANTH'}))
#     #     self.assertEqual(response.status_code, 200)

    def test_users_home_url(self):
        response = self.client.get(reverse('users-home'))
        self.assertEqual(response.status_code, 200)

    def test_search_users_home_view_url(self):
        response = self.client.get(reverse('search_users_home_view'))
        self.assertEqual(response.status_code, 200)

    def test_register_url(self):
        response = self.client.get(reverse('users-register'))
        self.assertEqual(response.status_code, 200)

    def test_login_url(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_logout_url(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 200)

    def test_logging_in(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        login = self.client.login(username='testuser', password='12345')

    def test_logging_out(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        login = self.client.logout()

    # def test_search_users_results_view_url(self):
    #     response = self.client.get(reverse('search_users_results_view'))
    #     self.assertEqual(response.status_code, 200)

    # def test_profile_url(self):
    #     response = self.client.get(reverse('users-profile'))
    #     self.assertEqual(response.status_code, 200)

    # def test_password_change_url(self):
    #     response = self.client.get(reverse('password_change'))
    #     self.assertEqual(response.status_code, 200)

    # def test_saved_courses_url(self):
    #     response = self.client.get(reverse('saved_courses'))
    #     self.assertEqual(response.status_code, 200)

    # def test_profile_model(self):
    #     user = User.objects.create_user(username='testuser', password='12345')
    #     prof = Profile.objects.create(user=user, major='linguistics', year='third', bio='test', saved_courses='[]')
    #     self.assertEquals(prof, "testuser,linguistics,third,[]")


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


    # path('admin/', admin.site.urls),
    # path('', TemplateView.as_view(template_name="home.html"), name='home'),
    # path('search/', TemplateView.as_view(template_name="search_page.html"), name='users-home'),
    # path('search/users/', views.SearchUsersHomeView.as_view(), name='search_users_home_view'),
    # path('search/users/results', views.SearchUsersResultsView.as_view(), name='search_users_results_view'),
    # path('departments/', views.get_departments, name='all_departments'),
    # path('departments/<str:dept>', views.find_all_by_dept_v2, name='dept_page'),
    # path('departments/<str:dept>/<str:cn>/<str:desc>/info', views.info, name='course_page'),
    # path('register/', views.RegisterView.as_view(), name='users-register'),
    # path('profile/', views.profile, name='users-profile'),
    # path('login/', views.CustomLoginView.as_view(redirect_authenticated_user=True, template_name='login.html',
    #                                        authentication_form=views.LoginForm), name='login'),
    # path('search/logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    # path('password-change/', views.ChangePasswordView.as_view(), name='password_change'),
    # path('search/saved_courses/', views.get_saved_courses, name='saved_courses'),
    # re_path(r'^oauth/', include('social_django.urls', namespace='social')),