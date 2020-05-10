import tkinter as tk
from tkinter import ttk
import threading
import argparse
import datetime
import time
import sys
import os

def snooze(window,t,alarm_time,message):
    t.do_run=False
    t.join()
    window.destroy()
    alarm_clock(alarm_time,message)


def time_incorrect(time):
    if time[0]<0 or time[1]<0 or time[0]>24 or time[1]>60:
        return True
    return False

def args_time():
    if args["time"]:
        time_variable = args["time"].split(":")
        for i in range(0, len(time_variable)):
            time_variable[i] = int(time_variable[i])

        if len(time_variable) != 2 or time_incorrect(time_variable):
            print("Insert a correct time!")
            sys.exit(0)

        return time_variable
    else:
        hours = input('Hours:')
        minutes = input('Minutes:')

        return [int(hours),int(minutes)]

def args_message():
    if not args["message"]:
        return 'Its time!'
    else:
        return args["message"]

def play_alarm(arg):
    t = threading.currentThread()
    while getattr(t, "do_run", True):
        os.system('play -nq -t alsa synth {} sine {}'.format(0.5, 440))
        time.sleep(0.5)


def messagebox(alarm_time,message):
    alarm_time[1]+=10

    t = threading.Thread(target=play_alarm, args=("task",))
    t.start()

    window = tk.Tk()
    window.wm_title("Alarm")
    windowWidth = window.winfo_reqwidth()
    windowHeight = window.winfo_reqheight()

    positionRight = int(window.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(window.winfo_screenheight()/3 - windowHeight/2)

    window.geometry("+{}+{}".format(positionRight, positionDown))
    label = ttk.Label(window, text=message, font=("Helvetica", 20))
    label.pack(pady=10)
    but_snooze = ttk.Button(window, text="Snooze", command = lambda:snooze(window,t,alarm_time,message))
    but_stop = ttk.Button(window, text="Stop", command = window.destroy)
    but_snooze.pack()
    but_stop.pack()

    window.mainloop()

    t.do_run=False
    t.join()

def alarm_clock(alarm_time,message):
    now_date = str(datetime.datetime.now().time())

    now = now_date.split(":")

    del now[-1]

    for i in range(0, 2):
        now[i] = int(now[i])

    while alarm_time!=now:
        now_date = str(datetime.datetime.now().time())

        now = now_date.split(":")

        print(alarm_time,now)
        for i in range(0, 2):
            now[i] = int(now[i])

        del now[-1]

    messagebox(alarm_time,message)

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-t", "--time", required = False, help = "Time to set the alarm (HH:MM)")
    ap.add_argument("-m", "--message", required = False, help = "Message that shows when the alarm goes off")
    args = vars(ap.parse_args())

    timev=args_time()
    message=args_message()

    alarm_clock(timev,message)
