import turtle
turtle.speed(10)

x = -80
for y in range(80,241,20):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.forward(160)
y = 240
turtle.right(90)
for x in range (-80,81,20):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.forward(160)
#color filling

for row in range(8):          # 0..7 (top to bottom)
    for col in range(8):      # 0..7 (left to right)
        x = -80 + col * 20
        y = 240 - row * 20
        if (row + col) % 2 == 0:   # alternate squares
            turtle.goto(x, y)      # top-left corner of this square
            turtle.setheading(0)   # ensure forward() goes right
            turtle.pendown()
            turtle.begin_fill()
            turtle.color('black')  # sets both pen and fill colour
            for _ in range(4):
                turtle.forward(20)
                turtle.right(90)
            turtle.end_fill()
            turtle.penup()

turtle.done()    
  
    
