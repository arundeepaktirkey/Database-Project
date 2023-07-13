from BackEnd.Backend_Transaction import Backend_Transaction as tran_backend
class Transaction():

    def create_transactions(student_no, name, address, selected_accommodation, selected_apartment, apartmentids, roomids):
        transactions = tran_backend.create_transactions(student_no, name, address, selected_accommodation, selected_apartment, apartmentids, roomids)
        return transactions
        