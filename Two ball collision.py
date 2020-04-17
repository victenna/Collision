import turtle,time
wn=turtle.Screen()
wn.bgcolor('violet')
turtle.tracer(2)

t=[]
for i in range(4):
    t.append(turtle.Turtle())
    t[i].hideturtle()
    t[i].up()
   
def scenario(turtle,shapee,size1,size2,clr):
    turtle.shape(shapee)
    turtle.shapesize(size1,size2)
    turtle.color(clr)

scenario(t[0],'circle',1,1,'blue')
scenario(t[1],'circle',1,1,'gold')
scenario(t[2],'arrow',0.5,4,'blue')
scenario(t[3],'arrow',0.5,4,'gold')

t5=turtle.Turtle()
t5.hideturtle()
t5.up()
t5.goto(0,-200)
image='Equation.gif'
wn.addshape(image)
t5.shape(image)
t5.showturtle()

#--------------------------------------------------

#TEXT

TEXT_FONT=('Arial',15,'bold')
text_main=turtle.Turtle()
text_main.color('black')
text_main.hideturtle()
text_main.up()
text_main.setposition(-250,250)
text_main.write('ELASTIC COLLISION of TWO BALLS', font=('Arial',25,'bold'))
text_main.up()
text_main.setposition(-150,200)
text_main.write('m1-->blue, m2-->gold', font=('Arial',25,'bold'))

text_main.up()
text_main.setposition(-230,150)
text_main.write('before collision velocity for blue ball ->U1, \
for gold ball ->U2=0', font=('Arial',15,'bold'))

text_main.up()
text_main.setposition(-230,-120)
text_main.write('after collision velocity for blue ball ->V1,\
for gold ball ->V2', font=('Arial',15,'bold'))

#----------------------------------------------

def collision(size1,size2,angle1,angle2,speed1,speed2,speed3):
    text1=turtle.Turtle()
    text1.hideturtle()
    text1.color('ghostwhite')
    text1.up()
    text1.clear()
    text1.setposition(-150,80)
    if speed1==0:
        text1.write('Two balls with equal masses m1=m2',\
                    font=('Arial',15,'bold'))
    if speed1==-3:
        text1.write('Two balls of different mass, m1<m2',\
                    font=('Arial',15,'bold'))

    if speed2==2:
        text1.write('Two balls of different mass, m1>m2',\
                    font=('Arial',15,'bold'))
        
    t[0].goto(-300,0)
    t[0].shapesize(size1)
    t[0].showturtle()
    
    t[1].goto(0,0)
    t[1].shapesize(size2)
    t[1].showturtle()
    
    t[2].setheading(angle1)
    t[2].goto(-300,-50)
    t[2].showturtle()
    time.sleep(0.5)

    for i in range(62):
        t[0].fd(4)
        t[2].fd(4)
        time.sleep(0.01)
    t[2].hideturtle()
    t[2].setheading(angle2)
    t[2].goto(-40,-50)
    t[2].showturtle()

    t[3].goto(0,-50)
    t[3].showturtle()

    for i in range(280):
        t[0].fd(speed1)
        t[2].fd(speed2)
        if speed1==0:
            t[2].hideturtle()
        t[1].fd(speed3)
        t[3].fd(speed3)
        time.sleep(0.01)
        
    time.sleep(0.5)
    t[0].hideturtle()
    t[1].hideturtle()
    t[2].hideturtle()
    t[3].hideturtle()
    text1.clear()

#-----------------------------------------------------------
    
while True:
    collision(2.5,2.5,0,0,0,0,4)
    collision(1.5,3.5,0,180,-3,3,2)
    collision(3.5,1.5,0,0,2,2,4)
    
    
    

