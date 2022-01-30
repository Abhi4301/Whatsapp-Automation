import tkinter as tk
import pywhatkit
import pyautogui
from tkinter import filedialog
import pyautogui as pg
import webbrowser as web
import time
import pandas as pd


def send(num, msg, hour, minute):
    pywhatkit.sendwhatmsg(f"+91{num}", msg, hour, minute, 36)
    print("hello")
    pyautogui.click()
    pyautogui.press("enter")


def uploadfile():
    file = filedialog.askopenfilename(filetypes=[("CSV Files", '.csv'),
                                                 ("Text Docs", '*.txt'),
                                                 ("All Types", '*.*')])
    f1 = open(file, "r")
    b = f1.read()
    f1.close()

    f2 = open("leads.csv", "w")
    f2.write(b)
    f2.close()


def exl():
    data = pd.read_csv("leads.csv")
    data_dict = data.to_dict('list')
    leads = data_dict['LeadNumber']
    messages = data_dict['Message']
    combo = zip(leads, messages)
    first = True
    for lead, message in combo:
        time.sleep(14)
        web.open("https://web.whatsapp.com/send?phone=" + lead + "&text=" + message)
        time.sleep(10)
        width, height = pg.size()
        pg.click(width / 2, height / 2)
        time.sleep(9)
        pg.press('enter')


