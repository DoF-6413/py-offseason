import wpilib
import wpilib.drive
import wpilib.src
import swerveModule
import subsistemas.gyro.Gyro as Gyro
import wpimath.kinematics as kinematics 
import wpimath.geometry as geometry

class swerve():

  velocidadmaxima = 10
  timer = wpilib.Timer()
  kinematics = kinematics.SwerveDrive2Kinematics
  modules = [4]
  

  
  def __init__(self) -> None:

    self.modules[0] = swerveModule.swerveModule(0)
    self.modules[1] = swerveModule.swerveModule(1)
    self.modules[2] = swerveModule.swerveModule(2)
    self.modules[3] = swerveModule.swerveModule(3)
    self.kinematics = kinematics.SwerveDrive2Kinematics()
    self.timer.start
    