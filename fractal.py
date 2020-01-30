import turtle
from random import randint
try:
    from Tkinter import *
except:
    from tkinter import *
import sys




##   global   ###################################
lvl = 6
s_len = 250
lenn=0
angle=0
wth = 10
#shit="lf rf ,150, 30"
#random = 0
#################################################


def percentage(percent, whole):
    return (percent*whole)/100

def get_angle():
    if angle=='r':
        return randint(10, 70);
    else:
        return angle

def get_len(len):
    if len=='r':
        num1=int(percentage(50, len))
        num2=int(percentage(80, len))
        ret=randint(num1, num2)
        del num1
        del num2
        return ret
    else:
        return len*2.0/3.0


def shit_tree(width, length, level):
    wth=width*3.0/4.0
    t.width(wth)
    turn = ""
    actions = []
    actions.clear()

    for char in shit:
        if char == "l":
            angle=get_angle()
            t.left(angle)
            actions.append(("l", angle))
        elif char == "r":
            angle=get_angle()
            t.right(angle)
            actions.append(("r", angle))
        elif char == "f":
            lenn=get_len(length)
            t.fd(lenn)
            actions.append(("f", lenn))
        elif char == "+":
            if level < lvl:
                shit_tree(wth, lenn, level+1)
            t.width(wth)
        elif char == " ":
            for action, num in reversed(actions):
                if action == "l":
                    t.right(num)
                elif action == "r":
                    t.left(num)
                elif action == "f":
                    t.back(num)
            actions.clear()
            try:
                del angle
            except:
                pass
            try:
                del lenn
            except:
                pass



def on_closing():
    root.destroy()
    turtle.bye()


def gui():
    global root, e_pattern, e_lvl, e_len, e_angle
    root=Tk()
    ll=Label(root,text="Pattern")
    ll.config(font=("Courier", 16))
    ll.pack()
            
    e_pattern=Entry(root, justify='center')
    e_pattern.config(font=("Courier", 16))
    e_pattern.insert(END, "lf+ ff+ rf+ ")
    e_pattern.pack()

    ll=Label(root,text="Level")
    ll.config(font=("Courier", 16))
    ll.pack()     
    e_lvl=Entry(root, justify='center')
    e_lvl.config(font=("Courier", 16))
    e_lvl.insert(END, "6")
    e_lvl.pack()

    ll=Label(root,text="Lenght")
    ll.config(font=("Courier", 16))
    ll.pack()
    e_len=Entry(root, justify='center')
    e_len.config(font=("Courier", 16))
    e_len.insert(END, "r")
    e_len.pack()

    ll=Label(root,text="Angle")
    ll.config(font=("Courier", 16))
    ll.pack()    
    e_angle=Entry(root, justify='center')
    e_angle.config(font=("Courier", 16))
    e_angle.insert(END, "r")
    e_angle.pack()

    ll=Label(root,text="")
    ll.config(font=("Courier", 8))
    ll.pack()    
    b=Button(root,text='Confirm',command=start)
    b.config(font=("Courier", 16))
    b.pack()
    ll=Label(root,text="")
    ll.config(font=("Courier", 8))
    ll.pack()

    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.eval('tk::PlaceWindow %s center' % root.winfo_pathname(root.winfo_id()))
    root.mainloop()










def main():
    global t
    #tmp=pattern.split(",")
    #shit = pattern
    print(shit)
    print(lvl)
    print(lenn)
    print(angle)

    t = turtle.Turtle(shape="circle")
    s = turtle.Screen()
    ##   preparing   ################################
    turtle.bgcolor("black")
    t.shapesize(.2, .2, .1)
    t.hideturtle()
    t.penup()
    t.goto(0.00, 40-s.window_height()/2)
    t.pendown()
    t.showturtle()
    t.color("white", "cyan")
    t.left(90)
    t.speed('fastest')
    #################################################
    length=get_len(s_len)
    t.width(wth)
    t.fd(length)
    shit_tree(wth, length, 2)
    #tree(wth, length, 2)
    turtle.done()


def fun(x,y):
    t.reset()
    s.resetscreen()
    gui()


def start():
    global s_len, lvl, lenn, angle, shit
    global t, s
    shit = e_pattern.get()
    lvl = int(e_lvl.get())
    lenn = e_len.get()
    if lenn != 'r':
        s_len = int(lenn)
        lenn = int(lenn)
    angle = e_angle.get()
    if angle != 'r':
        angle = int(angle)
    root.destroy()
    
    print(shit)
    print(lvl)
    print(lenn)
    print(angle)

    t = turtle.Turtle(shape="circle")
    s = turtle.Screen()
    ##   preparing   ################################
    turtle.bgcolor("black")
    s.onscreenclick(fun)
    t.shapesize(.2, .2, .1)
    t.hideturtle()
    t.penup()
    t.goto(0.00, 40-s.window_height()/2)
    t.pendown()
    t.showturtle()
    t.color("white", "cyan")
    t.left(90)
    t.speed('fastest')
    #################################################
    length=get_len(s_len)
    t.width(wth)
    t.fd(length)
    shit_tree(wth, length, 2)
    #tree(wth, length, 2)
    turtle.done()


gui()
