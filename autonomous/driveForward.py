

from magicbot import AutonomousStateMachine, timed_state, state
import wpilib

# this is one of your components
from components.drive_train import DriveTrain

class DriveForward(AutonomousStateMachine):
    MODE_NAME = 'Drive Forward'
    DEFAULT = True

    # Injected from the definition in robot.py
    driveTrain: DriveTrain

    @timed_state(duration=3, first=True, next_state='drop_cube')
    def drive_forward(self, initial_call):
        self.driveTrain.move(-0.7, 0)

    @state
    def drop_cube(self):
        pass
