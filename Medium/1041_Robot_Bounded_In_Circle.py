# On an infinite plane, a robot initially stands at (0, 0) and faces north.
# The robot can receive one of three instructions:
#
# "G": go straight 1 unit;
# "L": turn 90 degrees to the left;
# "R": turn 90 degrees to the right.
# The robot performs the instructions given in order, and repeats them forever.
#
# Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        size = len(instructions)

        if size <= 1:
            return False

        x, y, dirc = 0, 0, 4  # dir 0-N 1-E 2-S 3-W

        for i in range(size):
            if instructions[i] == "L":
                dirc -= 1
            elif instructions[i] == "R":
                dirc += 1
            else:
                dirc = dirc % 4

                if dirc == 0:
                    y += 1
                elif dirc == 1:
                    x += 1
                elif dirc == 2:
                    y -= 1
                else:
                    x -= 1

        if dirc == 0:
            if x == 0 and y == 0:
                return True
        else:
            newx, newy, newdirc = x, y, dirc

            for i in range(3):
                newdirc = newdirc % 4
                if newdirc == 0:
                    newx += x
                    newy += y
                elif newdirc == 1:
                    newx += y
                    newy -= x
                elif newdirc == 2:
                    newx -= x
                    newy -= y
                else:
                    newx -= y
                    newy += x
                newdirc += dirc

            if newx == 0 and newy == 0:
                return True
        return False