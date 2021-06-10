import datetime
from time import sleep
import mybot

def which_hour():
    timings=['09:00','09:50','10:50','11:40','13:20','14:10','15:00']
    now=datetime.datetime.now().strftime("%H:%M")
    day=datetime.datetime.now().strftime("%A")
    print("It is {}".format(int(now[0])))
    for i in range(0,7):
        for j in range(0,4):
            if j==0 and int(now[j])>int(timings[i][j] and j!=2) :  #if j is 0 then it is the first character, so break loop and go to next timing
                break                                     
            elif  j!=2 and  int(now[j])==int(timings[i][j]) :         #if both characters are same, then check the next character of the same timing
                continue
            elif j!=2 and int(now[j])>int(timings[i][j]):          #if character in 'now' is greater than the character in timing, go to the next timing  
                break
            elif  j==2:                                             #if character is ':'  
                continue
            elif j!=2 and int(now[j])<int(timings[i][j]):          #if character in timimgs > character in now, then return i 
                #print(i)
                return(i,day)
              
           
        
              
            
           
""" def keep():
    r=0
    while(r==0):
        which_hour()
        sleep(60)
            
            

keep()
         """

