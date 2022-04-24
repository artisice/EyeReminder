import time
from tkinter import *
from threading import Thread
import gc
import sys, os
from tkinter import messagebox
from tkvideo import tkvideo
from playsound import playsound

path = os.path.join(os.path.dirname(sys.executable), 'fhd1.mp4')


def closing():
    if messagebox.askokcancel('Выход', 'Вы уверены, что хотите выйти из приложения?'):
        raise SystemExit


tk = Tk()

tk.protocol("WM_DELETE_WINDOW", closing)

tk['bg'] = '#1d1d1d'
tk.title('Eye reminder')
tk.geometry('750x400')
x = (tk.winfo_screenwidth() - tk.winfo_reqwidth()) / 3
y = (tk.winfo_screenheight() - tk.winfo_reqheight()) / 3
tk.wm_geometry("+%d+%d" % (x, y))

tk.resizable(width=False, height=False)

canvas = Canvas(tk, height=250, width=300)
filename = PhotoImage(file="darkbg.png")
background_label = Label(tk, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
canvas.pack()

state = False

dark = PhotoImage(file="darkbg.png")
light = PhotoImage(file="lightbg.png")


def switch():
    global state
    if state:
        btn.config(image=off, bg="#111111", activebackground="#111111")
        background_label.config(image=dark)
        state = False
    else:
        btn.config(image=on, bg="#bed7ff", activebackground="#bed7ff")
        background_label.config(image=light)
        state = True


on = PhotoImage(file=r"light.png")
off = PhotoImage(file=r"dark.png")

btn = Button(tk, borderwidth=0, command=switch, bg="#111111", activebackground="#111111")
btn.place(relx=0.84, rely=0.4, anchor="center")
btn.config(image=off)

v = StringVar()
e = Entry(tk, textvariable=v, bg='#0099ff', bd=0, font=20, fg='#004776', selectbackground='#004776', width=18)
e.pack()
e.place(relx=0.35, rely=0.32)


def snd():
    playsound('fhd2.mp3')


def play():
    Thread(target=snd, daemon=True).start()


def vid():
    anim = Toplevel(tk)
    anim['bg'] = '#1d1d1d'
    anim.wm_attributes("-topmost", 1)
    anim.overrideredirect(True)
    my_label = Label(anim)
    my_label.pack()
    player = tkvideo('fhd1.mp4', my_label, loop=0, size=(1280, 720), hz=5)
    player.play()

    a = (anim.winfo_screenwidth() - anim.winfo_reqwidth()) / 4
    b = (anim.winfo_screenheight() - anim.winfo_reqheight()) / 4
    anim.wm_geometry("+%d+%d" % (a, b))

    anim.after(600, play)

    anim.after(45000, lambda: anim.destroy())


def btn1():
    ttk = Toplevel(tk)
    ttk.title('Eye remind')
    ttk.overrideredirect(True)

    img1 = PhotoImage(file="upr.png")
    label = Label(ttk, image=img1, height=715, width=955)
    label.image_ref = img1
    label.pack()

    a = (ttk.winfo_screenwidth() - ttk.winfo_reqwidth()) / 4
    b = (ttk.winfo_screenheight() - ttk.winfo_reqheight()) / 4
    ttk.wm_geometry("+%d+%d" % (a, b))
    ttk.wm_attributes("-topmost", 1)

    ttk.after(20000, lambda: ttk.destroy())

    tk.after(20200, vid)


def restart():
    os.execv(sys.executable, ['python'] + sys.argv)


class Timer(Thread):
    def run(self):
        while True:
            gc.collect()
            d = int(e.get())

            if d == 0:
                e.delete(0, END)
                e.insert(0, "Ошибка")
                break

            tk.after(d * 60 * 1000, btn1)
            time.sleep(d * 60)


def bttn1():
    Timer().start()


def cancel_butn():
    b = int(e.get())

    rbotn['state'] = 'disabled'

    if b == 0:
        rbotn['state'] = 'normal'


def functions():
    bttn1()
    cancel_butn()


botn1 = PhotoImage(file="img1.png")
rbotn1 = Button(tk, image=botn1, activebackground="#0099ff", command=restart)
rbotn1["bg"] = "#0099ff"
rbotn1["border"] = "0"
rbotn1.pack()
rbotn1.place(x=395, y=220)

botn = PhotoImage(file="img0.png")
rbotn = Button(tk, image=botn, activebackground="#0099ff", command=functions)
rbotn["bg"] = "#0099ff"
rbotn["border"] = "0"
rbotn.pack()
rbotn.place(x=273, y=220)

tk.iconbitmap('iconeye.ico')

tk.mainloop()
