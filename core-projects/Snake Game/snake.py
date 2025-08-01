from turtle import Turtle

MOVE_DIST = 20
up= 90
down=270
left=180
right=0
Starting_Position = (0,0), (-20, 0), (-40,0)


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in Starting_Position:
            self.add_segment(i)

    def add_segment(self, position):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Motion of segments to next segment (from last) before moving"""
        for seg_num in range(len(self.segments)-1, 0, -1):
            x = self.segments[seg_num-1].xcor()
            y=self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(x,y)
        self.head.fd(MOVE_DIST)

    def up(self):
        if self.head.heading()!= down:
            self.head.setheading(up)
    def down(self):
        if self.head.heading()!= up:
            self.head.setheading(down)
    def left(self):
        if self.head.heading()!= right:
            self.head.setheading(180)
    def right(self):
        if self.head.heading()!= left:
             self.head.setheading(0)

    def reset(self):
        for seg in self.segments:
            seg.goto(100,1505)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
