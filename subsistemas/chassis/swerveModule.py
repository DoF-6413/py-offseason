import math
import wpilib
import wpimath.kinematics as kinematics 
import wpimath.geometry as geometry
import wpimath.controller 
import wpimath.trajectory
import wpimath.units as units 
import Constants
from rev import CANSparkMax # if doesn't work uninstall and install the library again 

WHEEL_RAD = units.inchesToMeters(2)
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

        self.driverMotor.burnFlash()
        self.turningMotor.burnFlash()

        self.driverMotor.setCANTimeout(500)
        self.turningMotor.setCANTimeout(500)
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
        return kinematics.SwerveModulePosition(self.driveEncoder.getPosition,geometry.Rotation2d(self.turningEncoder.getPosition))
    def getkinematics(self) -> kinematics.SwerveDrive2Kinematics:
        """returns the kinematics of the modules"""
        return kinematics.SwerveDrive2Kinematics(Constants.getModuleTranslations)