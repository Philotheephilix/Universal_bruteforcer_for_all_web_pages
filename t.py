import linecache
import pyautogui as py
wordlist="wordlist.txt"

with open(wordlist, 'r', newline="") as csvfile:
    for count, line in enumerate(csvfile):
        pass
        count+=1
    for i in range(count):
        cur_user=linecache.getline(wordlist,i+1)
        for j in range(count):

            cur_pass=linecache.getline(wordlist,j+1)
            print("user",cur_user,"\npass",cur_pass)