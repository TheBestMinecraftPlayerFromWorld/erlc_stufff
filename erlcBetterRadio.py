import tkinter as tk
import keyboard
import time

root = tk.Tk()

texts =     [
                ["Traffic stop", ["A","B"]],
                ["Shooting",     ["A1","B1","C1"]]
            ]
ct = -1
is_writing   = False
btns = []

def round_rectangle(x1, y1, x2, y2, radius=25,clr="gray", **kwargs): # Creating a rounded rectangle
        points = [x1+radius, y1,
                x1+radius, y1,
                x2-radius, y1,
                x2-radius, y1,
                x2, y1,
                x2, y1+radius,
                x2, y1+radius,
                x2, y2-radius,
                x2, y2-radius,
                x2, y2,
                x2-radius, y2,
                x2-radius, y2,
                x1+radius, y2,
                x1+radius, y2,
                x1, y2,
                x1, y2-radius,
                x1, y2-radius,
                x1, y1+radius,
                x1, y1+radius,
                x1, y1]

        return canvas.create_polygon(points, **kwargs, smooth=True, fill=clr)
def update():
    global ct
    for i,btn in enumerate(btns):
        text = [[t[0]] for t in texts]
        text.insert(0,[])
        if ct!=-1:
            try:
                text = texts[ct]
            except:
                ct = -1
                update()
                return
        try:
            if ct==-1:
                txt = text[i][0]
            else:
                txt = text[1][i-1]
        except Exception as e:
            txt = ""
        if i == 0:
            txt = text[0]
            if ct==-1:
                txt = "ERLC - QUICK RADIO"
        btn.configure(text=txt)
        if txt == "":
            btn.pack_forget()
        else:
            btn.pack()


root.title("Better Radio")
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
sx = sw//4
sy = sw//3
x = (sw//4)*3-sx//2
y = (sh)-sy
root.geometry(f"{sx}x{sy}+%d+%d" % (x, y-40))
root.configure(background='gray')
root.resizable(False, False)
root.lift()
root.attributes('-topmost', True)
root.update()
root.overrideredirect(1) 
canvas = tk.Canvas(root, bg="pink", highlightthickness=0,width=sx,height=sy)
canvas.place(x=0,y=0)
root.attributes("-transparentcolor", "pink")
rad = sx//4
round_rectangle(0, 0, sx, sy, radius=rad)

def writeInChat(message):
    global is_writing
    is_writing = True
    keyboard.press_and_release("t")
    time.sleep(0.05)
    keyboard.press_and_release("#")
    time.sleep(0.1)
    keyboard.press_and_release("backspace")
    keyboard.write(message,0.005)
    time.sleep(0.05)
    keyboard.press_and_release("enter")
    time.sleep(0.1)
    keyboard.press_and_release("t")
    time.sleep(0.1)
    keyboard.press_and_release("backspace")
    is_writing = False

def buttonCallback(n):
    global ct
    if ct==-1:
        ct = n-1
    else:
        if texts[ct][n]:
            time.sleep(1)
            writeInChat(texts[ct][n])
    update()
def goBack():
    global ct
    ct=-1
    update()
for a in range(10):
    txt = f"{a+1}: --------"
    cmd = lambda x=a:buttonCallback(x)
    bg = "blue"
    if a == 0:
        txt = "<--"
        cmd = goBack
        bg = "green"
    btn = tk.Button(root,text=txt,command=cmd,background=bg,foreground="white")
    btn.pack(
        expand=True
    )
    
    btns.append(btn)
close = tk.Button(root, text = "Close Better Quick Radio", command = lambda: root.destroy(),background="red",foreground="white")
close.pack()
def keyPressed(event):
    if event.event_type=="down":
        na = event.name

        if na == "^":
            goBack()
        else:
            try:
                na = int(na)
            except:
                pass
            else:
                buttonCallback(na)
keyboard.hook(keyPressed)
update()
root.mainloop()