print("ESCUELA POLITECNICA NACIONAL")
print("PROGRAMACION AVANZADA")
print("NOMBRE: JORDAN SÁNCHEZ")

balonx=400
balony=200
arcox=0
arcoy=100

from tkinter import *

tk = Tk()
tk.config(bg="green")
canvas = Canvas(tk, width=600, height=400)
canvas.pack()
imagen1=PhotoImage(file="balon.png")
canvas.create_image(balonx,balony,ancho=NW, image=imagen1)
imagen2=PhotoImage(file="arco.png")
canvas.create_image(arcox,arcoy,ancho=NW, image=imagen2)

def coor(x,y):
    if y==1:
        x=x+3
    elif y==2:
        x=x-3
    elif y==3:
        x=x-3
    elif y==4:
        x=x+3


def moverimagen(event):
    balonx=400
    balony=200
    arcox=0
    arcoy=100
    if event.keysym == 'Up':
        canvas.move(1, 0, -3)
        coor(balony,1)
    elif event.keysym == 'Down':
        canvas.move(1, 0, 3)
        coor(balony,2)
    elif event.keysym == 'Left':
        canvas.move(1, -3, 0)
        coor(balonx,3)
    else:
        canvas.move(1, 3, 0)
        coor(balonx,4)

        
canvas.bind_all('<KeyPress-Up>', moverimagen)
canvas.bind_all('<KeyPress-Down>', moverimagen)
canvas.bind_all('<KeyPress-Left>', moverimagen)
canvas.bind_all('<KeyPress-Right>', moverimagen)

if balonx==arcox and balony==arcoy:
    print("GOOOL")

tk.mainloop()


