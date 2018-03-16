#!/usr/bin/env python3

import magicbot
import wpilib
import wpilib.drive

import components.forklift
import components.drive_train

import ctre


class Robot(magicbot.MagicRobot):

    forklift = components.forklift.Forklift
    driveTrain = components.drive_train.DriveTrain

    def createObjects(self):

        # GOTTA DO STUFF

        self.left_motor = ctre.WPI_TalonSRX(5)
        self.right_motor = ctre.WPI_TalonSRX(6)

        self.drive = wpilib.drive.DifferentialDrive(self.left_motor, self.right_motor)

        self.drive_stick = wpilib.Joystick(0)
        self.forklift_stick = wpilib.Joystick(1)

        # Other motors
        self.winch_motor = ctre.WPI_TalonSRX(7)
        self.other_motor2 = ctre.WPI_TalonSRX(8)




        # Elevator motor/sensors
        #self.elevator_top = wpilib.DigitalInput(1)
        #self.elevator_mid = wpilib.DigitalInput(2)
        #self.elevator_bottom = wpilib.DigitalInput(3)

        #Drive motors


        self.joy = wpilib.Joystick(0)

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        self.driveTrain.move(self.joy.getY(), self.joy.getX())
        # if self.joy.getRawButton(1):
        #     self.elevator.up()
        # if self.joy.getRawButton(2):
        #     self.elevator.down()
        # if self.joy.getRawButton(4):
        #     self.elevator.gotoTop()
        # if self.joy.getRawButton(3):
        #     self.elevator.gotoMiddle()


if __name__ == '__main__':
    wpilib.run(Robot)
