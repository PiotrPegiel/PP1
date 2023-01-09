class TV():
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = []
        self.volume = 0
    def turn_on(self):
        self.is_on = True
    def turn_off(self):
        self.is_on = False
    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no
    def set_channels(self, channels_list):
        self.channels = channels_list
    def dec_volume(self):
        if self.volume > 0:
            self.volume -= 1
    def inc_volume(self):
        if self.volume < 10:
            self.volume += 1
    def show_channels(self):
        print(self.channels)
    def show_status(self):
        if self.is_on == True:
            if self.channel_no <= len(self.channels):
                print(f"TV is on, volume = {self.volume}, channel {self.channel_no} ({self.channels[self.channel_no-1]})")
            else:
                print(f"TV is on, volume = {self.volume}, channel {self.channel_no}")
        else:
            print("TV is off")

a = TV()
a.show_status()
a.turn_on()
a.show_status()
a.set_channels(["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery", "Trwam"])
a.show_status()
a.inc_volume()
a.show_status()
a.dec_volume()
a.dec_volume()
a.show_status()
a.turn_off()