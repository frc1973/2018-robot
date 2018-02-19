#!/usr/bin/env python3

import magicbot
import wpilib
import wpilib.drive

import components.elevator
import components.drive_train


class Robot(magicbot.MagicRobot):

    elevator = components.elevator.Elevator
    driveTrain = components.drive_train.DriveTrain

    def createObjects(self):

        # GOTTA DO STUFF

        # Elevator motor/sensors
        self.elevator_motor = wpilib.Talon(2)
        self.elevator_top = wpilib.DigitalInput(1)
        self.elevator_mid = wpilib.DigitalInput(2)
        self.elevator_bottom = wpilib.DigitalInput(3)

        #Drive motors
        self.left_motor = wpilib.Spark(0)
        self.right_motor = wpilib.Spark(1)
        self.drive = wpilib.drive.DifferentialDrive(self.left_motor, self.right_motor)



        self.joy = wpilib.Joystick(0)

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        self.driveTrain.move(self.joy.getY(), self.joy.getX())
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
