class View_Accommodation(object):

    @staticmethod
    def show_bullet_point_list(accommodation_type, accommodations):
        print('--- {} LIST ---'.format(accommodation_type.upper()))
        for accommodation in accommodations:
            print('* {}'.format(accommodation))

    @staticmethod
    def show_number_point_list(accommodation_type, accommodations):
        print('--- {} LIST ---'.format(accommodation_type.upper()))
        for i, accommodation in enumerate(accommodations):
            print('{}. {}'.format(i+1, accommodation))

    @staticmethod
    def show_accommodation(accommodation_type, accommodation, accommodation_info):
        print('//////////////////////////////////////////////////////////////')
        print('Good news, we have some {}!'.format(accommodation.upper()))
        print('{} INFO: {}'.format(accommodation_type.upper(), accommodation_info))
        print('//////////////////////////////////////////////////////////////')

    @staticmethod
    def display_missing_accommodation_error(accommodation, err):
        print('**************************************************************')
        print('We are sorry, we have no {}!'.format(accommodation.upper()))
        print('{}'.format(err.args[0]))
        print('**************************************************************')

    @staticmethod
    def display_accommodation_already_stored_error(accommodation, accommodation_type, err):
        print('**************************************************************')
        print('Hey! We already have {} in our {} list!'
              .format(accommodation.upper(), accommodation_type))
        print('{}'.format(err.args[0]))
        print('**************************************************************')

    @staticmethod
    def display_accommodation_not_yet_stored_error(accommodation, accommodation_type, err):
        print('**************************************************************')
        print('We don\'t have any {} in our {} list. Please insert it first!'
              .format(accommodation.upper(), accommodation_type))
        print('{}'.format(err.args[0]))
        print('**************************************************************')

    @staticmethod
    def display_accommodation_stored(accommodation, accommodation_type):
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print('Hooray! We have just added some {} to our {} list!'
              .format(accommodation.upper(), accommodation_type))
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

    @staticmethod
    def display_change_accommodation_type(older, newer):
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')
        print('Change accommodation type from "{}" to "{}"'.format(older, newer))
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')

    @staticmethod
    def display_accommodation_updated(accommodation, o_name, o_address, n_name, n_address):
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')
        print('Change {} price: {} --> {}'
              .format(accommodation, o_name, n_name))
        print('Change {} quantity: {} --> {}'
              .format(accommodation, o_address, n_address))
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')

    @staticmethod
    def display_accommodation_deletion(name):
        print('--------------------------------------------------------------')
        print('We have just removed {} from our list'.format(name))
        print('--------------------------------------------------------------')
