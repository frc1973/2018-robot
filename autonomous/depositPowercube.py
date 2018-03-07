

from magicbot import AutonomousStateMachine, timed_state, state

import wpilib
import Forklift

from driveForward import DriveTrain

# TODO: The idea is to make the robot place one powercube to gain ownership of the scale during Autonomous
class depositPowercube(AutonomousStateMachine):
    """
        Orientating the robot of the side where it is at
        currently, and place the powercube in the scale.

    """
    left_Side = 'left side'
    DEFAULT = False

    mid_Side = 'right side'
    DEFAULT = False

    right_Side = 'right side'
    DEFAULT = False

    def left_Side(self, AutonomousStateMachine): #TODO: Finish this up
        if left_Side = True:
            self.driveTrain.move(-0.7, 0) # Drive forward
            set.winch_motor = True # Turning on the motor of the wincher
