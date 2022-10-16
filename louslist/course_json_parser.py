from .models import *


class CourseJsonParser:


    def __init__(self, json_object) -> None:
        self.json_object = json_object

    
    def get_instructor(self):

        instructor_obj = self.json_object.get("instructor", {})
        name = instructor_obj.get("name")
        email = instructor_obj.get("email")
        if not name or not email:
            return None
        if not Instructor.objects.filter(email=email).exists():
            Instructor.objects.create(name=name, email=email)
        return Instructor.objects.get(email=email)

    
    def get_section(self):
        
        instructor = self.get_instructor()
        if not instructor or not Instructor.objects.filter(email=instructor.email).exists():
            raise RuntimeError("Instructor doesn't exist")

        



    
