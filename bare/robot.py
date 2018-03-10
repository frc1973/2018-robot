#!/usr/bin/env python3
"""
    This is a good foundation to build your robot code on
"""

import wpilib
import wpilib.drive
import depositPowercube
import ctre

from Forklift import Forklift

class MyRobot(wpilib.IterativeRobot):

    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        self.left_motor = ctre.WPI_TalonSRX(5)
        self.right_motor = ctre.WPI_TalonSRX(6)

        self.drive = wpilib.drive.DifferentialDrive(self.left_motor, self.right_motor)

        self.drive_stick = wpilib.Joystick(0)
        self.forklift_stick = wpilib.Joystick(1)

        # Other motors
        self.winch_motor = ctre.WPI_TalonSRX(7)
        self.other_motor2 = ctre.WPI_TalonSRX(8)

        self.forklift = Forklift(self.forklift_stick, self.winch_motor)

    def teleopPeriodic(self):
        """This function is called periodically during operator control."""
        self.drive.arcadeDrive(self.drive_stick.getY(), self.drive_stick.getX())

        # self.other_motor2.set(self.forklift_stick.getZ())

        self.forklift.setSpeed()

if __name__ == "__main__":
    wpilib.run(MyRobot)
