"""
File: my_drawing.py
Name: Angel Chen
----------------------
This file uses campy module to
draw on a GWindow object.
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon, GArc, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    Mike Wazowski is one of my fav characters in Monsters, Inc.
    because he is sooo cute and optimistic!
    """
    window = GWindow(width=800, height=800, title='Mike Wazowski sticker')

    # Mike's body
    body = GOval(400, 400, x=200, y=200)
    body.filled = True
    body.fill_color = "darkseagreen"
    body.color = "darkseagreen"
    window.add(body)

    # Mike's eyes
    white_eye = GOval(175, 175, x=320, y=250)
    white_eye.filled = True
    white_eye.fill_color = "white"
    white_eye.color = "white"
    window.add(white_eye)

    black_eye = GOval(100, 100, x=350, y=270)
    black_eye.filled = True
    window.add(black_eye)

    small_white_eye = GOval(25, 25, x=375, y=280)
    small_white_eye.filled = True
    small_white_eye.fill_color = "white"
    small_white_eye.color = "white"
    window.add(small_white_eye)
    # Mike's mouth
    mouth = GOval(200, 100, x=300, y=450)
    mouth.filled = True
    window.add(mouth)
    # Mike's teethes
    teeth_1 = GPolygon()
    teeth_1.add_vertex((330, 462))
    teeth_1.add_vertex((360, 454))
    teeth_1.add_vertex((355, 480))
    teeth_1.filled = True
    teeth_1.fill_color = "white"
    teeth_1.color = "white"
    window.add(teeth_1)

    teeth_2 = GPolygon()
    teeth_2.add_vertex((360, 454))
    teeth_2.add_vertex((390, 450))
    teeth_2.add_vertex((377, 480))
    teeth_2.filled = True
    teeth_2.fill_color = "white"
    teeth_2.color = "white"
    window.add(teeth_2)

    teeth_3 = GPolygon()
    teeth_3.add_vertex((390, 450))
    teeth_3.add_vertex((420, 450))
    teeth_3.add_vertex((410, 480))
    teeth_3.filled = True
    teeth_3.fill_color = "white"
    teeth_3.color = "white"
    window.add(teeth_3)

    teeth_4 = GPolygon()
    teeth_4.add_vertex((420, 450))
    teeth_4.add_vertex((450, 455))
    teeth_4.add_vertex((430, 480))
    teeth_4.filled = True
    teeth_4.fill_color = "white"
    teeth_4.color = "white"
    window.add(teeth_4)

    teeth_5 = GPolygon()
    teeth_5.add_vertex((450, 455))
    teeth_5.add_vertex((477, 465.5))
    teeth_5.add_vertex((460, 488))
    teeth_5.filled = True
    teeth_5.fill_color = "white"
    teeth_5.color = "white"
    window.add(teeth_5)

    teeth_6 = GPolygon()
    teeth_6.add_vertex((360, 548))
    teeth_6.add_vertex((390, 550))
    teeth_6.add_vertex((375, 530))
    teeth_6.filled = True
    teeth_6.fill_color = "white"
    teeth_6.color = "white"
    window.add(teeth_6)

    teeth_7 = GPolygon()
    teeth_7.add_vertex((390, 550))
    teeth_7.add_vertex((420, 550))
    teeth_7.add_vertex((405, 530))
    teeth_7.filled = True
    teeth_7.fill_color = "white"
    teeth_7.color = "white"
    window.add(teeth_7)

    teeth_8 = GPolygon()
    teeth_8.add_vertex((420, 550))
    teeth_8.add_vertex((450, 546))
    teeth_8.add_vertex((435, 530))
    teeth_8.filled = True
    teeth_8.fill_color = "white"
    teeth_8.color = "white"
    window.add(teeth_8)
    # Mike's legs
    left_leg = GPolygon()
    left_leg.add_vertex((340, 570))
    left_leg.add_vertex((345, 700))
    left_leg.add_vertex((360, 700))
    left_leg.add_vertex((365, 590))
    left_leg.filled = True
    left_leg.fill_color = "darkseagreen"
    left_leg.color = "darkseagreen"
    window.add(left_leg)

    right_leg = GPolygon()
    right_leg.add_vertex((460, 590))
    right_leg.add_vertex((465, 700))
    right_leg.add_vertex((480, 700))
    right_leg.add_vertex((485, 570))
    right_leg.filled = True
    right_leg.fill_color = "darkseagreen"
    right_leg.color = "darkseagreen"
    window.add(right_leg)

    left_sole = GPolygon()
    left_sole.add_vertex((310, 700))
    left_sole.add_vertex((360, 700))
    left_sole.add_vertex((310, 720))
    left_sole.filled = True
    left_sole.fill_color = "darkseagreen"
    left_sole.color = "darkseagreen"
    window.add(left_sole)

    right_sole = GPolygon()
    right_sole.add_vertex((465, 700))
    right_sole.add_vertex((515, 700))
    right_sole.add_vertex((515, 720))
    right_sole.filled = True
    right_sole.fill_color = "darkseagreen"
    right_sole.color = "darkseagreen"
    window.add(right_sole)

    left_toe_1 = GPolygon()
    left_toe_1.add_vertex((310, 700))
    left_toe_1.add_vertex((310, 706))
    left_toe_1.add_vertex((300, 703))
    left_toe_1.filled = True
    window.add(left_toe_1)

    left_toe_2 = GPolygon()
    left_toe_2.add_vertex((310, 706))
    left_toe_2.add_vertex((310, 713))
    left_toe_2.add_vertex((300, 710))
    left_toe_2.filled = True
    window.add(left_toe_2)

    left_toe_3 = GPolygon()
    left_toe_3.add_vertex((310, 713))
    left_toe_3.add_vertex((310, 720))
    left_toe_3.add_vertex((300, 715))
    left_toe_3.filled = True
    window.add(left_toe_3)

    right_toe_1 = GPolygon()
    right_toe_1.add_vertex((515, 700))
    right_toe_1.add_vertex((515, 706))
    right_toe_1.add_vertex((525, 703))
    right_toe_1.filled = True
    window.add(right_toe_1)

    right_toe_2 = GPolygon()
    right_toe_2.add_vertex((515, 706))
    right_toe_2.add_vertex((515, 713))
    right_toe_2.add_vertex((525, 710))
    right_toe_2.filled = True
    window.add(right_toe_2)

    right_toe_3 = GPolygon()
    right_toe_3.add_vertex((515, 713))
    right_toe_3.add_vertex((515, 720))
    right_toe_3.add_vertex((525, 715))
    right_toe_3.filled = True
    window.add(right_toe_3)
    # Mike's hands
    left_arm = GPolygon()
    left_arm.add_vertex((200, 400))
    left_arm.add_vertex((160, 510))
    left_arm.add_vertex((163, 520))
    left_arm.add_vertex((210, 445))
    left_arm.filled = True
    left_arm.fill_color = "darkseagreen"
    left_arm.color = "darkseagreen"
    window.add(left_arm)

    right_arm = GPolygon()
    right_arm.add_vertex((600, 400))
    right_arm.add_vertex((595, 445))
    right_arm.add_vertex((637, 520))
    right_arm.add_vertex((640, 510))
    right_arm.filled = True
    right_arm.fill_color = "darkseagreen"
    right_arm.color = "darkseagreen"
    window.add(right_arm)

    left_hand = GOval(30, 30, x=150, y=498)
    left_hand.filled = True
    left_hand.fill_color = "darkseagreen"
    left_hand.color = "darkseagreen"
    window.add(left_hand)

    right_hand = GOval(30, 30, x=632, y=507)
    right_hand.filled = True
    right_hand.fill_color = "darkseagreen"
    right_hand.color = "darkseagreen"
    window.add(right_hand)
    # Mike's ears
    left_ear = GPolygon()
    left_ear.add_vertex((300, 230))
    left_ear.add_vertex((320, 230))
    left_ear.add_vertex((310, 190))
    left_ear.filled = True
    left_ear.fill_color = "darkseagreen"
    left_ear.color = "darkseagreen"
    window.add(left_ear)

    right_ear = GPolygon()
    right_ear.add_vertex((475, 230))
    right_ear.add_vertex((495, 230))
    right_ear.add_vertex((485, 190))
    right_ear.filled = True
    right_ear.fill_color = "darkseagreen"
    right_ear.color = "darkseagreen"
    window.add(right_ear)
    # texts
    label = GLabel("Uhhhh...", x=270, y=145)
    label.font = "Comic Sans MS-70-bold"
    label.color = "black"
    window.add(label)


if __name__ == '__main__':
    main()
