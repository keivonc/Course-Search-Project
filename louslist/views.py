from curses.ascii import HT
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.core import serializers
from .api_loader import *
from .models import Section, Meeting

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
    sections = Section.objects.filter(subject=dept).distinct('description')
    return render(request, 'findallbydept.html', {'sections': sections, "department": dept})

def info(request, dept, desc):
    filename = "JSON/" + dept + ".json"
    load_json_file(filename)
    sections = Section.objects.filter(description=desc)
    meetings = Meeting.objects.all()
    return render(request, 'des.html', {'sections': sections, 'meetings': meetings, "department": dept, "description": desc})

# order by catalog number not description