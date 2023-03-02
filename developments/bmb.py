import requests
from random import choice
from tkinter import *

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
}


window = Tk()
window.title('bomber')
window.resizable(width=False, height=False)


x = (window.winfo_screenwidth() - window.winfo_reqwidth()) / 2
y = (window.winfo_screenheight() - window.winfo_reqheight()) / 2
window.wm_geometry("+%d+%d" % (x - 50, y))

window.rowconfigure([0, 1, 2], minsize=100)
window.columnconfigure([0, 1, 2], minsize=100)

frame = Frame(window, borderwidth=2, relief=GROOVE)
frame.pack()

frm_btn = Frame(window)
frm_btn.pack()


ent_num = Entry(frame, bg='white')
ent_num.grid(row=0, column=1, padx=5)

ent_pass = Entry(frame, bg='white')
ent_pass.grid(row=1, column=1)

lbl_num = Label(frame, text='number:')
lbl_num.grid(row=0, column=0, padx=5)

lbl_pass = Label(frame, text='pass:')
lbl_pass.grid(row=1, column=0, padx=5, sticky='e')

level_rage = IntVar()

r1 = Radiobutton(frm_btn, text='long', variable=level_rage, value=1)
r1.grid(row=2, column=0)

r2 = Radiobutton(frm_btn, text='rage', variable=level_rage, value=2)
r2.grid(row=2, column=1)

btn_go = Button(frm_btn, text='boom')
btn_go.grid(row=2,column=2, pady=4, sticky='e')


window.mainloop()

#забомбить сашку +79188516454