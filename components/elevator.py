
import wpilib

class Elevator:

    elevator_motor = wpilib.Talon

    elevator_top = wpilib.DigitalInput
    elevator_mid = wpilib.DigitalInput
    elevator_bottom = wpilib.DigitalInput
    active = False

    speed = 0

    def up(self):
        self.speed = -1

    def down(self):
        self.speed = 1

    def gotoTop(self):
        pass

    def gotoMiddle(self):
        self.active = True

    def gotoBottom(self):
        pass

    def execute(self): # This is the start
        """
        self.speed = 0"""

        if self.active:
            self.speed = -1
            if self.elevator_mid.get():
                self.speed = 0
                self.active = False

        self.elevator_motor.set(self.speed)
        self.speed = 0
