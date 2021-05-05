import turtle
import time
import random

HEIGHT,WIDTH=500,500
COLOURS=["red","green","blue","orange","yellow","black","purple","pink","brown","cyan"]

def number_of_turtles():
    num=0
    while True:
        num = input("Enter the number of turtles(2-10):")
        if num.isdigit():
            num=int(num)
            if (2<= num <=10):
                return num
            
            print("Invalid number of input Try again")
            continue
            
        else:
            print("Invalid input Try again") 
            continue  

def race(colours,var):
    turtles=create_turtles(colours,var)
    
    while True:
        for racer in turtles:
            distance=random.randrange(10,20)
            racer.fd(distance)

            x,y=racer.pos()
            if y>=HEIGHT//2-30:
                return colours[turtles.index(racer)]



def create_turtles(colours,var):
    turtles=[]
    spacingx=WIDTH//(var+1)
    for i,colour in enumerate(colours):
        racer=turtle.Turtle()
        racer.color(colour)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2+(i+1)*spacingx,-HEIGHT//2+20)
        racer.pendown()
        turtles.append(racer)
    return turtles

def init_turtle():
    screen=turtle.Screen()
    screen.setup(HEIGHT,WIDTH)
    screen.title("Turtle Race!")

var=number_of_turtles()
init_turtle()

random.shuffle(COLOURS)
colours=COLOURS[:var]
winner=race(colours,var)
time.sleep(5)
print("The winnner of the turtle race is the colour with ",winner)