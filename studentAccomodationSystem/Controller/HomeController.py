
class HomeController(object):

    def __init__(self, view):
        self.view = view

    def transfering_controller(self):
        inputkey = self.view.logged_Student()
        if inputkey == 1:
            return inputkey
        elif inputkey == 2:
            return inputkey
        elif inputkey == 3:
            return exit()
        else:
            print('You have pressed invalid input !!!')

    