import wpilib
import wpilib.drive
import wpilib.src
import subsistemas.gyro.Gyro
import math
import wpimath.geometry



modules = [4]
gyro = subsistemas.gyro.Gyro
maxAngularSpeed = 5 
velocidadmaxima = 10
class swerve():

  def __init__(self) -> None:
    #middle is at 1,1
    self.FLPose = wpimath.geometry.Translation2d(0,2)
    self.FRPose = wpimath.geometry.Translation2d(2.2)
    self.BLPose = wpimath.geometry.Translation2d(0,0)
    self.BRPose = wpimath.geometry.Translation2d(2,0)

