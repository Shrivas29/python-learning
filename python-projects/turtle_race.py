from turtle import Turtle,Screen


screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="bet on",prompt="place a bet on a color and enter that color")
print(user_bet)
colors = ["blue","red","yellow","purple","brown","black"]


## tim
tim = Turtle(shape = "turtle")
tim.color(colors[0])
tim.penup()
tim.goto(x= -230,y= -100)

##timmy
timmy = Turtle(shape = "turtle")
timmy.color(colors[1])
timmy.penup()
timmy.goto(x= -230,y= -90)

##goat
goat = Turtle(shape = "turtle")
goat.color(colors[2])
goat.penup()
goat.goto(x= -230,y= -80)

##week
week = Turtle(shape = "turtle")
week.color(colors[3])
week.penup()
week.goto(x= -230,y= -70)

##best
best = Turtle(shape = "turtle")
best.color(colors[4])
best.penup()
best.goto(x= -230,y= -60)

##pop
## tim
pop = Turtle(shape = "turtle")
pop.color(colors[5])
pop.penup()
pop.goto(x= -230,y= -50)


screen.exitonclick()