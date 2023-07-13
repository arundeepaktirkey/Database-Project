from BackEnd.Backend_Room import Backend_Room as room_backend


class Model_Room(object):
    def __init__(self, application_items):
        self._room_type = 'apartment_ids'
        self.create_rooms(application_items)
    
    @property
    def room_type(self):
        return self._room_type

    @room_type.setter
    def room_type(self, new_room_type):
        self._room_type = new_room_type
    
    # create function
    def create_room(room_no, rent_per_semester, status,accommodation_no, apartment_no):
        room_backend.create_roomid(room_no, rent_per_semester, status,accommodation_no, apartment_no)

    def create_rooms(self, rooms):
        room_backend.create_roomids(rooms)

    # read function
    def read_rooms(self, accommodation_no, apartment_no):
        return room_backend.read_rooms(accommodation_no, apartment_no)
    
    
    def read_all_rooms(self, accommodation_no):
        return room_backend.read_all_rooms(accommodation_no)