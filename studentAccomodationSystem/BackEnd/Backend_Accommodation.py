import mvc_exceptions as mvc_exc

class Backend_Accommodation():
    
    accomodations = list() # global variable where we keep the data

    # create function
    def create_accommodations(app_accommodations):
        global accommodations
        accommodations = app_accommodations

    def create_accommodation(Acco_No, Name, Address):
        global accommodations
        results = list(filter(lambda x: x['name'] == Name, accommodations))
        if results:
            raise mvc_exc.ItemAlreadyStored('"{}" already stored!'.format(Name))
        else:
            accommodations.append({'accommodation_no': Acco_No, 'name': Name, 'address': Address })

    # read function
    def read_accommodation(name):
        global accommodations
        mylist = list(filter(lambda x: x['name'] == name, accommodations))
        if mylist:
            return mylist[0]
        else:
            raise mvc_exc.ItemNotStored('Can\'t read "{}" because it\'s not stored'.format(name))
    
    def read_accommodation_no(accommodation_no):
        global accommodations
        mylist = list(filter(lambda x: x['accommodation_no'] == accommodation_no, accommodations))
        if mylist:
            return accommodation_no
        else:
            raise mvc_exc.ItemNotStored('Can\'t read "{}" because it\'s not stored'.format(accommodation_no))
    

    def readAll_accommodation():
        global accommodations
        return [x for x in accommodations]

    # create function 
    def update_accommodation(Acco_No, Name, Address):
        global accommodations
        idxs_accommodations = list(
            filter(lambda i_x: i_x[1]['name'] == Name, enumerate(accommodations))
        )
        if idxs_accommodations:
            i, accommodation_to_update = idxs_accommodations[0][0], idxs_accommodations[0][1]
            accommodations[i] = {'accommodation_no': Acco_No, 'name': Name, 'address': Address }
        else:
            raise mvc_exc.ItemNotStored(
                'Can\'t update "{}" because it\'s not stored'.format(Name)
            )
    
    # delete function
    def delete_accommodation(name):
        global accommodations
        idxs_accommodations = list(
            filter(lambda i_x: i_x[1]['name'] == name, enumerate(accommodations))
        )
        if idxs_accommodations:
            i, accommodation_to_delete = idxs_accommodations[0][0], idxs_accommodations[0][1]
            del accommodations[i]
        else:
            raise mvc_exc.ItemNotStored(
                'Can\'t delete "{}" because it\'s not stored'.format(name)
            )

    