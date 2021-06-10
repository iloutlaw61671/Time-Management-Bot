from data import sendReminder
import datetime
from time import sleep

def updatethis():
    print("You're here")
    now1=datetime.datetime.now().strftime("%H:%M")
    notif=['08:50','09:40','10:40','11:30','13:10','14:00','14:50']
    for i in notif:
        if(i==now1):
            sendReminder()
def keep():
    r=0
    while(r==0):
        updatethis()
        sleep(60)   

keep()                             