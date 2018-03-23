
# import magicbot
# import wpilib
# import wpilib.drive

# import components.drive_train
import ctre
from ctre import WPI_TalonSRX


GotoTop = 30000
GotoMid = 17000
GotoBot = 0

class Forklift:
    winch_motor: ctre.WPI_TalonSRX

    position = 0

    def execute(self):
        self.winch_motor.set(WPI_TalonSRX.ControlMode.Position, self.position)


    '''
        Figure out the exact
        values for these variables

    '''

    def top(self):
        self.position = 7000

    def mid(self):
        self.position = 4000

    def bot(self):
        self.position = 0
