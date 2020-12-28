"""
File: bouncing_ball.py
Name: Angel Chen
-------------------------
This program simulates a bouncing ball.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

# Constants
VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

# Global variables
window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)
times = 0           # This controls the click times.
locked = True       # This controls the switch.


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True
    window.add(ball, START_X, START_Y)
    onmouseclicked(fall)


def fall(mouse):
    global times, locked
    vy = 0                                      # vy means the moved vertical values, starts with zero
    if times < 3:                               # when ball jumps out of the window below three times
        if locked:
            while True:
                locked = False                  # turn off the switch
                # ball starts moving
                ball.move(VX, vy)

                # check the position of ball
                if ball.y >= window.height:     # when ball is below window, it bounces back.
                    vy *= -REDUCE               # each bounce reduces y velocity to REDUCE of itself.
                if ball.x >= window.width:      # when ball jumps out of the window,
                    times += 1                  # add up one time
                    break                       # jump out of the while True area

                pause(DELAY)
                vy += GRAVITY
            window.add(ball, START_X, START_Y)  # ball go back to the original position
            locked = True  # turn on the switch so that we can keep
    else:  # when ball jumps out of the window more than three times
        window.add(ball, START_X, START_Y)  # a bouncing ball go back to original position  at (START_X, START_Y)
        ball.move(0, 0)  # the ball won't move anymore


if __name__ == "__main__":
    main()
