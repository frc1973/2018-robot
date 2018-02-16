#!/usr/bin/env python3

import magicbot
import wpilib

import components.elevator


class Robot(magicbot.MagicRobot):

    elevator = components.elevator.Elevator

    def createObjects(self):

        # Elevator motor/sensors
        self.elevator_motor = wpilib.Talon(1)
        self.elevator_top = wpilib.DigitalInput(1)
        self.elevator_mid = wpilib.DigitalInput(2)
        self.elevator_bottom = wpilib.DigitalInput(3)

        self.joy = wpilib.Joystick(0)

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        if self.joy.getRawButton(1):
            self.elevator.up()
        if self.joy.getRawButton(2):
            self.elevator.down()
        if self.joy.getRawButton(4):
            self.elevator.gotoTop()
        if self.joy.getRawButton(3):
            self.elevator.gotoMiddle()


if __name__ == '__main__':
    wpilib.run(Robot)
