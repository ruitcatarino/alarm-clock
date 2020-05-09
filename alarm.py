import argparse
import datetime
import easygui
import sys

def time_incorrect(time):
    if time[0]<0 or time[1]<0 or time[0]>24 or time[1]>60:
        return True
    return False

def args_variables(args):

    if args["time"]:
        time = args["time"].split(":")
        for i in range(0, len(time)):
            time[i] = int(time[i])

        if len(time) != 2 or time_incorrect(time):
            print("Insert a correct time!")
            sys.exit(0)
    else:
        hours = input('Hours:')
        minutes = input('Minutes:')

    if args["message"]:
        message = args["message"]
    else:
        message = 'Its time!'

    if time:
        return time,message

    return [hours,minutes],message

def messagebox(message):
    easygui.msgbox(message, title="Alarm")
    messagebox.showinfo("Alarm", message)

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-t", "--time", required = False, help = "Time to set the alarm (HH:MM)")
    ap.add_argument("-m", "--message", required = False, help = "Message that shows when the alarm goes off")
    args = vars(ap.parse_args())

    time,message=args_variables(args)
    messagebox(message)
    print(datetime.datetime.now().time())
