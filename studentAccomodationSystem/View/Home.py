'''
Welcome to Student Accommodation System
                                            Logged as Arun
1. Booking
2. Check Accommodation -> Booking
3. Exit
                                         
'''


class Home():
    def __init__(self, user):
        self._user = user
    
    def logged_Student(self):
        print("******************************************")
        print("\t\t\t WELCOME TO Student Accommodation System\n")
        print('\t\t\t\t\t\t Logged as {}'.format(self._user))
        print("\t\t\t 1. Booking\n")
        print("\t\t\t 2. Check Accommodation\n")
        print("\t\t\t 3. Exit\n")
        inputdata = int(input("->"))
        return inputdata
