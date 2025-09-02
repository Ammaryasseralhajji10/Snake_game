from turtle import Turtle

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.all_squares = []
        self.create_snake()
        self.head = self.all_squares[0]
    
    def create_snake(self):
        for position in starting_positions:
            self.add_segment(position)

    def add_segment(self, position):
        new_turtle = Turtle("square")
        new_turtle.penup()
        new_turtle.color("white")
        new_turtle.goto(position)
        self.all_squares.append(new_turtle)
    
    def extend(self):
        #add new segment to the snake
        self.add_segment(self.all_squares[-1].position())

    def move(self):
        for square_num in range(len(self.all_squares) - 1, 0, -1):
            new_x = self.all_squares[square_num - 1].xcor()
            new_y = self.all_squares[square_num - 1].ycor()
            self.all_squares[square_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def reset_snake(self):
        for sq in self.all_squares:
            sq.goto(1000,2000)
        self.all_squares.clear()
        self.create_snake()
        self.head = self.all_squares[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def right(self):
       if self.head.heading() != LEFT:
        self.head.seth(RIGHT)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)
                    






