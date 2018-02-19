
import wpilib

class Elevator:

    elevator_motor = wpilib.Talon

    elevator_top = wpilib.DigitalInput
    elevator_mid = wpilib.DigitalInput
    elevator_bottom = wpilib.DigitalInput

    active = False # gotoMiddle var name
    activeTop = False # gotoTop var name

    speed = 0

    def up(self):
        self.speed = -1

    def down(self):
        self.speed = 1

    def gotoTop(self):
        self.activeTop = True

    def gotoMiddle(self):
        self.active = True

    def gotoBottom(self):
        if self.active:
            self.speed = -1
            if self.elevator_top.get():
                self.speed = 0
                self.active = False

    def execute(self): # This is the start
        if self.active: # gotoMiddle action
            self.speed = -1
            if self.elevator_mid.get():
                self.speed = 0
                self.active = False

        self.elevator_motor.set(self.speed)
        self.speed = 0

        # gotoTop action
        if self.activeTop:
            self.speed = -1
            if self.elevator_top.get():
                self.speed = 0
                self.active = False

        self.elevator_motor.set(self.speed)
        self.speed = 0
