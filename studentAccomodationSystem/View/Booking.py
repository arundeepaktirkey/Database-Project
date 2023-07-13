'''

                                            Logged as Arun
Welcome to Student Accommodation System

BOOKING ROOM
Student_no = 100614999
Student Name = Arun Blaze
Student Address = 83, bridge Street, Derby
Has_room = No
Registration_date = 13/12/2022

-SELECT ACCOMMODATION--
1. Agatha
2.Christopher
3.Darley

-SELECT ROOM TYPE-
1. En-Suite
2. Studio
3. Standard
Press 0 for Room Prices

'''
class Booking():
    
    @staticmethod
    def create_student_info():
        print("******************************************")
        print("\n \t\t STUDENT INFORMATION FORMS \n")
        studentname = input("Student Name = ")
        assert studentname !=  '' , 'student name should not be empty'
        studentaddress = input("Student Address = ")
        assert studentaddress !=  '' , 'student address should not be empty'
        return [studentname,studentaddress]

    @staticmethod
    def student_info(user,student_no, name, address, has_room, registration_date ):
        print("******************************************")
        print("\t\t\t WELCOME TO Student Accommodation System\n")
        print('\t\t\t\t Logged as {}'.format(user))
        print("\n \t\t\t STUDENT INFO \n")
        print("Student Number = {}".format(student_no))
        print("Student Name = {}".format(name))
        print("Student Address = {}".format(address))
        print("Room Availed = {}".format(has_room))
        print("Registration Date = {}".format(registration_date))
    
    @staticmethod
    def select_Accommodation(accommodations):
        print('\t\t\t --- SELECT ACCOMMODATION ---')
        for i, accommodation in enumerate(accommodations):
            print('{}. {}'.format(i+1, accommodation['name']))
        inputdata = int(input("->"))
        assert inputdata !=  0 , 'inputdata should not be zero or empty'
        return inputdata
    
    @staticmethod
    def show_apartments(apartments):
        print('\t\t\t --- ACCOMMODATION ---')
        for i, apart in enumerate(apartments):
            print('{}. Accommodation : {} , Apartment Type : {}'.format(i+1, 'Agatha'  if apart['accommodation_no'] == 1 else ('Christopher' if apart['accommodation_no'] ==2 else 'Darley') , apart['apartment_type'] ))

    @staticmethod
    def select_room_type(room_type):
        print('\t\t\t --- SELECT ROOM TYPE ---')
        for i, room_type in enumerate(room_type):
            print('{}. {}'.format(room_type['apartment_no'], room_type['apartment_type']))
        print("Press 0 for room prices")
        inputdata = int(input("->"))
        return inputdata

    @staticmethod
    def room_price(room_price):
        print('\t\t\t --- ROOM PRICE ---')
        for i, room_price in enumerate(room_price):
            print('{}. {}'.format(i+1, room_price['rent_per_semester']))
            inputdata = input(" Y or N for Booking->")
            assert inputdata !=  '' , 'inputdata should not be empty'
            return inputdata

    @staticmethod
    def room_all_price(room_price):
        print('\t\t\t --- ROOM PRICE ---')
        for i, x in enumerate(room_price):
            print('{}. Apartment : {} Price {}'.format(i+1, x['apartment_no'] ,x['rent_per_semester']))
        input("Press any key to Exit ->")

    def transaction(transactions):
        print('\t\t\t --- TRANSACTION INFO ---')
        for key,value in transactions[0].items():
            print(' {data}  {datavalue} '.format( data=key if key in ('student_no','name','student_address','rent_per_semester','room_no','apartment_type','date_from','date_to') else '' , datavalue=value if key in ('student_no','name','student_address','rent_per_semester','room_no','apartment_type','date_from','date_to') else '' ))
        input("Thank You !!!!! ->")