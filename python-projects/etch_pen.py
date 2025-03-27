from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()



def move_forward():
    tim.forward(10)
def move_backward():
    tim.backward(10)
def move_rigth():
    new_headinng = tim.heading() - 10
    tim.setheading(new_headinng)
def move_left():
    new_headinng = tim.heading() + 10
    tim.setheading(new_headinng)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(move_forward,"w")
screen.onkey(move_backward,"s")
screen.onkey(move_rigth,"d")
screen.onkey(move_left,"a")
screen.onkey(clear,"c")
screen.exitonclick()