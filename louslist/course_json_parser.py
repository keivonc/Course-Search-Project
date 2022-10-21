from .models import *


class CourseJsonParser:


    def __init__(self, json_object) -> None:
        self.json_object = json_object

    
    def get_instructor(self):

        instructor_obj = self.json_object.get("instructor", {})
        name = instructor_obj.get("name")
        email = instructor_obj.get("email")
        if not Instructor.objects.filter(email=email).exists():
            Instructor.objects.create(name=name, email=email)
        return Instructor.objects.get(email=email)

    
    def get_section(self):
        
        instructor = self.get_instructor()
        if not instructor or not Instructor.objects.filter(email=instructor.email).exists():
            raise RuntimeError("Instructor doesn't exist")
        
        section = Section(instructor = instructor,
                            course_number=self.json_object.get("course_number"),
                            semester_code=self.json_object.get("semester_code"),
                            course_section=self.json_object.get("course_section"),
                            subject=self.json_object.get("subject"),
                            catalog_number=self.json_object.get("catalog_number"),
                            description=self.json_object.get("description"),
                            units=self.json_object.get("units"),
                            component=self.json_object.get("component"),
                            class_capacity=self.json_object.get("class_capacity"),
                            wait_list=self.json_object.get("wait_list"),
                            wait_cap=self.json_object.get("wait_cap"),
                            enrollment_total=self.json_object.get("enrollment_total"),
                            enrollment_available=self.json_object.get("enrollment_available"),
                            topic=self.json_object.get("topic", "N/A"))
        if not Section.objects.filter(course_number = section.course_number).exists():
            section.save()
        
        return Section.objects.get(course_number = section.course_number)


    def get_meetings(self):
        section = self.get_section()
        if not Section.objects.filter(course_number = section.course_number).exists():
            raise RuntimeError("Section doesn't exist and hasn't been created")
        
        if Meeting.objects.filter(section=section).exists():
            return Meeting.objects.filter(section=section)
        meetings = []
        for meeting in self.json_object.get("meetings", []):
            new_meeting = Meeting(section=section,
                                    days = meeting.get("days"),
                                    start_time = meeting.get("start_time"),
                                    end_time = meeting.get("end_time"),
                                    facility_description = meeting.get("facility_description"))
            meetings.append(new_meeting)
        
        for meeting in meetings:
            meeting.save()

        return meetings

    
    def load_all(self):
        self.get_meetings()



        



    
