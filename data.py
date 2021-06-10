import mysql.connector
import datetime
from timecheck import which_hour
from mybot import sendMessage
mydb = mysql.connector.connect(
    host='localhost', user='root', passwd='password', database='girrafe')
if (mydb):
    print('conection successful')
else:
    print('conection unsuccessful')
mycursor = mydb.cursor(buffered=True)   

session , day=which_hour()
print("It is session {0} on a {1}".format(session,day))
def getext():
    
    mycursor.execute("SELECT {} FROM schedule WHERE sno={} ".format(day,session))

    for i in mycursor:
        text="You have {} class now".format(i[0])
        print(i)
        print(text)    
    return(text)    

       


#mycursor.execute("SELECT chat_id FROM notif WHERE section={}".format(n))
def sendReminder():
    mycursor.execute("SELECT chat_id from contact")
    ids=[]
    
    for i in mycursor:
        print("This is is i {}".format(i))
        ids.append(i)
        
        
        continue

    
        
    print(ids)    
    for i in ids:
        print(i[0])
        text=getext()
        sendMessage(int(i[0]),text)
        continue

 
