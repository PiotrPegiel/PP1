class TV():
    def __init__(self):
        self.is_on = False
    def turn_on(self):
        self.is_on = True
    def turn_off(self):
        self.is_on = False
    def show_status(self):
        if self.is_on == True:
            print("TV is on")
        else:
            print("TV is off")
a = TV()
a.show_status()
a.turn_on()
a.show_status()
a.turn_off()
a.show_status()