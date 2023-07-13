'''

Welcome to Student Accommodation System

Enter Username
ArunDeep

Enter Password
asder

'''
from Controller.UserController import UserController as user_obj
import os

class Login():
    print("******************************************")
    print("\t\t\t WELCOME TO Student Accommodation System\n")
    print("\t\t 1. Login\n")
    print("\t\t 2. Register\n")
    inputdata = int(input('->'))
    if inputdata == 1:
        print("\t\t\t Enter Username\n")
        username = input("->")
        assert username !=  '' , 'username should not be empty'
        print("\t\t\t Enter Password\n")
        password = input("->")
        assert password !=  '' , 'password should not be empty'
    elif inputdata == 2:
        print("\t\t\t WELCOME TO Student Accommodation System\n")
        print("\t\t\t\t\t Student Registration")
        print("\t Enter Student_no\n")
        student_no = int(input("->"))
        assert student_no !=  0 , 'student no should not be empty'
        print("\t Enter Username\n")
        username = input("->")
        assert username !=  '' , 'username should not be empty'
        print("\t Enter Password\n")
        password = input("->")
        assert password !=  '' , 'password should not be empty'

    def get_inputdata(self):
        return self.inputdata

    def get_student_no(self):
        return self.student_no

    def get_username(self):
       return self.username
    
    def get_password(self):
        return self.password

    @staticmethod
    def display_userid_stored(student_no):
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print('{} Registered Successful'
              .format(student_no))
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    
    @staticmethod
    def display_all_userids(userids):
        print('\t\t\t --- USERIDS ---')
        for i, userid in enumerate(userids):
            print('{}. Student No :{}  Username : {}'.format(i+1, userid['student_no'], userid['username']))

    @staticmethod
    def display_userid_validation(userid):
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print('Logged as {}'
              .format(userid))
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

    @staticmethod
    def display_userid_validation_error():
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print('Incorrect Credentials, Please check')
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

