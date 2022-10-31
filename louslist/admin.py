from django.contrib import admin
from .models import Profile, Instructor, Section, Meeting

admin.site.register(Profile)
admin.site.register(Instructor)
admin.site.register(Section)
admin.site.register(Meeting)