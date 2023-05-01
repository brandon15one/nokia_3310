from turtle import Turtle, Screen


class SnakeHead:
    def __init__(self):
        self.image = "snake.png"

        self.screen = Screen()
        self.screen.bgcolor('green')
        self.screen.register_shape(image)

        self.turtle = Turtle(shape=image)

        self.screen.mainloop()
