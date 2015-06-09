import tkinter
import random
WIDTH , HEIGHT = map(int,input().split())
field = [["1" for i in range(HEIGHT)] for i in range(WIDTH)]

c = tkinter.Canvas( width = (WIDTH+1) * 20, heigh = (HEIGHT+1)*20)
c.pack()


def divider(lt , pc):
    pc = pc - 1
    lt = lt - 1

    proport = []

    devire = [0]*(pc+2)
    devire[pc+1] = lt
    s = 0
  
    for j in range(pc):
        proport.append(random.randint(5 , 10))
        s += proport[j]
   
    for i in range(pc):
        devire[i+1] = int(devire [i] + lt // (s / proport[i]))
    return(devire)

def walker_main(x1 , y1 , x2 , y2): 
    global field 
    global WIDTH 
    global HEIGHT
    x1 , x2 = min(x1 , x2) , max(x1 , x2)
    y1 , y2 = min(y1 , y2) , max(y1 , y2)

    cs = divider((x2-x1) , int((((x1-x2)**2 + (y1-y2)**2)**0.5) // 5 + 1))
    for k in range(len(cs)):
        cs[k] += x1
    ys = [random.randint(2 , (HEIGHT-1)) for y in range(len(cs))]

    for i in range(len(cs) - 1):
        for h in range(cs[i+1] - cs[i] + 1):
            field[cs[i] + h - 1][ys[i] - 1] = "0"
    for i in range(len(ys) - 1):
        if ys[i+1] - ys[i] > 0:
            for h in range(ys[i+1] - ys[i]):
                field[cs[i + 1] - 1][ys[i] + h - 1] = "0"
        else:
            for h in range(ys[i] - ys[i+1]):
                field[cs[i + 1] - 1][ys[i] - h - 1] = "0"

    for i in range(HEIGHT):
            if field[-2][i] == '0':
                if field[-2][i+1] == '1':
                    if field[-2][i-1] == '0':
                        field[-1][i-1] = '0'
                    elif field[-2][i-1] == '1':
                        field[-1][i] = '0'

        for x in range(1,WIDTH-2):
            for y in range(1,HEIGHT-1):
                a = []
                counter = 0
                a.append(field[x-1][y])
                a.append( field[x+1][y])
                a.append( field[x][y-1])
                a.append( field[x][y+1])
                for i in range(len(a)):
                    if a[i] =='0':
                        counter += 1
                if counter == 1:
                    field[x][y] = '0'

walker_main(1, 1, WIDTH, HEIGHT)

printer = [[0 for i in range(WIDTH)] for i in range(HEIGHT)]
for i in range(WIDTH):
    for j in range(HEIGHT):
        printer[j][i] = field[i][j]
for n in printer:
    print(n)
    
def painter():
    global HEIGHT
    global WIDTH
    global c
    global field

    for x in range(WIDTH):
        for y in range(HEIGHT):
            if field[x][y] =='1':
                c.create_rectangle(20 *x, 20 *y, 20 * x + 20, 20*y + 20, fill = "blue")
            elif field[x][y] == '0':
                c.create_rectangle(20 *x, 20 *y, 20 * x + 20, 20*y + 20, fill = "white")
painter()
c.mainloop()

