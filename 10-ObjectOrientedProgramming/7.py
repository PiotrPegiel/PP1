class University():
    def __init__(self):
        self.name = 'UEK'
    def print_name(self):
        print(self.name)
    def set_name(self, name):
        self.name = name
a = University()
a.print_name()
a.set_name("MIT")
a.print_name()