

import ctre
from ctre import WPI_TalonSRX

from magicbot import will_reset_to

import wpilib

class Fork:
    fork_switch: wpilib.DigitalInput
    arm_motor: ctre.WPI_TalonSRX

    position = will_reset_to(0)
    last_position = 0

    def execute(self):
        if self.position != 0: # if nothing is being pressed - do this
            self.last_position = self.position

        self.arm_motor.set(self.position)

    def open(self):
        self.position = -1

# TODO: Check if the value is right(both functions)
    def close(self):
        self.position = 1
