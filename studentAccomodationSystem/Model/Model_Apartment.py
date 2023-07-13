from BackEnd.Backend_Apartment import Backend_Apartment as apar_backend


class Model_Apartment(object):
    def __init__(self, application_items):
        self._apartment_type = 'apartment_ids'
        self.create_apartments(application_items)
    
    @property
    def apartment_type(self):
        return self._apartment_type

    @apartment_type.setter
    def apartment_type(self, new_apartment_type):
        self._apartment_type = new_apartment_type
    
    # create function
    def create_apartment(self,apartment_no, accommodation_no, apartment_type, address, counts):
        apar_backend.create_apartmentid(apartment_no, accommodation_no, apartment_type, address, counts)

    def create_apartments(self, apartments):
        apar_backend.create_apartmentids(apartments)

    # read function

    def read_all_apartments(self):
        return apar_backend.read_apartmentids()
        
    def read_apartments_in_accommodation(self, accommodation_no):
        return apar_backend.read_apartments_in_accommodation(accommodation_no)