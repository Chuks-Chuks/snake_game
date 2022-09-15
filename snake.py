import turtle as t


class Snake:
    UP = 90
    DOWN = 270
    LEFT = 180
    RIGHT = 0
    BOUNDARY = 295

    def __init__(self):
        self.x_positions = (0, -20, -40)
        self.segments = []
        self.create_snake()
        self.move_distance = 20
        self.head = self.segments[0]
        self.tail = self.segments[-1]

    def create_snake(self):
        for _ in range(3):
            tim = t.Turtle("square")
            # to tell the snake objects not to draw a line as they move across the screen.
            tim.penup()
            tim.goto(x=self.x_positions[_], y=0)
            self.segments.append(tim)

    def move(self):
        for segment_position in range(len(self.segments) - 1, 0, -1):
            new_x_coordinate = self.segments[segment_position - 1].xcor()
            new_y_coordinate = self.segments[segment_position - 1].ycor()
            self.segments[segment_position].goto(new_x_coordinate, new_y_coordinate)
        self.head.fd(self.move_distance)

    def up(self):
        if self.head.heading() != self.DOWN:
            self.head.setheading(self.UP)

    def down(self):
        if self.head.heading() != self.UP:
            self.head.setheading(self.DOWN)

    def left(self):
        if self.head.heading() != self.RIGHT:
            self.head.setheading(self.LEFT)

    def right(self):
        if self.head.heading() != self.LEFT:
            self.head.setheading(self.RIGHT)

    def add_segment(self):
        tim = t.Turtle("square")
        tim.penup()
        new_x_coordinate = self.tail.xcor()
        new_y_coordinate = self.tail.ycor()
        tim.goto(x=new_x_coordinate, y=new_y_coordinate)
        self.segments.append(tim)

    def easy_level(self):
        if self.head.xcor() > self.BOUNDARY or self.head.xcor() < -self.BOUNDARY:
            if self.head.xcor() > self.BOUNDARY:
                new_x = -1 * int(self.head.xcor() - 20)
            else:
                new_x = -1 * int(self.head.xcor() + 20)
            self.head.goto(new_x, self.head.ycor())

        if self.head.ycor() > 295 or self.head.ycor() < -295:
            if self.head.ycor() > self.BOUNDARY:
                new_y = -1 * int(self.head.ycor() - 10)
            else:
                new_y = -1 * int(self.head.ycor() + 10)
            self.head.goto(self.head.xcor(), new_y)

    def hard_level(self):
        if self.head.xcor() > self.BOUNDARY or self.head.xcor() < -self.BOUNDARY or self.head.ycor() > self.BOUNDARY \
                or self.head.ycor() < -self.BOUNDARY:
            return True
