import turtle
flower = turtle.Turtle()
flower.color('blue')
flower.speed(0)

window = turtle.Screen()
window.bgcolor('bisque')


for i in range (0,50):      
    flower.right(60)
    flower.forward(50)
    flower.right(60)
    flower.forward(50)
    flower.right(120)
    flower.forward(50)
    flower.right(60)
    flower.forward(50)
    flower.right(60)
    flower.right(7.2)
flower.color('green')
flower.right(90)
flower.forward(300)

window.exitonclick()

