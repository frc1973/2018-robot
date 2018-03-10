

import wpilib
import wpilib.drive

import ctre


class Forklift():
    GOING_UP = 1
    GOING_DOWN = -1
    SLOW = 1.0/3.0
    MEDIUM = 0.5
    FAST = 0.9

    STATE_TOP = 0
    STATE_NEAR_TOP = 1
    STATE_MIDDLE = 2
    STATE_NEAR_BOTTOM = 3
    STATE_BOTTOM = 4

    def __init__(self, joystick, winch_motor):
        self.joystick = joystick
        self.winch_motor = winch_motor
        self.encoder = None #TODO:
        self.top_limit_switch = wpilib.DigitalInput(1) # TODO
        self.bot_limit_switch = wpilib.DigitalInput(2) # TODO
        self.joystick_speed = 0

    def getWinchSpeedLimit(self, state, direction):
        """

            Get the Max speed of the winch motor
            based on where the Forklift is

        """

        if state == STATE_TOP and direction == GOING_UP:
            return 0
        elif state == STATE_NEAR_TOP and direction == GOING_UP:
            return SLOW
        elif state == STATE_BOTTOM and direction == GOING_DOWN:
            return 0
        elif state == STATE_NEAR_BOTTOM and direction == GOING_DOWN:
            return SLOW
        else:
            return FAST

    def positionToState(self):
        """

            Convert the potentiometer position
            to state

        """
        # TODO: fix these numbers once we calibrate the encoder
        POSITION_TOP = 10000
        POSITION_MID_TOP = 8000
        POSITION_MID_BOTTOM = 2000
        POSITION_BOTTOM = 1000

        position = self.encoder.getPosition() # TODO figure out how to get encoder value

        if self.top_limit_switch.get():
            return STATE_TOP
        elif self.bot_limit_switch.get():
            return STATE_BOTTOM

        if position >= POSITION_TOP:
            return STATE_TOP # Stop
        elif position < POSITION_TOP and position >= POSITION_MID_TOP:
            return STATE_NEAR_TOP # Keep going
        elif position < POSITION _MID_TOP and position >= POSITION_MID_BOTTOM:
            return STATE_NEAR_MIDDLE # Keep going
        elif position < POSITION_MID_BOTTOM and position >= POSITION_BOTTOM:
            return STATE_NEAR_BOTTOM # Stop
        else:
            return STATE_BOTTOM

    def joystickCommandToDirection(self):
        """

            Convert forklift winch motor commanded
            value to a direction

        """
        joystick_command = self.joystick.getY() # TODO: verify Y is forward/back
        if joystick_command > 0:
            return GOING_UP
        elif joystick_command < 0:
            return GOING_DOWN
        else:
            return 0

    def readJoystickSpeed(self):
        """

            This checks the speed from the joystick commands.


        """
        # if he's not pushing the joystick stop the forklift
        if self.joystickCommandToDirection() == 0:
            self.joystick_speed = 0
        # if he's pushing the joystick and he pressed the slow button
        elif self.joystick.getRawButton(4):
            self.joystick_speed = SLOW
        # if he's pushing the joystick and he pressed the medium button
        elif self.joystick.getRawButton(3):
            self.joystick_speed = MEDIUM
        # if he's pushing the joystick and he pressed the fast button
        elif self.joystick.getRawButton(5):
            self.joystick_speed = FAST
        # if he just pushed the joystick and has not set any speed yet
        elif self.joystick_speed == 0:
            self.joystick_speed = SLOW

    def setSpeed(self):
        state = self.positionToState()
        direction = self.joystickCommandToDirection()
        speed_limit = self.getWinchSpeedLimit(state, direction)
        self.readJoystickSpeed()

        # Obey the joystick, unless it goes above the speed limit
        if self.joystick_speed > speed_limit:
            # TODO: set winch motor speed
            self.winch_motor.set(speed_limit * direction)
        else:
            self.winch_motor.set(self.joystick_speed * direction)
