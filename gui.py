import tkinter

a = 3

top = tkinter.Tk()

b = tkinter.__dict__
for (k,v) in b.items():
    print(k)