class automation(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.iconbitmap(self, default="LOGO.ico")
        tk.Tk.wm_title(self, "Whatsapp Automation")

        self.geometry("842x510")
        self.configure(bg="#ffffff")
        self.resizable(False, False)

        self.container = container = tk.Frame(self, background="#ffffff")
        container.grid(row=0, column=0, sticky='nesw')
        container.configure(background="#ffffff")
        container.pack(side="top", fill="both")

        self.frames = {}

        for F in (MainWindow, SecondWindow, ThirdWindow):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            frame.grid(row=0, column=0, sticky="nsew")
            self.frames[page_name] = frame

        self.show_frame('MainWindow')

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class MainWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller1 = controller
        # SET BACKGROUND AND SET IMAGE IN BACKGROUND
        self.frame1 = tk.Frame(self, background="#ffffff")
        self.canvas1 = tk.Canvas(self, bg="#ffffff", height=510, width=842, bd=0, highlightthickness=0,
                                 relief="ridge")
        self.canvas1.place(x=0, y=0)
        self.canvas1.pack(side='left')
        self.background_img1 = tk.PhotoImage(file="background.png")
        self.canvas1.create_image(0, 0, image=self.background_img1, anchor="nw")

        self.img1 = tk.PhotoImage(file="img1.png")
        self.b1 = tk.Button(self, image=self.img1, borderwidth=0, highlightthickness=0,
                            command=lambda: controller.show_frame('SecondWindow'),
                            relief="flat")

        self.b1.pack()
        self.b1.place(x=445, y=150, width=348, height=62)
        # creating third button

        self.img3 = tk.PhotoImage(file="img3.png")
        self.b3 = tk.Button(self, image=self.img3, borderwidth=0, highlightthickness=0,
                            command=lambda: controller.show_frame('ThirdWindow'), relief="flat")
        self.b3.pack()
        self.b3.place(x=445, y=300, width=348, height=62)

        self.canvas1.pack()


# SECOND WINDOW
class SecondWindow(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        a = tk.StringVar()
        b = tk.StringVar()
        c = tk.IntVar()
        d = tk.IntVar()
        self.controller = controller
        # SET BACKGROUND AND SET IMAGE IN BACKGROUND
        self.frame2 = tk.Frame(self, background="#ffffff")
        self.canvas2 = tk.Canvas(self, bg="#ffffff", height=510, width=842, bd=0, highlightthickness=0,
                                 relief="ridge")
        self.canvas2.place(x=0, y=0)

        # set image in background
        self.background_img2 = tk.PhotoImage(file="background2.png")
        self.canvas2.create_image(0, 0, image=self.background_img2, anchor="nw")

        # enter a number
        self.entry1_img = tk.PhotoImage(file="textBox1.png")
        self.canvas2.create_image(570, 112, image=self.entry1_img)

        self.entry1 = tk.Entry(self, bd=0, bg="#c4c4c4", highlightthickness=0, textvariable=a)
        self.entry1.pack()
        self.entry1.place(x=423, y=90, width=280, height=45)

        # enter a massage

        self.entry2_img = tk.PhotoImage(file="textBox2.png")
        self.canvas2.create_image(570, 225, image=self.entry2_img)

        self.entry2 = tk.Entry(self, bd=0, bg="#c4c4c4", highlightthickness=0, textvariable=b)
        self.entry2.pack()
        self.entry2.place(x=423, y=203, width=280, height=45)

        # enter a time -> Hour
        self.entry3_img = tk.PhotoImage(file="textBox3.png")
        self.canvas2.create_image(470, 329, image=self.entry3_img)

        self.entry3 = tk.Entry(self, bd=0, bg="#c4c4c4", highlightthickness=0, textvariable=c)
        self.entry3.pack()
        self.entry3.place(x=423, y=312, width=80.0, height=35)

        # minute
        self.entry4_img = tk.PhotoImage(file="textBox4.png")
        self.canvas2.create_image(676, 329, image=self.entry4_img)

        self.entry4 = tk.Entry(self, bd=0, bg="#c4c4c4", highlightthickness=0, textvariable=d)
        self.entry4.pack()
        self.entry4.place(x=630, y=312, width=80.0, height=35)

        # Go home
        self.img4 = tk.PhotoImage(file="img4.png")
        self.b4 = tk.Button(self, image=self.img4, borderwidth=0, highlightthickness=0,
                            command=lambda: controller.show_frame('MainWindow'), relief="flat")
        self.b4.pack()
        self.b4.place(x=418, y=400, width=100, height=37)

        # Send message
        self.img5 = tk.PhotoImage(file="img5.png")
        self.b5 = tk.Button(self, image=self.img5, borderwidth=0, highlightthickness=0,
                            command=lambda: send(a.get(), b.get(), c.get(), d.get()), relief="flat")
        self.b5.pack()
        self.b5.place(x=642, y=400, width=100, height=37)
        self.canvas2.pack(side='left')


# THIRD WINDOW CODE
class ThirdWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller3 = controller
        # SET BACKGROUND AND SET IMAGE IN BACKGROUND
        self.frame3 = tk.Frame(self, background="#ffffff")
        self.canvas3 = tk.Canvas(self, bg="#ffffff", height=510, width=842, bd=0, highlightthickness=0,
                                 relief="ridge")

        self.canvas3.place(x=0, y=0)

        self.background_img3 = tk.PhotoImage(file="background4.png")
        self.canvas3.create_image(0, 0, image=self.background_img3, anchor="nw")
        # BUTTON FOR UPLOAD FILES
        self.img8 = tk.PhotoImage(file="img8.png")
        self.b8 = tk.Button(self, image=self.img8, borderwidth=0, highlightthickness=0, command=lambda: uploadfile(),
                            relief="flat")
        self.b8.pack()
        self.b8.place(x=430, y=180, width=350, height=61)
        # BUTTON FOR GOTO MAIL WINDOW
        self.img9 = tk.PhotoImage(file="img9.png")
        self.b9 = tk.Button(self, image=self.img9, borderwidth=0, highlightthickness=0,
                            command=lambda: controller.show_frame('MainWindow'), relief="flat")
        self.b9.pack()
        self.b9.place(x=430, y=385, width=119, height=47)
        # BUTTON FOR SEND MESSAGES
        self.img10 = tk.PhotoImage(file="img10.png")
        self.b10 = tk.Button(self, image=self.img10, borderwidth=0, highlightthickness=0, command=lambda: exl(),
                             relief="flat")
        self.b10.pack()
        self.b10.place(x=655, y=385, width=119, height=47)
        self.canvas3.pack(side='left')


if __name__ == '__main__':
    app = automation()
    app.mainloop()
