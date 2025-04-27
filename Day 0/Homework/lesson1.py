from turtle import *

#we want to build a house

#step 1: square 
shape("turtle")
width(7)
color("pink")
forward(200)     #house height (y)
left(90)
forward(200)      #house length (x)
left(90)
forward(200)
left(90)
forward(200)


#onto the door
left(90)
forward(50)
color("black")
begin_fill()
left(90)
forward(70)   #door height
right(90)
forward(25)     #door width
right(90)
forward(70)
end_fill()
penup()
goto(200, 200)
pendown()

#roof

color("green")
begin_fill()
right(150)
forward(200)     #roof height
left(120)
forward(200)
end_fill()

#window
color("blue")
penup()
goto(150, 70)
pendown()
left(120)
forward(10)
left(90)
forward(50)     #window height
left(90)
forward(40)     #window length
left(90)
forward(50)
left(90)
forward(40)
left(180)
forward(20)
right(90)
forward(50)
left(180)
forward(25)
right(90)
forward(20)
right(180)
forward(40)

exitonclick()

print("GOA <3")