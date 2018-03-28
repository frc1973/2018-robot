#!/usr/bin/env python3

import magicbot
import wpilib
import wpilib.drive

import components.forklift
import components.drive_train
import components.fork

import ctre

from ctre import WPI_TalonSRX


class Robot(magicbot.MagicRobot):

    forklift: components.forklift.Forklift
    fork: components.fork.Fork
    driveTrain: components.drive_train.DriveTrain

    #: Which PID slot to pull gains from. Starting 2018, you can choose from
    #: 0,1,2 or 3. Only the first two (0,1) are visible in web-based
    #: configuration.
    kSlotIdx = 0

    #: Talon SRX/ Victor SPX will supported multiple (cascaded) PID loops. For
    #: now we just want the primary one.
    kPIDLoopIdx = 0

    #: set to zero to skip waiting for confirmation, set to nonzero to wait and
    #: report to DS if action fails.
    kTimeoutMs = 10

    twitchyX = magicbot.tunable(0.7) #
    twitchyY = magicbot.tunable(0.7)


    def createObjects(self):

        # GOTTA DO STUFF

        self.left_speed = 0
        self.right_speed = 0 # Because we want our velocity to be equals to 0; at first

        self.fork_switch = wpilib.DigitalInput(1)
        self.gyro = wpilib.ADXRS450_Gyro()

        self.left_motor = ctre.WPI_TalonSRX(5)
        self.right_motor = ctre.WPI_TalonSRX(6)

        self.drive = wpilib.drive.DifferentialDrive(self.left_motor, self.right_motor)

        self.drive_stick = wpilib.Joystick(0)
        self.forklift_stick = wpilib.Joystick(1)

        # Other motors
        self.winch_motor = ctre.WPI_TalonSRX(7)

        self.arm_motor = ctre.WPI_TalonSRX(8)
        # choose the sensor and sensor direction
        self.winch_motor.configSelectedFeedbackSensor(WPI_TalonSRX.FeedbackDevice.CTRE_MagEncoder_Relative, self.kPIDLoopIdx, self.kTimeoutMs)

        # choose to ensure sensor is positive when output is positive
        self.winch_motor.setSensorPhase(True)

        # choose based on what direction you want forward/positive to be.
        # This does not affect sensor phase.
        self.winch_motor.setInverted(False)

        # set the peak and nominal outputs, 12V means full
        self.winch_motor.configNominalOutputForward(0, self.kTimeoutMs)
        self.winch_motor.configNominalOutputReverse(0, self.kTimeoutMs)
        self.winch_motor.configPeakOutputForward(1, self.kTimeoutMs)
        self.winch_motor.configPeakOutputReverse(-1, self.kTimeoutMs)

        # Set the allowable closed-loop error, Closed-Loop output will be
        # neutral within this range. See Table in Section 17.2.1 for native
        # units per rotation.
        self.winch_motor.configAllowableClosedloopError(0, self.kPIDLoopIdx, self.kTimeoutMs)

        # set closed loop gains in slot0, typically kF stays zero - see documentation */
        self.winch_motor.selectProfileSlot(self.kSlotIdx, self.kPIDLoopIdx)
        self.winch_motor.config_kF(0, 0, self.kTimeoutMs)
        self.winch_motor.config_kP(0, 0.9, self.kTimeoutMs)
        self.winch_motor.config_kI(0, 0, self.kTimeoutMs)
        self.winch_motor.config_kD(0, 0, self.kTimeoutMs)

        # zero the sensor
        self.winch_motor.setSelectedSensorPosition(0, self.kPIDLoopIdx, self.kTimeoutMs)





        # Elevator motor/sensors
        #self.elevator_top = wpilib.DigitalInput(1)
        #self.elevator_mid = wpilib.DigitalInput(2)
        #self.elevator_bottom = wpilib.DigitalInput(3)

        #Drive motors


        self.joy = wpilib.Joystick(0)

    def teleopInit(self):
        pass

    def teleopPeriodic(self):

        self.driveTrain.move(self.twitchyY*self.joy.getY(), self.twitchyY*self.joy.getX())

        # if self.joy.getRawButton(8):
        #    self.driveTrain.move2(-90)
        # elif self.joy.getRawButton(9):
        #    self.driveTrain.move2(90)

        # Creating the buttom for the actuator/fork
        # if self.joy.getRawButton(1):
        #    self.fork.OPEN()


        # TODO: center of gravity compensation


        # y = self.joy.getY()
        # b3 = self.joy.getRawButton(3)
        # b4 = self.joy.getRawButton(4)
        # b5 = self.joy.getRawButton(5)

        if self.joy.getRawButton(4):
            self.forklift.top()
        if self.joy.getRawButton(3):
            self.forklift.mid()
        if self.joy.getRawButton(5):
            self.forklift.bot()

        if self.joy.getRawButton(7):
            self.forklift.normal(self.joy.getZ())

        # control the arm
        if self.joy.getRawButton(1): # This is trigger
            self.fork.close()
        elif self.joy.getRawButton(2): # This is the other
            self.fork.open()


if __name__ == '__main__':
    wpilib.run(Robot)
