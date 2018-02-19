#import math
import wpilib

class DriveTrain:
    '''
        Simple magicbot drive object
    '''

    #wall_p = tunable(-1.8)
    #distance = tunable(0)
    #analog = tunable(0)

    #tx = tunable(0)
    #ty = tunable(0)
    #offset = tunable(1.0)

    #MaxY = tunable(0.8)

    #ultrasonic = wpilib.AnalogInput
    drive = wpilib.drive.DifferentialDrive

    def __init__(self):
        self.x = 0
        self.y = 0
# distance is .98
    def move(self, y, x):
        self.y = y
        self.x = x

    def rotate(self, x):
        self.x = x

    def execute(self):
        self.tx = self.x
        self.ty = self.y
        self.drive.arcadeDrive(self.y, self.x, True)

        self.x = 0
        self.y = 0
