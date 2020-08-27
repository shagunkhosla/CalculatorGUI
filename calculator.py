from tkinter import *


def hello(event):
    global screenvalue
    text=event.widget.cget("text")

    if text=="=":
        if screenvalue.get().isdigit():
            value=int(screenvalue.get())
        else:
            try:
                value=eval(screenvalue.get())
            except Exception as e:
                print(e)
                value="Error"
                
        screenvalue.set(value)
        screen.update()

    elif text=="C":
        screenvalue.set("")
        screen.update()

    else:
        screenvalue.set((screenvalue.get())+(text))
        screen.update()

root=Tk()
root.geometry("644x700")
root.maxsize(644,700)
root.minsize(644,700)
root.title("Calculator By Shagun")
root.wm_iconbitmap("calciii.ico")

screenvalue=StringVar()
screenvalue.set("")
screen=Entry(root, textvariable=screenvalue, font="lucida 40 bold")
screen.pack(fill=X, pady=10, padx=10, ipadx=25)

frames=[]
for i in range(0,4):
    f=Frame(root, bg="grey")
    f.pack(fill=X, expand=TRUE)
    frames.append(f)

options=['9','8','7','+','6','5','4','-','3','2','1','*','C','0','/','=']
j=0
for i in range(0,4):
    b1=Button(frames[i],text=options[j], font="lucida 40 bold", padx=5, pady=5)
    b1.pack(side=LEFT, padx=20, pady=20)
    b1.bind('<Button>', hello)
    j+=1
    b2=Button(frames[i],text=options[j], font="lucida 40 bold", padx=5, pady=5)
    b2.pack(side=LEFT, padx=20, pady=20)
    b2.bind('<Button>', hello)
    j += 1
    b3=Button(frames[i],text=options[j], font="lucida 40 bold", padx=5, pady=5)
    b3.pack(padx=20, pady=20, side=LEFT)
    b3.bind('<Button>', hello)
    j+=1
    b4 = Button(frames[i], text=options[j], font="lucida 40 bold", padx=15, pady=5)
    b4.pack(padx=20, pady=20)
    b4.bind('<Button>', hello)
    j += 1

root.mainloop()