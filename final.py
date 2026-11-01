import turtle as t
import math as m
import random as r
import time as ti

wn=t.Screen()
wn.tracer(0)
angles=[0,0]
points=[]
#list
polies=[[-10,10,-10],[-10,0,-10],[0,0,-10],[0,10,-10],[-10,10,-10]],[[-10,10,-10],[0,10,-10],[0,10,20],[-10,10,20],[-10,10,-10]],[[-10,10,20],[-10,0,20],[0,0,20],[0,10,20],[-10,10,20]],[[-10,0,-10],[0,0,-10],[0,0,20],[-10,0,20],[-10,0,-10]],[[20,-20,20],[-30,-20,20],[-30,30,20],[20,30,20],[20,-20,20]],[[-30,30,40],[-30,30,20],[20,30,20],[20,30,40],[-30,30,40]],[[-30,-20,40],[-30,-20,20],[20,-20,20],[20,-20,40],[-30,-20,40]],[[20,-20,40],[-30,-20,40],[-30,30,40],[20,30,40],[20,-20,40]],[[10,-10,50],[10,-10,40],[10,20,40],[10,20,50],[10,10,50],[10,10,60],[10,0,60],[10,0,50],[10,-10,50]],[[-20,-10,50],[-20,-10,40],[-20,20,40],[-20,20,50],[-20,10,50],[-20,10,60],[-20,0,60],[-20,0,50],[-20,-10,50]],[[-20,-10,50],[-20,-10,40],[10,-10,40],[10,-10,50],[0,-10,50],[0,-10,60],[-10,-10,60],[-10,-10,50],[-20,-10,50]],[[-20,20,50],[-20,20,40],[10,20,40],[10,20,50],[0,20,50],[0,20,60],[-10,20,60],[-10,20,50],[-20,20,50]],[[-20,20,50],[-10,20,50],[-10,10,50],[-20,10,50],[-20,20,50]],[[0,20,50],[10,20,50],[10,10,50],[0,10,50],[0,20,50]],[[-20,0,50],[-10,0,50],[-10,-10,50],[-20,-10,50],[-20,0,50]],[[0,0,50],[10,0,50],[10,-10,50],[0,-10,50],[0,0,50]],[[0,0,60],[0,0,50],[10,0,50],[10,0,60],[0,0,60]],[[0,10,60],[0,10,50],[10,10,50],[10,10,60],[0,10,60]],[[-20,0,60],[-20,0,50],[-10,0,50],[-10,0,60],[-20,0,60]],[[-20,10,60],[-20,10,50],[-10,10,50],[-10,10,60],[-20,10,60]],[[0,0,60],[10,0,60],[10,10,60],[0,10,60],[0,20,60],[-10,20,60],[-10,10,60],[-20,10,60],[-20,0,60],[-10,0,60],[-10,-10,60],[0,-10,60],[0,0,60]]
#input
demo=str(input("Demo mode?(y/n)"))
demo="y" in demo
if not demo:
    drawa=str(input("What draw mode? Pointcloud(p), Wireframe(w), Filled(f)\nWarning: filled mode is buggy\n"))
    move=str(input("What camera mode? Animated(a), Manual(m)\n"))
    if move=="a":
        move1=float(input("How many degrees per tick to the right?"))
        move2=float(input("How many degrees per tick up?"))
        ang1=int(input("Start how many degrees to the right?"))
        ang2=int(input("Start how many degrees up?"))
        angles=[ang1,ang2]
        tx=int(input("translate x?"))
        ty=int(input("translate y?"))

    if move=="m":
        print("Controls:\n   W: move camera up\n   A: move camera left\n   S: move camera down\n   D: move camera right")
else:
    drawa="w"
    move="a"
    move1=0.15
    move2=0
    angles=[0,20]
    tx=15
    ty=0
allturts=[]
t.tracer(0)

