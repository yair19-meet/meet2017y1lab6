import turtle
turtle.shape('turtle')
square = turtle.clone()
square.shape('square')
square.goto(100, 0)
square.goto(100, 100)
square.goto(0, 100)
square.goto(0, 0)

triangle = turtle.clone()
triangle.shape('triangle')
triangle.goto(300, 0)
triangle.goto(150, 100)
triangle.goto(0, 0)

square.goto(100, 100)
square.goto(300, 300)
square.stamp()
square.goto(100, 100)

triangle.goto(-150, 300)
triangle.stamp()
triangle.goto(-300, 0)


