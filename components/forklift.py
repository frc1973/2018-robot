
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
    mode = 'pct'
    pct = 0

    def execute(self):
        
        if self.mode == 'pct':
            self.winch_motor.set(self.pct)
            self.pct = 0
        else:
            # Don't uncomment this until we test it!
            #self.winch_motor.set(WPI_TalonSRX.ControlMode.Position, self.position)
            pass
        
    def normal(self, v):
        self.mode = 'pct'
        self.pct = v
        


    '''
        Figure out the exact
        values for these variables

    '''

    def top(self):
        self.mode = 'pos'
        self.position = 7000

    def mid(self):
        self.mode = 'pos'
        self.position = 4000

    def bot(self):
        self.mode = 'pos'
        self.position = 0
