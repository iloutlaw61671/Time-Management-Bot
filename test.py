#import mybot
import mysql.connector
mydb = mysql.connector.connect(
    host='localhost', user='root', passwd='password', database='girrafe')
if (mydb):
    print('conection successful')
else:
    print('conection unsuccessful')
mycursor = mydb.cursor(buffered=True)   

def get_chat(a):
    print("Original type of a is {}".format(type(a)))
    a=str(a)
    print(a)
    mycursor.execute("SELECT * FROM contact")
    count=0
    for i in mycursor:
        print(i)
        if i[0]==a:

            count+=1
  
        else:
            count+=count

    if count==0:
        print("adding")
        mycursor.execute("INSERT INTO contact (chat_id,section) VALUES (%s,%s)",(a,'n'))
        mydb.commit()

    print("Completed checking")
    return()
 
