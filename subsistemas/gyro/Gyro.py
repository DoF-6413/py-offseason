from navx import AHRS

# Create an AHRS object, specifying the port the NavX is connected to
navx = AHRS.create_spi()

# Get the current yaw angle
yaw = navx.getYaw()
print("Yaw:", yaw)

# Get the current pitch angle
pitch = navx.getPitch()
print("Pitch:", pitch)

# Get the current roll angle
roll = navx.getRoll()
print("Roll:", roll)