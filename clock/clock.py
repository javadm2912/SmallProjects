from cProfile import label
from curses import window
from tkinter import *
from tkinter.ttk import *
from time import strftime
from turtle import window_height, window_width

main_clock = Tk()
main_clock.title("CLOCK")

main_clock.resizable(False,False)

def time():
    time_string = strftime(' %H:%M:%S ')
    clock_label.config(text=time_string)
    clock_label.after(1000, time)

clock_label = Label(main_clock,font = ('Purisa',75),background='black',foreground='#Cb3328')
clock_label.pack(anchor='center')

time()
mainloop()
