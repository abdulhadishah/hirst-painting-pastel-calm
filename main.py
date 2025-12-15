import random
from turtle import Turtle, Screen, colormode

colormode(255)

screen = Screen()
screen.title("Hirst Painting - Pastel Calm")
screen.bgcolor(228, 228, 222)


color_palette = [
    (214, 168, 166),  # dusty rose
    (170, 204, 198),  # muted teal
    (182, 176, 212),  # soft lavender
    (192, 210, 184),  # sage green
    (232, 190, 174),  # peach clay
    (205, 185, 210),  # mauve
    (176, 196, 222),  # soft steel blue
    (228, 216, 168),  # warm sand yellow
    (198, 186, 170),  # taupe
    (176, 204, 196),  # eucalyptus
]

# dot size = 20
# dots per row = 10
# spacing = 50

painter = Turtle()
colormode(255)
painter.speed("fastest")
painter.penup()
painter.hideturtle()

start_y = -250


def draw_row(y):
    start_x = -250
    for _ in range(10):
        painter.setpos(start_x, y)
        painter.dot(20, random.choice(color_palette))
        start_x += 50


for _ in range(10):
    draw_row(start_y)
    start_y += 50

screen.exitonclick()
