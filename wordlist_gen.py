import csv
int=[]
string=['Test','licet','Licet','LICETADMIN','licetadmin','LICET','Loyola','LICAM','Icam','test','server','admin','hp','aruba','I11','i11','admin','LOHO2','loho','loho2']
print(len(string))
for i in range(2009,2024):
    i=str(i)
    int.append(i)
symbols=['','@','#','$','&','*','!','?']
int.append("123")
int.append("456")
int.append("321")
with open('wordlist.txt', 'w', newline="") as csvfile:
    writer = csv.writer(csvfile,delimiter=" ")
    for str in range(len(string)):

        str=string[str]
        for symbol in symbols:
            for symbol1 in symbols:
                for i in range(len(int)):
                    i=int[i]
                    trypass=str+symbol+symbol1+i
                    
                    writer.writerow([trypass])
print(trypass)
