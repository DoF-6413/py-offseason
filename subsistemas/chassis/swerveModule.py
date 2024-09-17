import math
import wpilib
import wpimath.kinematics
import wpimath.geometry
import wpimath.controller
import wpimath.trajectory
import wpimath.units

WHEEL_RAD = wpimath.units.inchesToMeters(2)
ENCODER_RESOLUTION = 4096
MODULE_MAX_ANG_VEL = math.pi #Module max angular vel 
MODULE_MAX_ACCELERATION = math.tau  # module max angula acceleration Tau (τ) is a mathematical constant that is the ratio of a circle's circumference to its radius. This produces a number, and that number is always the same.

class swerveModule:
    def __init__(
           self,
           driveMotorChannel: int,
           turningMotorChannel: int,
           driveEncoderChannelA: int,
           driveEncoderChannelB: int,
           turningEncoderChannelA: int,
           turningEncoderChannelB: int,)-> None:
         """Constructs a SwerveModule with a drive motor, turning motor, drive encoder and turning encoder.

        :param driveMotorChannel:      PWM output for the drive motor.
        :param turningMotorChannel:    PWM output for the turning motor.
        :param driveEncoderChannelA:   DIO input for the drive encoder channel A
        :param driveEncoderChannelB:   DIO input for the drive encoder channel B
        :param turningEncoderChannelA: DIO input for the turning encoder channel A
        :param turningEncoderChannelB: DIO input for the turning encoder channel B
        """
         self.driverMotor = wpilib.CAN(1)
         self.turningMotor = wpilib.CAN(2)
         self.driveEncoder = wpilib.Encoder(driveEncoderChannelA,driveEncoderChannelB)
         self.turningEncoder = wpilib.Encoder(turningEncoderChannelA,turningEncoderChannelB)
         self.drivePID = wpimath.controller.PIDController(1,0,0)
         self.turningPID = wpimath.controller.PIDController(1,0,0,wpimath.trajectory.TrapezoidProfile.Constraints(MODULE_MAX_ANG_VEL,MODULE_MAX_ACCELERATION),"""HOW FAST IT UPODATES DEFAULT 20 MILISEC """ )


        # Set the distance per pulse for the drive encoder. We can simply use the
        # distance traveled for one rotation of the wheel divided by the encoder
        # resolution.
         self.driveEncoder.setDistancePerPulse(math.tau * WHEEL_RAD / ENCODER_RESOLUTION)

        # Set the distance (in this case, angle) in radians per pulse for the turning encoder.
        # This is the the angle through an entire rotation (2 * pi) divided by the
        # encoder resolution.
         self.turningEncoder.setDistancePerPulse(math.tau/ENCODER_RESOLUTION)
        # Limit the PID Controller's input range between -pi and pi and set the input
        # to be continuous.
         self.turningPID.enableContinuousInput(math.tau/ ENCODER_RESOLUTION)

    def getState(self) -> wpimath.kinematics.SwerveModuleState:
        """Returns the current state of the module.

        :returns: The current state of the module.
        """    
        return wpimath.kinematics.SwerveModuleState(
        self.driveEncoder.getRate(), wpimath.geometry.Rotation2d(self.turningEncoder.getDistance()),
        )
    def getPosition(self) -> wpimath.kinematics.SwerveModulePosition:
        """Returns the current position of the module.

        :returns: The current position of the module.
        """    
        return wpimath.kinematics.SwerveModulePosition(self.driveEncoder.getRate(),wpimath.geometry.Rotation2d(self.turningEncoder.getRate()), )