import turtle

t = turtle.Turtle()
t.pencolor("red")
t.pensize(2)
t.speed(1)
points = [(-300,-300),(300,-300), (0,250)]

def get_mid(p,q):
    return ((p[0] + q[0])/2, (p[1] + q[1])/2)

def triangele(points, n):
    t.penup()
    t.goto(*points[0])
    t.pendown()
    t.goto(*points[1])
    t.goto(*points[2])
    t.goto(*points[0])

    if n > 0:
        triangele([points[0], get_mid(points[0], points[1]),
                   get_mid(points[0], points[2])], n-1)
        triangele([get_mid(points[0], points[1]), points[1],
                   get_mid(points[1], points[2])], n - 1)
        triangele([get_mid(points[0], points[2]),
                   get_mid(points[1], points[2]), points[2]], n - 1)

triangele(points, 3)

turtle.mainloop()
