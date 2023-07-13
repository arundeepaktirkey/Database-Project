import mvc_exceptions as mvc_exc

class AccommodationController(object):

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def show_accommodations(self, bullet_points=False):
        accommodations = self.model.read_accommodations()
        accommodation_type = self.model.accommodation_type
        if bullet_points:
            self.view.show_bullet_point_list(accommodation_type, accommodations)
        else:
            self.view.show_number_point_list(accommodation_type, accommodations)

    def show_accommodation(self, accommodation_name):
        try:
            accommodation = self.model.read_accommodation(accommodation_name)
            accommodation_type = self.model.accommodation_type
            self.view.show_accommodation(accommodation_type, accommodation_name, accommodation)
        except mvc_exc.ItemNotStored as e:
            self.view.display_missing_accommodation_error(accommodation_name, e)

    def insert_accommodation(self, acc_no, name, address):
        assert name != '' , 'name of accommodation should be there'
        assert address != '' , 'address should be there'
        accommodation_type = self.model.accommodation_type
        try:
            self.model.create_accommodation(acc_no, name, address)
            self.view.display_accommodation_stored(name, accommodation_type)
        except mvc_exc.ItemAlreadyStored as e:
            self.view.display_accommodation_already_stored_error(name, accommodation_type, e)

    def update_accommodation(self, acc_no, name, address):
        assert name != '' , 'name of accommodation should be there'
        assert address != '' , 'address of accommodation should be there'
        accommodation_type = self.model.accommodation_type

        try:
            older = self.model.read_accommodation(name)
            self.model.update_accommodation(acc_no, name, address)
            self.view.display_accommodation_updated(
                name, older['name'], older['address'], name, address)
        except mvc_exc.ItemNotStored as e:
            self.view.display_accommodation_not_yet_stored_error(name, accommodation_type, e)
            # if the accommodation is not yet stored and we performed an update, we have
            # 2 options: do nothing or call insert_accommodation to add it.
            # self.insert_accommodation(name, price, quantity)

    def update_accommodation_type(self, new_accommodation_type):
        old_accommodation_type = self.model.accommodation_type
        self.model.accommodation_type = new_accommodation_type
        self.view.display_change_accommodation_type(old_accommodation_type, new_accommodation_type)

    def delete_accommodation(self, name):
        accommodation_type = self.model.accommodation_type
        try:
            self.model.delete_accommodation(name)
            self.view.display_accommodation_deletion(name)
        except mvc_exc.ItemNotStored as e:
            self.view.display_accommodation_not_yet_stored_error(name, accommodation_type, e)
