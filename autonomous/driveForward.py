from magicbot import AutonomousStateMachine, timed_state, state
import wpilib

# this is one of your components
from components.drive_train import DriveTrain

class DriveForward(AutonomousStateMachine):
    MODE_NAME = 'Drive Forward'
    DEFAULT = True

    # Injected from the definition in robot.py
    driveTrain = DriveTrain

    @timed_state(duration=3, first=True)
    def drive_forward(self):
        self.driveTrain.move(-0.7, 0)
