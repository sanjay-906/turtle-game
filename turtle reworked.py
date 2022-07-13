# Write your code here :-)
# Write your code here :-)
from turtle import Turtle
from random import randint

#creating the objects
a1=Turtle()
a2=Turtle()
a3=Turtle()
a4=Turtle()
a5=Turtle()

#assigning the colors to the object
a1.color('red')
a2.color('orange')
a3.color('purple')
a4.color('green')
a5.color('blue')

#adding shape of the object
a1.shape('turtle')
a2.shape('turtle')
a3.shape('turtle')
a4.shape('turtle')
a5.shape('turtle')

#moving the objects to the starting point of the race
a1.penup()
a1.goto(-300,50)
a1.pendown()
a2.penup()
a2.goto(-300,70)
a2.pendown()
a3.penup()
a3.goto(-300,90)
a3.pendown()
a4.penup()
a4.goto(-300,110)
a4.pendown()
a5.penup()
a5.goto(-300,130)
a5.pendown()

#testing:
#x1,x2,x3,x4,x5=10,2,3,4,50

x1=randint(1,8)
x2=randint(1,8)
x3=randint(1,8)
x4=randint(1,8)
x5=randint(1,8)

b={"red":x1,"orange":x2,"purple":x3,"green":x4,"blue":x5}
x=input(str("which horse do you place the bet?(type color):"))
#starting the race

for i in range (50):
    a1.forward(x1)    #(randint(1,8))
    a2.forward(x2)     #(randint(1,8))
    a3.forward(x3)         #(randint(1,8))
    a4.forward(x4)    #(randint(1,8))
    a5.forward (x5)          #(randint(1,8))

maxt = max(x1,x2,x3,x4,x5)
if b[x]==maxt:
    print("you won!")
else:

    print("you lost")
