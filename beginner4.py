from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.beginner import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[4],0)
# your code starts here:
for i in range(1):
    robotArm.moveRight()
for i in range(6):
    robotArm.grab()
    if robotArm.scan() == "white":
      robotArm.moveLeft()
      robotArm.drop()
      robotArm.moveRight()
    elif robotArm.scan() == "red":
     robotArm.moveRight()
     robotArm.drop()
     robotArm.moveLeft()
    else:
      robotArm.drop()
# your code ends here

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()
