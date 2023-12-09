import random

print("Hey !!! Want to generate password . How many letters of password do u want ?")
password_num=int(input())
string="abcdefghijklmnopqrstuvwxyz012456789"
special_char="!@#?"
password=""

# generation of password of given input

for i in range(1,password_num+1):
    password=password + random.choice(string)

# checking for special char in password
    
for i in range(len(password)):
    if password[i] in special_char :
        break
    else :
        continue 

# following block is for adding special char in password

else :
        num=random.randint(2,len(password)-1)        #2 becoz 2-1=1 means 1st index position and last - 1= second last means it will from 2 to second last ...to get rid of 1st and last position
        if num==1 or num==len(password):
            pass
        else:
            num_place_letter=password[num-1]
            rand_char=random.choice(special_char)
            password=password.replace(num_place_letter,rand_char)

# changing into upper cases...basically we are changing half letters to upper
change=len(password)//2
print("actual number of changes :",change)
for i in range(change):
    num1=random.randint(1,len(password))
    num2=password[num1-1]
    password=password.replace(num2,num2.upper())

print("Your generated password is --> ",password)    
