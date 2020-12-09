import turtle,time
wn=turtle.Screen()
wn.setup(1200,700)
turtle.tracer(2)
t1=turtle.Turtle('circle')   #синий шар
t1.color('blue')
t1.hideturtle()
t1.up()
t2=turtle.Turtle('circle')     #желтый шар
t2.color('gold')
t2.hideturtle()
t2.up()
t3=turtle.Turtle('arrow')    #стрелка синего шара
t3.hideturtle()
t3.up()
t3.color('blue')
t3.shapesize(0.5,4)
t4=turtle.Turtle('arrow')     #стрелка желтого шара
t4.up()
t4.color('gold')
t4.shapesize(0.5,4)
t4.hideturtle()
t5=turtle.Turtle()    # Equation image
t5.hideturtle()
t5.up()
image='Equation.gif'
wn.addshape(image)
t5.shape(image)
t5.goto(0,-200)
def motion1(size1,size2):
    t1.shapesize(size1)
    t1.setheading(0)#!!
    t1.goto(-300,0)
    t1.showturtle()
    t3.setheading(0)#!!
    t3.goto(-300,-50)
    t3.showturtle()
    t2.shapesize(size2)
    t2.goto(0,0)
    t2.showturtle()
    t4.hideturtle()#!!
    time.sleep(0.5)#!!
    for i in range(62):
        t1.fd(4)
        t3.fd(4)
        time.sleep(0.01)
def motion2(step1,step2):
    for i in range(320):
        t1.fd(step1)
        t3.fd(step1)
        t2.fd(step2)
        t4.fd(step2)
        time.sleep(0.01)
  
while True:
    #Столкновение шаров одинаковой массы)
    wn.bgpic('Image1.gif')
    motion1(2.5,2.5)
    t3.hideturtle()
    t4.goto(0,-50)
    t4.showturtle()
    motion2(0,4)
    #Масса синего шара меньше
    wn.bgpic('Image2.gif')
    t3.clear()
    t4.clear()
    motion1(1.5,3.5)
    t1.setheading(180)
    t3.setheading(180)
    t4.goto(0,-50)
    t4.showturtle()
    motion2(4,2)
    #Масса синего шара больше
    wn.bgpic('Image3.gif')
    t3.clear()
    t4.clear()
    motion1(3.5,1.5)
    t4.goto(0,-50)
    t4.showturtle()
    motion2(2,4)
    time.sleep(0.05)



