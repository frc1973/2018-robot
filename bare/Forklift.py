

import wpilib
import wpilib.drive

import ctre


class Forklift():
    GOING_UP = 1
    GOING_DOWN = -1
    SLOW = 1.0/3.0
    FAST = 0.9

    STATE_TOP = 0
    STATE_NEAR_TOP = 1
    STATE_MIDDLE = 2
    STATE_NEAR_BOTTOM = 3
    STATE_BOTTOM = 4


    def __init__(self, joystick, winch_motor, potentiometer):
        self.joystick = joystick
        self.winch_motor = winch_motor
        self.potentiometer = potentiometer

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
        # TODO: fix these numbers once we calibrate the potentiometer
        POSITION_TOP = 10000
        POSITION_MID_TOP = 8000
        POSITION_MID_BOTTOM = 2000
        POSITION_BOTTOM = 1000

        position = self.potentiometer.getPosition() # TODO figure out how to get potentiometer value

        if position >= POSITION_TOP:
            return STATE_TOP # Stop
        elif position < POSITION_TOP and position >= POSITION_MID_TOP:
            return STATE_NEAR_TOP # Keep going
        elif position < POSITION _MID_TOP and position >= POSITION_MID_BOTTOM:
            return STATE_NEAR_MIDDLE # Keep going
        elif position < POSITION_MID_BOTTOM and position >= POSITION_BOTTOM:
            return STATE_NEAR_BOTTOM # Stop
        else:
            return NEAR_BOTTOM

    def joystickCommandToDirection(self):
        """

            Convert forklift winch motor commanded
            value to a direction

        """
        joystick = self.joystick.getY() # TODO: verify Y is forward/back
        if joystick_command > 0:
            return GOING_UP
        elif joystick_command < 0:
            return GOING_DOWN
        else:
            return 0

    def setSpeed(self):
        state = self.positionToState()
        direction = self.joystickCommandToDirection()
        max_speed = self.getWinchSpeedLimit(state, direction)

        #TODO: check joystick speed commands (buttons) and set speed based on Joystick
        # and speed limit
        # Obey the joystick, unless it goes above the speed limit

        if speed > max_speed:
            # TODO: set winch motor speed
            # self.winch_motor.
            pass
