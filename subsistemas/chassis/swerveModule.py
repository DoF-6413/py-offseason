import math
import wpilib
import wpimath.kinematics as kinematics 
import wpimath.geometry as geometry
import wpimath.controller 
import wpimath.trajectory
import wpimath.units
from rev import SparkAbsoluteEncoder

from rev import CANSparkMax

WHEEL_RAD = wpimath.units.inchesToMeters(2)
ENCODER_RESOLUTION = 4096
MODULE_MAX_ANG_VEL = math.pi #Module max angular vel 
MODULE_MAX_ACCELERATION = math.tau  # module max angula acceleration Tau (τ) is a mathematical constant that is the ratio of a circle's circumference to its radius. This produces a number, and that number is always the same.

class swerveModule:
    def __init__(self, index)-> None:
        """index is the number of modules that exist"""
        match index:
            case 0:
                self.driverMotor = CANSparkMax()#TODO CHECK ID
                self.turningMotor = CANSparkMax()#TODO CHECK ID
                self.driveEncoder = self.driverMotor.getEncoder()
                self.turningEncoder = self.turningMotor.getEncoder()
            case 1:
                self.driverMotor = CANSparkMax()#TODO CHECK ID
                self.turningMotor = CANSparkMax()#TODO CHECK ID
                self.driveEncoder = self.driverMotor.getEncoder()
                self.turningEncoder = self.turningMotor.getEncoder()
            case 2:
                self.driverMotor = CANSparkMax()#TODO CHECK ID
                self.turningMotor = CANSparkMax()#TODO CHECK ID
                self.driveEncoder = self.driverMotor.getEncoder()
                self.turningEncoder = self.turningMotor.getEncoder()
            case 3:
                self.driverMotor = CANSparkMax()#TODO CHECK ID
                self.turningMotor = CANSparkMax()#TODO CHECK ID
                self.driveEncoder = self.driverMotor.getEncoder()
                self.turningEncoder = self.turningMotor.getEncoder()
    def getState(self) -> kinematics.SwerveModuleState:
        """Returns the current state of the module.

        :returns: The current state of the module.
        """    
        return kinematics.SwerveModuleState(
        self.driveEncoder.getVelocity(), geometry.Rotation2d(self.turningEncoder.getPosition()),
        )
    def getPosition(self) -> kinematics.SwerveModulePosition:
        """Returns the current position of the module.

        :returns: The current position of the module.
        """    
        return kinematics.SwerveModulePosition(self.driveEncoder.getPosition,wpimath.geometry.Rotation2d(self.turningEncoder.getPosition))