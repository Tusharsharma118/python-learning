class Fan:
    def __init__(self, make, radius, color):
        self.make = make
        self.radius = radius
        self.color = color
        self.speed = 0.0
        self.isOn = False

    def switch_on(self):
        self.isOn = True

    def switch_off(self):
        self.isOn = False

    def change_speed(self, how_much):
        self.speed += how_much

    def __repr__(self):
        return ('Make: ' + self.make
                + '\nRadius: ' + str(self.radius)
                + '\nColor: ' + self.color
                + '\nSpeed: ' + str(self.speed)
                + '\nTurned On: ' + str(self.isOn))

fan = Fan('Bajaj', 10, 'Red')
print(fan)
