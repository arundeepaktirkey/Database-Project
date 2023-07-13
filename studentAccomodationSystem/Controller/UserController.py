import mvc_exceptions as mvc_exc

class UserController(object):

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def check_userid(self, username, password):
        try:
            u = self.model.read_username(username)
            p = self.model.read_password(password)
            
            self.view.display_userid_validation(u)
            
        except mvc_exc.ItemNotStored as e:
            self.view.display_userid_validation_error()

    def get_credentials(self, userid):
        if userid == 'username':
            return self.view.get_username()
        elif userid == 'password':
            return self.view.get_password()
        elif userid == 'student_no':
            return self.view.get_student_no()
        else:
            print('Something went wrong!!!')

    def get_inputdata(self):
        return self.view.get_inputdata()

    def insert_userid(self, student_no, username, password):
        assert student_no != '' , 'student_no should be there'
        assert username != '' , 'username should be there'
        assert password != '' , 'password should be there'
        userid_type = self.model.userid_type
        try:
            userids = self.model.create_userid(student_no, username, password)
            self.view.display_all_userids(userids)
            self.view.display_userid_stored(student_no)
        except mvc_exc.ItemAlreadyStored as e:
            self.view.display_userid_already_stored_error(student_no, userid_type, e)

    def update_userid(self, student_no, username, password):
        assert student_no != '' , 'student_no should be there'
        assert username != '' , 'username should be there'
        assert password != '' , 'password should be there'
        userid_type = self.model.userid_type
        try:
            older = self.model.read_userid(student_no)
            self.model.update_userid(student_no, username, password)
            self.view.display_userid_updated(
                username, older['username'], username)
        except mvc_exc.ItemNotStored as e:
            self.view.display_userid_not_yet_stored_error(student_no, userid_type, e)
            # if the accommodation is not yet stored and we performed an update, we have
            # 2 options: do nothing or call insert_accommodation to add it.
            # self.insert_accommodation(name, price, quantity)

    def update_userid_type(self, new_userid_type):
        old_userid_type = self.model.userid_type
        self.model.userid_type = new_userid_type
        self.view.display_change_userid_type(old_userid_type, new_userid_type)

    def delete_userid(self, student_no):
        userid_type = self.model.userid_type
        try:
            self.model.delete_userid(student_no)
            self.view.display_userid_deletion(student_no)
        except mvc_exc.ItemNotStored as e:
            self.view.display_userid_not_yet_stored_error(student_no, userid_type, e)

