from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.beginner import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[5],0)
# your code starts here:
for i in range(1):
    robotArm.moveRight()
for i in range(7):
    robotArm.grab()
    for i in range(8):
        robotArm.moveRight()
    robotArm.drop()
    for i in range(8):
        robotArm.moveLeft()


# your code ends hee

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()
