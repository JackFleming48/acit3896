import turtle

t = turtle.Turtle()
t.speed(0)

def koch(times, length):
    if times == 0:
        t.forward(length)
    else:
        koch(times - 1, length / 3)
        t.left(60)
        koch(times - 1, length / 3)
        t.right(120)
        koch(times - 1, length / 3)
        t.left(60)
        koch(times - 1, length / 3)

times = 2
length = 300

for x in range(3):
    koch(times, length)
    t.right(120)

turtle.done()