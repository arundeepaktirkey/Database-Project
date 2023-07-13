import mvc_exceptions as mvc_exc
from datetime import date

from Model.Transaction import Transaction

from View.Booking import Booking

class BookingController(object):

    def __init__(self, model_Student, model_Accommodation, model_Apartment, model_room, view):
        self.model_Student = model_Student
        self.model_Accommodation = model_Accommodation
        self.model_Apartment = model_Apartment
        self.model_Room = model_room
        self.view = view

    # self, student_no, name, address, has_room, registration_date
    def read_student_info(self, user,student_no, name, address, has_room, registration_date):
        # try:
        s_no = self.model_Student.read_student_no(student_no)
        s_name = self.model_Student.read_sname(name)
        s_address = self.model_Student.read_saddress(address)
        s_room = self.model_Student.read_has_room(has_room)
        s_date = self.model_Student.read_date(registration_date)

        self.view.student_info(user,s_no, s_name, s_address, s_room, s_date )
        # except Exception as e:
        #     print(e)

    def write_user_deails(self,student_no):
        student_no = student_no
        listofstudent = self.view.create_student_info()
        hasroom = 0
        registration_date = str(date.today())
        self.model_Student.create_studentid(student_no, listofstudent[0], listofstudent[1], hasroom, registration_date)



    def get_user_details(self, username, userid, studentid):
        mylist = list(filter(lambda x: x['username'] == username, userid))
        id = next(iter(mylist))
        first_key = list(id.values())[0]
        # print(first_key)
        mylist2 = list(filter(lambda x: x['student_no'] == first_key, studentid))
        # print(mylist2)
        id2 = next(iter(mylist2))
        # print(id2)
        return id2
    
    def read_accommodation(self):
        acc = self.model_Accommodation.read_accommodations()
        inputkey = self.view.select_Accommodation(acc)
        return inputkey
    
    def read_apartments(self):
        apart = self.model_Apartment.read_all_apartments()
        self.view.show_apartments(apart)
    
    # do now... working here.....
    def read_select_accommodation(self, selected_accommodation):
        apart_in_acc = self.model_Apartment.read_apartments_in_accommodation(selected_accommodation)
        inputdata = self.view.select_room_type(apart_in_acc)
        return inputdata

    def read_room_price(self, selected_accommodation, selected_apartment):
        if(selected_apartment != 0):
            room_price = self.model_Room.read_rooms(selected_accommodation, selected_apartment)
            inputdata = self.view.room_price(room_price)
        elif(selected_apartment == 0):
            room_price = self.model_Room.read_all_rooms(selected_accommodation)
            self.view.room_all_price(room_price)
            exit()
        else:
            print('Wrong entered input')
        
        if inputdata == 'N' or inputdata == 'n' :
            exit() 
        return inputdata

    def create_transactions(self, student_no, name, address, selected_accommodation, selected_apartment, apartmentids, roomids):
        transactions = Transaction.create_transactions(student_no, name, address, selected_accommodation, selected_apartment, apartmentids, roomids)
        Booking.transaction(transactions)
        