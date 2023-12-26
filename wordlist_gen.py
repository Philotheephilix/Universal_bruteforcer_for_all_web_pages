import os
import csv
import time
intt=[]
string=[]
print(len(string))
def clr():
    os.system('cls')
clr()
wordlist_name=input("Enter name of the wordlist to create : ")
wordlist_dir='./Wordlists/'+wordlist_name+".txt"
clr()
fist=input("Enter the common guessed word : ")
string.append(fist)
op=input("Add Another (add atleast 10 strings to make the worlist powerfull) (Y/N)")
opp='y'
while((op in ['Y','y']) and (opp in ["Y","y"])):
    fist=input("Enter guessed word ")
    string.append(fist)
    opp=input("Add Another (add atleast 10 strings to make the worlist powerfull) (Y/N)")
clr()
years=int(input("Enter a year range used in password (Usually the year os establishment of the Organization) \nEnter starting year : "))
yeare=int(input('Enter Current year :'))

for i in range(years,yeare):
    i=str(i)
    intt.append(i)
symbols=['','@','#','$','&','*','!','?']

intt.append("123")
intt.append("456")
intt.append("321")

clr()
print("initialized all values")
time.sleep(0.3)
for i in range(3):
    print(". . . . . . . . . . . . .")
    time.sleep(.4)
clr()
count=0
with open(wordlist_dir, 'w', newline="") as csvfile:
    writer = csv.writer(csvfile,delimiter=" ")
    for strr in range(len(string)):
        strr=string[strr]
        for symbol in symbols:
            for symbol1 in symbols:
                for i in range(len(intt)):
                    i=intt[i]
                    trypass=strr+symbol+symbol1+i
                    count+=1
                    writer.writerow([trypass])
count=str(count)
print("worlist generated sucessfully\n Stored in \""+wordlist_dir+"\"")
print("worlist contains "+count+" attempts")
