from BackEnd.Backend_Accommodation import Backend_Accommodation as acc_backend

class Model_Accommodation(object):
    def __init__(self, application_items):
        self._accommodation_type = 'accomodation'
        self.create_accommodations(application_items)
    
    @property
    def accommodation_type(self):
        return self._accommodation_type

    @accommodation_type.setter
    def accommodation_type(self, new_accommodation_type):
        self._accommodation_type = new_accommodation_type
    
    def create_accommodation(self,acc_no, name, address):
        acc_backend.create_accommodation(acc_no, name, address)

    def create_accommodations(self, accommodations):
        acc_backend.create_accommodations(accommodations)

    def read_accommodation(self, name):
        return acc_backend.read_accommodation(name)

    def read_accommodations(self):
        return acc_backend.readAll_accommodation()
    
    def update_accommodation(self, acc_no, name, address):
        acc_backend.update_accommodation(acc_no, name, address)

    def delete_accommodation(self, name):
        acc_backend.delete_accommodation(name)
    



    

