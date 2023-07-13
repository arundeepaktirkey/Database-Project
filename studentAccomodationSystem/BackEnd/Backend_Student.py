import mvc_exceptions as mvc_exc

class Backend_Student():
        
    studentids = list() # global variable where we keep the data

    # create function
    def create_studentids(app_accommodations):
        global studentids
        studentids = app_accommodations

    def create_studentid(student_no, SName, SAddress, has_room, registration_date):
        global studentids
        results = list(filter(lambda x: x['student_no'] == student_no, studentids))
        if results:
            raise mvc_exc.ItemAlreadyStored('"{}" already stored!'.format(SName))
        else:
            studentids.append({'student_no': student_no, 'name':SName, 'address':SAddress, 'has_room':has_room, 'registration_date':registration_date })



    # read function
    def read_student_no(student_no):
        global studentids
        mylist = list(filter(lambda x: x['student_no'] == student_no, studentids))
        if mylist:
            return student_no
        else:
            raise mvc_exc.ItemNotStored('Can\'t read "{}" because it\'s not stored'.format(student_no))
    
    def read_sname(name):
        global studentids
        mylist = list(filter(lambda x: x['name'] == name, studentids))
        if mylist:
            return name
        else:
            raise mvc_exc.ItemNotStored('Can\'t read "{}" because it\'s not stored'.format(name))
    
    def read_saddress(address):
        global studentids
        mylist = list(filter(lambda x: x['address'] == address, studentids))
        if mylist:
            return address
        else:
            raise mvc_exc.ItemNotStored('Can\'t read "{}" because it\'s not stored'.format(address))
    
    def read_has_room(has_room):
        global studentids
        mylist = list(filter(lambda x: x['has_room'] == has_room, studentids))
        if mylist:
            return has_room
        else:
            raise mvc_exc.ItemNotStored('Can\'t read "{}" because it\'s not stored'.format(has_room))
    
    def read_date(date):
        global studentids
        mylist = list(filter(lambda x: x['registration_date'] == date, studentids))
        if mylist:
            return date
        else:
            raise mvc_exc.ItemNotStored('Can\'t read "{}" because it\'s not stored'.format(date))
    
    def read_studentids():
        global studentids
        return [x for x in studentids]