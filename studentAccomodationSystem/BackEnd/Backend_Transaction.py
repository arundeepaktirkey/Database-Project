import mvc_exceptions as mvc_exc

from copy import deepcopy
from datetime import date
from dateutil.relativedelta import relativedelta

class Backend_Transaction():

    transactionids = list()

    


    # create rooms function
    def create_transactions(student_no, name, address, selected_accommodation, selected_apartment, apartmentids, roomids):
        global transactionids
        
        # create dictionary from list1:
        dict1 = {(record["accommodation_no"], record["apartment_no"]): record  for record in apartmentids}

        #compare elements in list2 to those on list1:
        result = {}
        for record in roomids:
            ckey = record["accommodation_no"], record["apartment_no"]
            new_record = deepcopy(record)
            if ckey in dict1:
                for key, value in dict1[ckey].items():
                    if key in ("accommodation_no", "apartment_no"):
                        # Do not merge these keys
                        continue
                    # Dict's "setdefault" finds a key/value, and if it is missing
                    # creates a new one with the second parameter as value
                    new_record[key] = value

            result[ckey] = new_record

        apartment_room_data = list(result.values())

        transactionids = list(filter(lambda x: x['accommodation_no'] == selected_accommodation and x['apartment_no'] == selected_apartment, apartment_room_data))

        for x in transactionids:
            # 'student_no':100612450, 'name':'Arun Blaze', 'address':'derby,england',
            x['student_no'] = student_no
            x['name'] = name
            x['student_address'] = address
            x['date_from'] = str(date.today())
            x['date_to'] = str(date.today() + relativedelta(months=6))

        return transactionids

