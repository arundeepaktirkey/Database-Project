import mvc_exceptions as mvc_exc

from BackEnd.Backend_Accommodation import Backend_Accommodation as backend_acc

class Backend_Apartment(backend_acc):

    apartmentids = list()

    # create function
    def create_apartmentids(app_apartment):
        global apartmentids
        apartmentids = app_apartment

    def create_apartmentid(apartment_no, accommodation_no, apartment_type, address, counts):
        global apartmentids
        results = list(filter(lambda x: x['accommodation_no'] == accommodation_no, apartmentids))
        if results:
            raise mvc_exc.ItemAlreadyStored('"{}" already stored!'.format(accommodation_no))
        else:
            apartmentids.append({'apartment_no':apartment_no, 'accommodation_no':accommodation_no, 'apartment_type':apartment_type, 'address': address, 'counts': counts })


    # read function
    def read_apartments_in_accommodation(accommodation_no):
        global apartmentids
        mylist = list(filter(lambda x: x['accommodation_no'] == accommodation_no, apartmentids))
        if mylist:
            return mylist
        else:
            raise mvc_exc.ItemNotStored('Can\'t read "{}" because it\'s not stored'.format(accommodation_no))
    
    def read_apartment_no(apartment_no):
        global apartmentids
        mylist = list(filter(lambda x: x['apartment_no'] == apartment_no, apartmentids))
        if mylist:
            return apartment_no
        else:
            raise mvc_exc.ItemNotStored('Can\'t read "{}" because it\'s not stored'.format(apartment_no))


    def read_accommodation_no(accommodation_no):
        return backend_acc.Backend_Accommodation.read_accommodation_no(accommodation_no= accommodation_no)

    def read_types(types):
        global apartmentids
        mylist = list(filter(lambda x: x['types'] == types, apartmentids))
        if mylist:
            return types
        else:
            raise mvc_exc.ItemNotStored('Can\'t read "{}" because it\'s not stored'.format(types))
    
    def read_address(address):
        global apartmentids
        mylist = list(filter(lambda x: x['address'] == address, apartmentids))
        if mylist:
            return address
        else:
            raise mvc_exc.ItemNotStored('Can\'t read "{}" because it\'s not stored'.format(address))
    


    def read_counts(counts):
        global apartmentids
        mylist = list(filter(lambda x: x['counts'] == counts, apartmentids))
        if mylist:
            return counts
        else:
            raise mvc_exc.ItemNotStored('Can\'t read "{}" because it\'s not stored'.format(counts))
    
    def read_apartmentids():
        global apartmentids
        return [x for x in apartmentids]
