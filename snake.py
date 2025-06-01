from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40,0)]
MOVE_DISTNACE = 20

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.squares =[]
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
           self.add_square(position)

    def add_square(self, position):
        new_square = Turtle(shape="square")
        new_square.penup()
        new_square.color("white")
        # new_square.setpos(position)
        new_square.goto(position)
        self.squares.append(new_square)

    def extend(self):
        """add a new segment to the snake"""
        self.add_square(self.squares[-1].position())


    def move(self):
        for square_num in range(len(self.squares)-1, 0, -1):
            new_x = self.squares[square_num-1].xcor()
            new_y = self.squares[square_num-1].ycor()
            self.squares[square_num].goto(new_x, new_y)
        self.squares[0].fd(MOVE_DISTNACE)

    def right(self):
        if self.squares[0].heading() != LEFT:
            self.squares[0].setheading(RIGHT)
    
    def left(self):
        if self.squares[0].heading() != RIGHT:
            self.squares[0].setheading(LEFT)
    
    def up(self):
        if self.squares[0].heading() != DOWN:
            self.squares[0].setheading(UP)

    def down(self):
        if self.squares[0].heading() != UP:
            self.squares[0].setheading(DOWN)

