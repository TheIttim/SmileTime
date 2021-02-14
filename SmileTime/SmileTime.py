import turtle
import tkinter as tk

root= tk.Tk()
root.title('Smile Time!')
root.iconbitmap('../SmileTime.ico')
canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()
    

def smiley():
    turtle.hideturtle()
    turtle.reset()
    turtle.hideturtle()
    turtle.pensize(5)
    #Head
    turtle.fillcolor('yellow')
    turtle.begin_fill()
    turtle.circle(150)
    turtle.end_fill()
    #Left Eye
    turtle.penup()
    turtle.goto(-75, 150)
    turtle.pendown()
    turtle.fillcolor('black')
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()
    #Right Eye
    turtle.penup()
    turtle.goto(0, 0)
    turtle.goto(75, 150)
    turtle.pendown()
    turtle.fillcolor('black')
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()
    #Face
    turtle.penup()
    turtle.goto(0, 0)
    turtle.goto(-70, 100)
    turtle.pendown()
    turtle.right(90)
    turtle.fillcolor('black')
    turtle.begin_fill()
    turtle.circle(75, 180)
    turtle.end_fill()
    turtle.done()

button1 = tk.Button(text='It\'s Smile Time',command=smiley, bg='brown',fg='white')
canvas1.create_window(150, 150, window=button1)

root.mainloop()