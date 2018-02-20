#!/usr/bin/env python3
"""
    This is a good foundation to build your robot code on
"""

import wpilib
import wpilib.drive

import ctre


class MyRobot(wpilib.IterativeRobot):

    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        self.left_motor = ctre.WPI_TalonSRX(5)
        self.right_motor = ctre.WPI_TalonSRX(6)
        self.drive = wpilib.drive.DifferentialDrive(self.left_motor, self.right_motor)

        self.stick = wpilib.Joystick(0)
        self.stick2 = wpilib.Joystick(1)

        self.other_motor1 = ctre.WPI_TalonSRX(7)
        self.other_motor2 = ctre.WPI_TalonSRX(8)

    def teleopPeriodic(self):
        """This function is called periodically during operator control."""
        self.drive.arcadeDrive(self.stick.getY(), self.stick.getX())

        self.other_motor1.set(self.stick.getZ())
        self.other_motor2.set(self.stick2.getZ())

if __name__ == "__main__":
    wpilib.run(MyRobot)