def retx(point):
    global angles
    return m.cos(m.radians(angles[0]))*point[0]*5+m.sin(m.radians(angles[0]))*point[1]*5+tx
def rety(point):
    global angles
    return (m.sin(m.radians(angles[1]))*m.sin(m.radians(angles[0]))*point[0] - m.sin(m.radians(angles[1]))*m.cos(m.radians(angles[0]))*point[1] + m.cos(m.radians(angles[1]))*point[2])*5+ty
#procedure
pen=t.Turtle()
pen.hideturtle()
def draw_poly(poly,pen):
    
    pen.penup()
            
    pen.fillcolor((r.randint(100,255)/255,r.randint(100,255)/255,r.randint(100,255)/255))
    #pen.goto((m.cos(m.radians(angles[0]))*poly[0][0]+m.sin(m.radians(angles[0]))*poly[0][1]*10,(m.cos(m.radians(angles[1]))*(poly[0][2])+(1-m.cos(m.radians(angles[1])))*(poly[0][0]+poly[0][1]))*10))
    
    
    pen.goto(retx(poly[0]),rety(poly[0]))
    if drawa=="f":
        pen.begin_fill()
    
    for point in poly:
        
        pen.pendown()
        pen.goto(retx(point),rety(point))
    if drawa=="f":
        pen.end_fill()
    pen.penup()
    pen.speed(0)
    
def draw():
    if drawa=="p":
        for point in points:
            poin=t.Turtle()
            
            poin.penup()
            poin.speed(0)
            #ex=m.cos(m.radians(angles[0]))*point[0]*10+m.sin(m.radians(angles[0]))*point[1]*10
            #why=(m.sin(m.radians(angles[1]))*m.sin(m.radians(angles[0]))*point[0] - m.sin(m.radians(angles[1]))*m.cos(m.radians(angles[0]))*point[1] + m.cos(m.radians(angles[1]))*point[2])*10
            poin.goto(retx(point),rety(point))
            
            allturts.append(poin)
    
    if (drawa in "fw"):
        
        wn.tracer(0,1)
        
        
        
        pen.speed(0)
        for poly in polies:
            draw_poly(poly,pen)
        
        t.update()
        pen.clear()
        pen.penup()
        
        

while move=="a":
    
    
    if False:
        for i in allturts:
            i.hideturtle()
            i.clear()
            i=0
        
        
    
    
    angles[0]+=move1
    angles[1]+=move2
    draw()
    
    
def horizontaleft():
    
    
    angles[0]+=1
    #call to procedure
    draw()
    
    ti.sleep(0.01)
    wn.onkeypress(horizontaleft,"a")
    wn.onkeypress(horizontalright,"d")
    wn.onkeypress(vertup,"w")
    wn.onkeypress(vertdown,"s")
    wn.listen()

def horizontalright():
    
    
    angles[0]-=1
    draw()
    
    ti.sleep(0.01)
    wn.onkeypress(horizontaleft,"a")
    wn.onkeypress(horizontalright,"d")
    wn.onkeypress(vertup,"w")
    wn.onkeypress(vertdown,"s")
    wn.listen()

def vertup():
    
    
    angles[1]+=1
    draw()
    
    ti.sleep(0.01)
    wn.onkeypress(horizontaleft,"a")
    wn.onkeypress(horizontalright,"d")
    wn.onkeypress(vertup,"w")
    wn.onkeypress(vertdown,"s")
    wn.listen()

def vertdown():
    
    
    angles[1]-=1
    draw()
    
    ti.sleep(0.01)
    wn.onkeypress(horizontaleft,"a")
    wn.onkeypress(horizontalright,"d")
    wn.onkeypress(vertup,"w")
    wn.onkeypress(vertdown,"s")
    wn.listen()
wn.listen()
#more input
wn.onkeypress(horizontaleft,"a")
wn.onkeypress(horizontalright,"d")
wn.onkeypress(vertup,"w")
wn.onkeypress(vertdown,"s")


wn.listen()
imnh=input()
