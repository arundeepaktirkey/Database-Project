from BackEnd.Backend_User import Backend_User as user_backend

class User(object):

    def __init__(self, application_items):
        self._userid_type = 'UserId'
        self.create_userids(application_items)
    
    @property
    def userid_type(self):
        return self._userid_type

    @userid_type.setter
    def userid_type(self, new_userid_type):
        self._userid_type = new_userid_type
    
    def create_userid(self, student_no, username, password):
        userids = user_backend.create_userid(student_no, username, password)
        return userids

    def create_userids(self, userid):
        user_backend.create_userids(userid)

    def read_username(self, username):
        return user_backend.read_username(username)

    def read_password(self, password):
        return user_backend.read_password(password)

    def update_userid(self, student_no, username, password):
        user_backend.update_userid(student_no, username, password)

    def delete_accommodation(self, student_no):
        user_backend.delete_userid(student_no)
    