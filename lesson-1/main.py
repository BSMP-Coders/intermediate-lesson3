import turtle

# Set up the turtle window
turtle.title("Basic Turtle Application")
turtle.bgcolor("lightblue")

# Create a turtle and draw a simple square
t = turtle.Turtle()
t.color("darkgreen")
t.pensize(3)

for _ in range(4):
    t.forward(100)
    t.right(90)

# Keep the window open until closed by the user
# Add a simple interactive game: click inside the square to change its color

def change_color(x, y):
    # Check if click is inside the square (100x100, starting at center)
    if -50 < x < 50 and -50 < y < 50:
        t.color("orange")
        t.fillcolor("yellow")
        t.begin_fill()
        for _ in range(4):
            t.forward(100)
            t.right(90)
        t.end_fill()
        t.color("darkgreen")  # Reset outline color

# Listen for mouse clicks
turtle.onscreenclick(change_color)

turtle.done()