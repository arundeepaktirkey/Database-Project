import mvc_exceptions as mvc_exc

class Backend_User():
    
    userids = list() # global variable where we keep the data

    # create function
    def create_userids(app_accommodations):
        global userids
        userids = app_accommodations

    def create_userid(student_no, username, password):
        global userids
        results = list(filter(lambda x: x['student_no'] == student_no, userids))
        if results:
            raise mvc_exc.ItemAlreadyStored('"{}" already stored!'.format(student_no))
        else:
            userids.append({'student_no': student_no, 'username': username, 'password': password })
        return userids

    # read function
    def read_username(username):
        global userids
        mylist = list(filter(lambda x: x['username'] == username, userids))
        if mylist:
            return username
        else:
            raise mvc_exc.ItemNotStored('Can\'t read "{}" because it\'s not stored'.format(username))
    
    def read_password(password):
        global userids
        mylist = list(filter(lambda x: x['password'] == password, userids))
        if mylist:
            return mylist[0]
        else:
            raise mvc_exc.ItemNotStored('Can\'t read "{}" because it\'s not stored'.format(password))
    

    def read_userids():
        global userids
        return [x for x in userids]

    # create function 
    def update_userid(student_no, username, password):
        global userids
        idxs_userids = list(
            filter(lambda i_x: i_x[1]['student_no'] == student_no, enumerate(userids))
        )
        if idxs_userids:
            i, userid_to_update = idxs_userids[0][0], idxs_userids[0][1]
            userids[i] = {'student_no': student_no, 'username': username, 'password': password }
        else:
            raise mvc_exc.ItemNotStored(
                'Can\'t update "{}" because it\'s not stored'.format(student_no)
            )
    
    # delete function
    def delete_userid(student_no):
        global userids
        idxs_userids = list(
            filter(lambda i_x: i_x[1]['student_no'] == student_no, enumerate(userids))
        )
        if idxs_userids:
            i, userid_to_delete = idxs_userids[0][0], idxs_userids[0][1]
            del userids[i]
        else:
            raise mvc_exc.ItemNotStored(
                'Can\'t delete "{}" because it\'s not stored'.format(student_no)
            )

    