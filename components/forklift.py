
# import magicbot
# import wpilib
# import wpilib.drive

# import components.drive_train
import ctre
from ctre import WPI_TalonSRX

from magicbot import tunable



class Forklift:
    winch_motor: ctre.WPI_TalonSRX

    position = 0
    mode = 'pct'
    pct = 0

    encoder = tunable(0)
    pid_p = tunable(0.9)
    set_p = None

    def execute(self):

        if self.set_p is None or abs(self.set_p - self.pid_p) < 0.0001:
            self.winch_motor.config_kP(0, self.pid_p, 0)
            self.set_p = self.pid_p

        if self.mode == 'pct':
            self.winch_motor.set(self.pct)
            self.pct = 0
        else:
            # Don't uncomment this until we test it!
            #self.winch_motor.set(WPI_TalonSRX.ControlMode.Position, self.position)
            pass

        self.encoder = self.winch_motor.getSensorCollection().getQuadraturePosition()




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
