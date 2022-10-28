from curses.ascii import HT
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.core import serializers
from .api_loader import *
from .models import Section, Meeting
from django.contrib.auth import get_user_model
from .forms import UserUpdateForm
from django.contrib import messages

def load_api(request):
    get_all_json_files()
    return HttpResponse("I just read a whole lot of JSON files")

def load_api_by_dept(request, dept):
    filename = 'JSON/' + dept + '.json'
    load_json_file(filename)
    return HttpResponse("I just read a whole lot of JSON files")

def find_all_by_dept(request, dept):
    sections = Section.objects.filter(subject=dept)
    sections_serialized = serializers.serialize('json', sections)
    return HttpResponse(sections_serialized, content_type = 'application/json')

def find_all_by_dept_v2(request, dept):
    filename = "JSON/" + dept + ".json"
    load_json_file(filename)
    sections = Section.objects.filter(subject=dept).distinct('description', 'catalog_number')
    sections = sections.order_by('catalog_number')
    return render(request, 'findallbydept.html', {'sections': sections, "department": dept})

def info(request, dept, desc, cn):
    filename = "JSON/" + dept + ".json"
    load_json_file(filename)
    sections = Section.objects.filter(description=desc, catalog_number=cn)
    meetings = Meeting.objects.all()
    return render(request, 'des.html', {'sections': sections, 'meetings': meetings, "department": dept, "description": desc, 'catalog_number': cn})

def profile(request, username):
    if request.method == 'POST':
        user = request.user
        form = UserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user_form = form.save()

            messages.success(request, f'{user_form}, Your profile has been updated!')
            return HttpResponseRedirect('profile', user_form.username)

        for error in list(form.errors.values()):
            messages.error(request, error)

    user = get_user_model().objects.filter(username=username).first()
    if user:
        form = UserUpdateForm(instance=user)
        # form.fields['description'].widget.attrs = {'rows': 1}
        return render(request, 'profile.html', context={'form': form})

    return HttpResponseRedirect("homepage")
