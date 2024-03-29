
from controller import Robot,Keyboard,Motion

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = 32
robot=Robot()
keyboard=Keyboard()
keyboard.enable(timestep)

forward = Motion('../../motions/Forwards50.motion')
backward = Motion('../../motions/Backwards.motion')
sideStepLeft = Motion('../../motions/SideStepLeft.motion')
sideStepRight = Motion('../../motions/SideStepRight.motion')
Turnleft = Motion('../../motions/TurnRight60.motion')
HandWave = Motion('../../motions/HandWave.motion')
def startMotion(motion):
    motion.play()
def printMsg():
    print('press up to move forward')
    print('press down to move backward')
    print('press left for side step left')
    print('press right for side step right')
    print('press a to turn left')
    print('press b to turn right')
key=-1
printMsg()

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    if key==Keyboard.LEFT:
        startMotion(sideStepLeft)
    elif key == Keyboard.RIGHT:
                startMotion(sideStepRight)
    elif key == Keyboard.UP:
        startMotion(forward)
    elif key == Keyboard.DOWN:
                startMotion(backward)
    elif key == 65:
            startMotion(TurnLeft)
    elif key == 66:
        startMotion(HandWave)

# Enter here exit cleanup code.
