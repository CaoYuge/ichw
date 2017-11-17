import turtle
import threading

wn = turtle.Screen()
wn.bgcolor("black")

def draw_a_ellipse(s,a,b,c,t):
    s.speed(c-1)
    s.penup()
    s.goto(0+t,-b)
    s.pendown()
    s.speed(c)
    for adjustment in range(4):
        adjustmentx = [0+t,a+t,0+t,-a+t]
        adjustmenty = [-b,0,b,0]
        s.goto(adjustmentx[adjustment],adjustmenty[adjustment])
        for i in range(90):
            pos = s.pos()
            x = float(pos[0])-t
            y = float(pos[1])
            a1 = b**4
            a2 = a**4
            a3 = a1*(x**2) + a2*(y**2)
            a4 = a3**1.5
            a5 = a1*a2
            r = a4/a5
            s.circle(r,1)
    s.goto(0+t,-b)
a = turtle.Turtle()
b = turtle.Turtle()
c = turtle.Turtle()
d = turtle.Turtle()
e = turtle.Turtle()
f = turtle.Turtle()
g = turtle.Turtle()

for i in range(7):
    n = [a,b,c,d,e,f,g]
    m = ["red","blue","purple","white","red","green","yellow"]
    n[i].color(m[i])

g.dot(10)

for i in [a,b,c,d,e,f]:
    i.shape("circle")

g.hideturtle()

threads = []
t1 = threading.Thread(target=draw_a_ellipse,args=(a,50,40,1,30))
threads.append(t1)
t2 = threading.Thread(target=draw_a_ellipse,args=(b,130,120,1,50))
threads.append(t2)
t3 = threading.Thread(target=draw_a_ellipse,args=(c,75,72,1,21))
threads.append(t3)
t4 = threading.Thread(target=draw_a_ellipse,args=(d,100,80,1,60))
threads.append(t4)
t5 = threading.Thread(target=draw_a_ellipse,args=(e,120,80,1,90))
threads.append(t5)
t6 = threading.Thread(target=draw_a_ellipse,args=(f,160,140,1,78))
threads.append(t6)

for t in threads:
    t.setDaemon(True)
    t.start()

wn.exitonclick()