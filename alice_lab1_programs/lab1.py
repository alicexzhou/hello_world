#Alice Zhou
#CS111, Lab 1
#lab1.py

from cs1graphics import *

paper = Canvas(500, 500, "yellow") #default 200 by 200
face = Rectangle(250, 300, Point(250, 250))
face.setFillColor("bisque")
paper.add(face)

leftEye = Circle(25, Point(200, 200))
leftEye.setFillColor("blue")
paper.add(leftEye)

rightEye = Circle(25, Point(300, 200))
rightEye.setFillColor("blue")
paper.add(rightEye)

nose = Polygon(Point(250, 250), Point(230, 280), Point(270, 280))
nose.setFillColor("orange")
paper.add(nose)

mouth = Rectangle(80, 30, Point(250, 330))
mouth.setFillColor("red")
paper.add(mouth)

lightning = Path(Point(252, 186), Point(272, 160), Point(242, 146), Point(262, 126))
lightning.setBorderColor("yellow")
lightning.setBorderWidth(5)
paper.add(lightning)

roundHead = Ellipse(250, 50, Point(250, 100))
roundHead.setFillColor("bisque")
roundHead.setDepth(30)
paper.add(roundHead)