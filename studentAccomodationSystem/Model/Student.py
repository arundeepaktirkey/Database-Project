from BackEnd.Backend_Student import Backend_Student as student_backend


class Student(object):

    def __init__(self, application_items):
        self._studentid_type = 'StudentId'
        self.create_studentids(application_items)

    @property
    def studentid_type(self):
        return self._studentid_type

    @studentid_type.setter
    def studentid_type(self, new_studentid_type):
        self._studentid_type = new_studentid_type

    def create_studentid(self, student_no, SName, SAddress, has_room, registration_date):
        student_backend.create_studentid(student_no, SName, SAddress, has_room, registration_date)

    def create_studentids(self, userid):
        student_backend.create_studentids(userid)

    def read_student_no(self, student_no):
        return student_backend.read_student_no(student_no)

    def read_sname(self, sname):
        return student_backend.read_sname(sname)  

    def read_saddress(self, saddress):
        return student_backend.read_saddress(saddress)
    
    def read_has_room(self, room):
        return student_backend.read_has_room(room)
    
    def read_date(self, date):
        return student_backend.read_date(date)