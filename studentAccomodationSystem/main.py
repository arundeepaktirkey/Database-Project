from Controller.AccommodationController import AccommodationController as acc_cont
from Controller.UserController import UserController as user_cont
from Controller.HomeController import HomeController as home_cont
from Controller.BookingController import BookingController as book_cont

from Model.Model_Accommodation import Model_Accommodation 
from Model.Model_Apartment import Model_Apartment
from Model.User import User
from Model.Student import Student
from Model.Model_Apartment import Model_Apartment
from Model.Model_Room import Model_Room

from View.View_Accommodation import View_Accommodation
from View.Login import Login
from View.Home import Home
from View.Booking import Booking

def main():
    ####    Implementation of inheritance is in BackEnd > Backend_Apartment and BackEnd > Backend_Rooms
    ####    Whereas BackEnd_Accommodation is parent class, Backend_Apartment and BackEnd_Rooms are child class
    accommodationids = [
        {'accommodation_no': 1, 'name': 'Agatha', 'address': 'Bridge Street'},
        {'accommodation_no': 2, 'name': 'Christopher', 'address': 'Collin Street'},
        {'accommodation_no': 3, 'name': 'Darley', 'address': 'Darley Street'}
    ]

    userids = [
        {'student_no':100612450, 'username':'arunblaze10', 'password': '1234'}
    ]

    studentids = [
        {'student_no':100612450, 'name':'Arun Blaze', 'address':'derby,england', 'has_room':0, 'registration_date':'06/01/2023' },
        {'student_no':100612751, 'name':'Mattew Copper', 'address':'derby,england', 'has_room':0, 'registration_date':'06/01/2023' }
    ]

    apartmentids = [
        {'apartment_no':1, 'accommodation_no':1, 'apartment_type':'En-suite', 'address' : 'A' , 'counts': 16 },
        {'apartment_no':2, 'accommodation_no':1, 'apartment_type':'Studio', 'address' : 'B' , 'counts': 30 },
        {'apartment_no':3, 'accommodation_no':1, 'apartment_type':'Standard','address' : 'C' , 'counts': 40 },
        {'apartment_no':4, 'accommodation_no':2, 'apartment_type':'En-suite', 'address' : 'D', 'counts': 30 },
        {'apartment_no':5, 'accommodation_no':2, 'apartment_type':'Studio', 'address' : 'E' , 'counts': 40 },
        {'apartment_no':6, 'accommodation_no':2, 'apartment_type':'Standard','address' : 'F' , 'counts': 50 },
        {'apartment_no':7, 'accommodation_no':3, 'apartment_type':'En-suite','address' : 'G' , 'counts': 40 },
        {'apartment_no':8, 'accommodation_no':3, 'apartment_type':'Standard', 'address' : 'H' , 'counts': 60 }
    ]

    roomids = [
        {'room_no': 1, 'rent_per_semester': 3000,'status': 'B','accommodation_no': 1, 'apartment_no':1},
        {'room_no': 2, 'rent_per_semester': 3000,'status': 'B','accommodation_no': 1, 'apartment_no':1},
        {'room_no': 3, 'rent_per_semester': 3000,'status': 'B','accommodation_no': 1, 'apartment_no':1},
        {'room_no': 4, 'rent_per_semester': 3000,'status': 'B','accommodation_no': 1, 'apartment_no':1},
        {'room_no': 5, 'rent_per_semester': 3000,'status': 'A','accommodation_no': 1, 'apartment_no':1},
        {'room_no': 6, 'rent_per_semester': 3000,'status': 'A','accommodation_no': 1, 'apartment_no':1},
        {'room_no': 7, 'rent_per_semester': 3000,'status': 'A','accommodation_no': 1, 'apartment_no':1},
        {'room_no': 8, 'rent_per_semester': 3000,'status': 'A','accommodation_no': 1, 'apartment_no':1},
        {'room_no': 9, 'rent_per_semester': 3000,'status': 'A','accommodation_no': 1, 'apartment_no':1},
        {'room_no': 10, 'rent_per_semester': 3000,'status': 'A','accommodation_no': 1, 'apartment_no':1},
        {'room_no': 11, 'rent_per_semester': 3000,'status': 'A','accommodation_no': 1, 'apartment_no':1},
        {'room_no': 12, 'rent_per_semester': 3000,'status': 'A','accommodation_no': 1, 'apartment_no':1},
        {'room_no': 13, 'rent_per_semester': 3000,'status': 'A','accommodation_no': 1, 'apartment_no':1},
        {'room_no': 14, 'rent_per_semester': 3000,'status': 'A','accommodation_no': 1, 'apartment_no':1},
        {'room_no': 15, 'rent_per_semester': 3000,'status': 'A','accommodation_no': 1, 'apartment_no':1},
        {'room_no': 16, 'rent_per_semester': 3000,'status': 'A','accommodation_no': 1, 'apartment_no':1},
        {'room_no': 17, 'rent_per_semester': 2600,'status': 'B','accommodation_no': 1, 'apartment_no':2},
        {'room_no': 18, 'rent_per_semester': 2600,'status': 'A','accommodation_no': 1, 'apartment_no':2},
        {'room_no': 19, 'rent_per_semester': 2600,'status': 'A','accommodation_no': 1, 'apartment_no':2},
        {'room_no': 20, 'rent_per_semester': 2600,'status': 'A','accommodation_no': 1, 'apartment_no':2},
        {'room_no': 21, 'rent_per_semester': 2000,'status': 'B','accommodation_no': 1, 'apartment_no':3},
        {'room_no': 22, 'rent_per_semester': 2000,'status': 'A','accommodation_no': 1, 'apartment_no':3},
        {'room_no': 23, 'rent_per_semester': 2000,'status': 'A','accommodation_no': 1, 'apartment_no':3},
        {'room_no': 24, 'rent_per_semester': 2000,'status': 'A','accommodation_no': 1, 'apartment_no':3},
        {'room_no': 25, 'rent_per_semester': 2900,'status': 'B','accommodation_no': 2, 'apartment_no':4},
        {'room_no': 26, 'rent_per_semester': 2900,'status': 'A','accommodation_no': 2, 'apartment_no':4},
        {'room_no': 27, 'rent_per_semester': 2900,'status': 'A','accommodation_no': 2, 'apartment_no':4},
        {'room_no': 28, 'rent_per_semester': 2500,'status': 'A','accommodation_no': 2, 'apartment_no':5},
        {'room_no': 29, 'rent_per_semester': 2000,'status': 'A','accommodation_no': 2, 'apartment_no':6},
        {'room_no': 30, 'rent_per_semester': 2700,'status': 'B','accommodation_no': 3, 'apartment_no':7},
        {'room_no': 31, 'rent_per_semester': 2700,'status': 'A','accommodation_no': 3, 'apartment_no':7},
        {'room_no': 32, 'rent_per_semester': 1800,'status': 'B','accommodation_no': 3, 'apartment_no':8},
        {'room_no': 33, 'rent_per_semester': 1800,'status': 'A','accommodation_no': 3, 'apartment_no':8}
    ]
    # Accommodation Controller
    accommodation_ctrl = acc_cont(Model_Accommodation(accommodationids), View_Accommodation())
    

    counter = 0
    student_no = 0
    while True:
        # User Controller
        login = user_cont(User(userids),Login())

        # get logged username from below
        username = login.get_credentials('username')
        password = login.get_credentials('password')

        inputdata = login.get_inputdata()

        if inputdata == 1:
            login.check_userid(username=username,password=password)
            break
        elif inputdata == 2 and counter == 0 :    
            std_no = login.get_credentials('student_no')
            student_no = std_no
            login.insert_userid(student_no=student_no, username=username, password=password)
        elif counter >= 1:
            break
        else:
            print(inputdata)
            print(counter)
            print("exceeded counter or input wrong !!!")
            break
        counter = counter + 1

    # Home Controller
    home = home_cont(Home(user = username))

    returnkey = home.transfering_controller()

    if returnkey == 2:
        book = book_cont(Student(studentids),Model_Accommodation(accommodationids), Model_Apartment(apartmentids), Model_Room(roomids),Booking())
        book.read_apartments()

        home = home_cont(Home(user = username))
        returnkey = home.transfering_controller()
        




    # booking Controller
    book = book_cont(Student(studentids),Model_Accommodation(accommodationids), Model_Apartment(apartmentids), Model_Room(roomids),Booking())

    if inputdata == 2:
        book.write_user_deails(student_no)
        
    info = book.get_user_details(username = username,userid= userids, studentid=studentids)
    
    student_no = list(info.values())[0]
    name = list(info.values())[1]
    address = list(info.values())[2]
    has_room = list(info.values())[3]
    registration_date = list(info.values())[4]
    
    # show student details
    book.read_student_info(user= username, student_no=student_no, name=name, address=address, has_room=has_room, registration_date=registration_date)
    
    # show all accommodations
    selected_accommodation = book.read_accommodation()

    # show room types from selected accommodation
    selected_apartment = book.read_select_accommodation(selected_accommodation = selected_accommodation)

    # show room price and confirm booking
    confirmation = book.read_room_price(selected_accommodation = selected_accommodation, selected_apartment = selected_apartment)

    # Book room for student
    if confirmation == 'Y' or confirmation == 'y':
        book.create_transactions(student_no, name, address, selected_accommodation, selected_apartment, apartmentids, roomids)
    else:
        exit()

    


if __name__ == '__main__':
        main()