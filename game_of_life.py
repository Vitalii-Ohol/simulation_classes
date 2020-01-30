try:
    from Tkinter import Frame, Canvas, Tk, Button, LEFT, RIGHT, Variable, Checkbutton,Entry
    #from Tkinter import *
except:
    from tkinter import Frame, Canvas, Tk, Button, LEFT, RIGHT, Variable, Checkbutton,Entry
    #from tkinter import *
##try:
##    import ttk
##except:
##    from tkinter import ttk
##s=ttk.Style()
##print(s.theme_names())
##s.theme_use('alt')

survive_rule = [2,3]
born_rule = [3]


live_color = "black"
dead_color = "white"
grid_size = 70
cell_size = 10






def get_neighbours(x, y):
    return {((x + dx)%grid_size, (y + dy)%grid_size) for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]}

def is_survivor(universe, x, y):
    if(len(get_neighbours(x, y) & universe)==0):
        print("error "+str(x)+":"+str(y)+"      "+str(len(get_neighbours(x, y) & universe)))
        print("survive: "+str(len(get_neighbours(x, y) & universe) in survive_rule))
    return len(get_neighbours(x, y) & universe) in survive_rule

def is_born(universe, x, y):
    if(len(get_neighbours(x, y) & universe)==0):
        print("error "+str(x)+":"+str(y)+"      "+str(len(get_neighbours(x, y) & universe)))
        print("born: "+str(len(get_neighbours(x, y) & universe) in born_rule))
    return len(get_neighbours(x, y) & universe) in born_rule

def step(universe):
    survivors = { (x, y) for x, y in universe if is_survivor(universe, x, y) }
    survivors = { (x%grid_size, y%grid_size) for x, y in survivors}
    list_of_neighbour_sets = [get_neighbours(x, y) for x, y in universe]
    flattened_neighbour_set = {item for subset in list_of_neighbour_sets for item in subset}
    births = { (x, y) for x, y in flattened_neighbour_set if is_born(universe, x, y) }
    births = { (x%grid_size, y%grid_size) for x, y in births}
    dead = flattened_neighbour_set - survivors - births
    dead = { (x%grid_size, y%grid_size) for x, y in dead}
    return survivors | births, dead

def create_grid():
    x = 10
    y = 10
    global rectangles
    rectangles = []
    for i in range(grid_size):
        rectangles.append([])
        for j in range(grid_size):
            rect = canvas.create_rectangle(x, y, x+cell_size, y+cell_size, fill=dead_color)
            rectangles[i].append(rect)
            x += cell_size
        x = 10
        y += cell_size

def change_colour_on_click(event):
    x, y = event.x, event.y
    x, y = x-x%cell_size, y-y%cell_size
    try:
        iy = int(x / cell_size - 1)
        ix = int(y / cell_size - 1)
        if ix == -1 or iy == -1:
            raise IndexError
        if (ix, iy) in universe:
            universe.remove((ix, iy))
            canvas.itemconfig(rectangles[ix][iy], fill=dead_color)
        else:
            universe.add((ix, iy))
            canvas.itemconfig(rectangles[ix][iy], fill=live_color)
        print(universe)
    except IndexError:
        return

def fill_on_click(event):
    x, y = event.x, event.y
    x, y = x-x%cell_size, y-y%cell_size
    try:
        iy = int(x / cell_size - 1)
        ix = int(y / cell_size - 1)
        if ix == -1 or iy == -1:
            raise IndexError
        universe.add((ix, iy))
        canvas.itemconfig(rectangles[ix][iy], fill=live_color)
        print(universe)
    except IndexError:
        return


def clear_on_click(event):
    x, y = event.x, event.y
    x, y = x-x%cell_size, y-y%cell_size
    try:
        iy = int(x / cell_size - 1)
        ix = int(y / cell_size - 1)
        if ix == -1 or iy == -1:
            raise IndexError
        
        universe.discard((ix, iy))
        canvas.itemconfig(rectangles[ix][iy], fill=dead_color)
        print(universe)
    except IndexError:
        return


def repaint(tmp_live, tmp_dead):
    for (ix, iy) in tmp_dead | tmp_live:
        canvas.itemconfig(rectangles[ix][iy], fill=dead_color)
    for (ix, iy) in tmp_live:
        canvas.itemconfig(rectangles[ix][iy], fill=live_color)

def clear():
    global universe
    global rectangles
    
    
    for i in range(grid_size):
        for j in range(grid_size):
            canvas.itemconfig(rectangles[i][j], fill=dead_color)
    universe.clear()
    print(universe)

def change_mode():
    mp = mode_btn['text']
    if(mp=='clear'):
        mode_btn['text'] = 'fill'
    else:
        mode_btn['text'] = 'clear'

def begin():
    global universe
    change_rule()

    universe, tmp_dead = step(universe)
    repaint(universe, tmp_dead)
    # universe = tmp_survive | tmp_born
    global begin_id
    begin_id = root.after(200, begin)

def step_ev(event):
    change_rule()
    global universe
    universe, tmp_dead = step(universe)
    repaint(universe, tmp_dead)
   
def stop():
    root.after_cancel(begin_id)


def change_rule():
    global survive_rule
    global born_rule
    
    tmp = text.get()
    if(len(tmp) >0):
        tmp = tmp.split('/')
        survive_rule = [int(x) for x in list(tmp[0])]
        born_rule = [int(x) for x in list(tmp[1])]
        print(survive_rule)
        print(born_rule)
    else:
        survive_rule = [2,3]
        born_rule = [3]








root = Tk()
root.title("Game of Life")
frame = Frame(root, width=720, height=720)
frame.pack()
canvas = Canvas(frame, width=720, height=720)
canvas.pack()
universe = set()
create_grid()
#frame = Frame(root)
start = Button(root, text="Start", command=begin)
start.pack(side = LEFT)
stop = Button(root, text="Stop", command = stop)
stop.pack(side = LEFT)
clear = Button(root, text="Erase", command = clear)
clear.pack(side = LEFT)
text = Entry(root)
text.insert(0, "23/3")
text.pack(side=LEFT)
canvas.bind("<Button-1>", change_colour_on_click)
canvas.bind("<Button-3>", change_colour_on_click)
canvas.bind("<B1-Motion>", fill_on_click)
canvas.bind("<B3-Motion>", clear_on_click)
root.bind("<space>", step_ev)
#frame.pack()

 
root.mainloop()
