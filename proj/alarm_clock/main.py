from tkinter import *
import time 


app = Tk()

app.geometry('400x300')
app.title("Study Clock")

main_title = Label("Study Time Tracker")

hour = Entry(app, text='', width=2)
hour.grid(column = 0, row = 1)
minute = Entry(app, text='')
minute.place(x=150, y=70, width=60, height=30)


app.mainloop()