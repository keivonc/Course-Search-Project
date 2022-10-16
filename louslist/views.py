from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.core import serializers
from .api_loader import *
from .models import Section


def load_api_by_dept(request, dept):
    filename = 'JSON/' + dept + '.json'
    load_json_file(filename)
    return HttpResponse("I just read a whole lot of JSON files")

def find_all_by_dept(request, dept):
    sections = Section.objects.filter(subject=dept)
    sections_serialized = serializers.serialize('json', sections)
    return HttpResponse("I just read a whole lot of JSON files")

def find_all_by_dept_v2(request, dept):
    sections = Section.objects.filter(subject=dept)
    return render(request, 'findallbydept.html', {'sections': sections})