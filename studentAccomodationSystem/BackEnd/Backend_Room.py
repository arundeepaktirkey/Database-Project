import mvc_exceptions as mvc_exc
from BackEnd.Backend_Apartment import Backend_Apartment

class Backend_Room(Backend_Apartment):

    roomids = list()

    # create rooms function
    def create_roomids(app_rooms):
        global roomids
        roomids = app_rooms

    def create_roomid(room_no, rent_per_semester, status,accommodation_no, apartment_no):
        global roomids
        results = list(filter(lambda x: x['room_no'] == room_no, roomids))
        if results:
            raise mvc_exc.ItemAlreadyStored('"{}" already stored!'.format(room_no))
        else:
            roomids.append({'room_no': room_no, 'rent_per_semester': rent_per_semester,'status': status,'accommodation_no': accommodation_no, 'apartment_no':apartment_no})


    # read functions
    def read_room_no(room_no):
        global roomids
        mylist = list(filter(lambda x: x['room_no'] == room_no, roomids))
        if mylist:
            return room_no
        else:
            raise mvc_exc.ItemNotStored('Can\'t read "{}" because it\'s not stored'.format(room_no))
    
    def read_rent_per_semester(rent_per_semester):
        global roomids
        mylist = list(filter(lambda x: x['rent_per_semester'] == rent_per_semester, roomids))
        if mylist:
            return rent_per_semester
        else:
            raise mvc_exc.ItemNotStored('Can\'t read "{}" because it\'s not stored'.format(rent_per_semester))
    
    def read_status(status):
        global roomids
        mylist = list(filter(lambda x: x['status'] == status, roomids))
        if mylist:
            return status
        else:
            raise mvc_exc.ItemNotStored('Can\'t read "{}" because it\'s not stored'.format(status))
    


    def read_accommodation_no(accommodation_no):
        return super().read_accommodation_no()

    def read_apartment_no(apartment_no):
        return super().read_apartment_no(apartment_no)   

    def read_rooms(accommodation_no, apartment_no):
        global roomids
        mylist = list(filter(lambda x: x['status'] == 'A' and x['accommodation_no'] == accommodation_no and x['apartment_no'] == apartment_no, roomids))
        if mylist:
            return mylist
        else:
            raise mvc_exc.ItemNotStored('Can\'t read room because it\'s not stored')

    def read_all_rooms(accommodation_no):
        global roomids
        mylist = list(filter(lambda x: x['status'] == 'A' and x['accommodation_no'] == accommodation_no , roomids))
        if mylist:
            return mylist
        else:
            raise mvc_exc.ItemNotStored('Can\'t read room because it\'s not stored')

    def read_roomids():
        global roomids
        return [x for x in roomids]