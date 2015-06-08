import random
import tkinter

WIDTH , HEIGHT = map(int,input().split())
field = [[1 for i in range(HEIGHT)] for i in range(WIDTH)]

c = tkinter.Canvas( width = (WIDTH+1) * 25, heigh = (HEIGHT+1)*25)
c.pack()


def painter(field):
    global HEIGHT
    global WIDTH
    global c

    for x in range(0, WIDTH*25,25):
        for y in range(0, HEIGHT*25,25):

            for i in field:
                for j in i:
                    if j:
                        c.create_rectangle(x+25, y+25, x+ 2*25, y+ 2*25, fill = "blue")
                    else:
                        c.create_rectangle(x+ 25, y+25, x+ 2*25, y+ 2*25, fill = "white")

def walker(x1 , y1 , x2 , y2):
    
    global field
    global WIDTH
    global HEIGHT
    x_3 = (x1 + x2) // 2
    y_3 = (y1 + y2) // 2
    y_3 = (y1 + y2) // 2
    
    if ((x1 - x2) // 4) - ((x2 - x1) // 4) < -1:
        x3 = x_3 + random.randint(((x1 - x2) // 4 - 1) , ((x2 - x1) // 4 + 1))
    else:
        x3 = x_3 + random.randint(((x2 - x1) // 4 - 1) , ((x1 - x2) // 4 + 1))
        
    if ((y1 - y2) // 4) - ((y2 - y1) // 4) < 3:
        y3 = y_3 + random.randint(((y1 - y2) // 4 - 1) , ((y2 - y1) // 4 + 1))
    else:
        y3 = y_3 + random.randint(((y2 - y1) // 4 - 1) , ((y1 - y2) // 4 + 1))

    if x3 > WIDTH - 2:
        x3 = WIDTH - 2 
    if y3 > HEIGHT - 2:
        y3 = HEIGHT - 2
    if x3 < 1:
        x3 = 1
    if y3 < 1:
        y3 = 1
        
    field[x3][y3] = 0
    if (x1 - x2)**2 > 0 or (y1 - y2)**2 > 0:
        if (x1 - x3)**2 > 1 or (y1 - y3)**2 > 1:
            walker(x1 , y1 , x3 , y3)
        if (x2 - x3)**2 > 1 or (y2 - y3)**2 > 1:
            walker(x3 , y3 , x2 , y2)

walker(0, 4, 11, 6)
painter(field)
c.mainloop()
