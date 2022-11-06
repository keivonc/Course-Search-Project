from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View
from django.views.generic import TemplateView, ListView
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.core import serializers
from django.urls import reverse_lazy
from django.db.models import F, Q

from .api_loader import *
from .models import Section, Meeting, Profile, User
from .forms import RegisterForm, LoginForm, UpdateUserForm, UpdateProfileForm
# import os

@login_required
def load_api(request):
    get_all_json_files()
    return HttpResponse("I just read a whole lot of JSON files")

@login_required
def load_api_by_dept(request, dept):
    filename = 'JSON/' + dept + '.json'
    load_json_file(filename)
    return HttpResponse("I just read a whole lot of JSON files")

@login_required
def get_departments(request):
    sections = Section.objects.all().values('subject').distinct()
    sections = sections.order_by('subject')
    return render(request, 'departments.html', {'sections': sections})

@login_required
def find_all_by_dept(request, dept):
    sections = Section.objects.filter(subject=dept)
    sections_serialized = serializers.serialize('json', sections)
    return HttpResponse(sections_serialized, content_type = 'application/json')

@login_required
def find_all_by_dept_v2(request, dept):
    # filename = "JSON/" + dept + ".json"
    # load_json_file(filename)
    # for f in os.listdir('JSON'):
    #     load_json_file('JSON/' + f)
    # for query in Meeting.objects.all():
    #     if query.start_time:
    #         if int(query.start_time[0:2]) > 12:
    #             query.start_time = str(int(query.start_time[0:2]) - 12) + ":" + query.start_time[3:5] + " PM"
    #             query.save()
    #         else: 
    #             query.start_time = str(int(query.start_time[0:2])) + ":" + query.start_time[3:5] + " AM"
    #             query.save()
     # for query in Meeting.objects.all():
    #     if query.end_time:
    #         if int(query.end_time[0:2]) > 12:
    #             query.end_time = str(int(query.end_time[0:2]) - 12) + ":" + query.end_time[3:5] + " PM"
    #             query.save()
    #         else: 
    #             query.end_time = str(int(query.end_time[0:2])) + ":" + query.end_time[3:5] + " AM"
    #             query.save()
    sections = Section.objects.filter(subject=dept).distinct('description', 'catalog_number')
    sections = sections.order_by('catalog_number')
    if request.POST.get('add_to_saved'):
        profile = get_object_or_404(Profile, user=request.user)
        if not profile.saved_courses:
            profile.saved_courses = [request.POST.get("add_to_saved")]
        else:
            profile.saved_courses += [request.POST.get('add_to_saved')]
        profile.save(update_fields=["saved_courses"])
    return render(request, 'findallbydept.html', {'sections': sections, "department": dept})

@login_required
def info(request, dept, desc, cn):
    # filename = "JSON/" + dept + ".json"
    # load_json_file(filename)
    # sections = Section.objects.filter(description=desc, catalog_number=cn)
    # meetings = Meeting.objects.all()
    # return render(request, 'des.html', {'sections': sections, 'meetings': meetings, "department": dept, "description": desc, 'catalog_number': cn})
    meetings = Meeting.objects.filter(section__description=desc, section__catalog_number=cn)
    return render(request, 'des.html', {'meetings': meetings, "department": dept, "description": desc, 'catalog_number': cn})

def login(request):
    return render(request, 'login.html')

@login_required
def get_saved_courses(request):
    saved_courses = Profile.objects.filter(user__username=request.user.username).values('saved_courses')
    saved_courses1 = saved_courses[0]['saved_courses']
    sections = Section.objects.none()
    for section in saved_courses1:
        section1 = section.split(",")
        sections |= Section.objects.filter(subject=section1[0], catalog_number=section1[1][1:], description=section1[2][1:-1]).distinct('catalog_number', 'description')
    sections = sections.order_by('catalog_number')
    return render(request, 'saved_courses.html', {'sections': sections})

class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'register.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(to='/search')
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect(to='login')
        return render(request, self.template_name, {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'profile.html', {'user_form': user_form, 'profile_form': profile_form})

class CustomLoginView(LoginView):
    form_class = LoginForm
    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')
        if not remember_me:
            self.request.session.set_expiry(0)
            self.request.session.modified = True
        return super(CustomLoginView, self).form_valid(form)

class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('users-home')


# https://learndjango.com/tutorials/django-search-tutorial
class SearchUsersHomeView(TemplateView):
    template_name = 'search_users_page.html'

class SearchUsersResultsView(ListView):
    model=Profile
    template_name= 'search_users_results.html'

    def get_context_data(self,**kwargs):
        context = super(SearchUsersResultsView,self).get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get("q")
        return context

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Profile.objects.filter(
            ((Q(user__username__icontains=query) | Q(user__first_name__icontains=query) | Q(user__last_name__icontains=query)) & Q(user__is_staff=False))
        )
        return object_list
    
