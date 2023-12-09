from tkinter import *
import random
import tkinter.messagebox as tmsg


root = Tk()

# logic starts here


def display(password):
    show = Label(text=f'Generated Password : {password} .', font='bold')
    show.pack()


def greetings():
    greet = Label(text='Thank You ....', foreground='red')
    greet.pack()


def prints():
    counter = 0
    while (counter <= 2):
        counter = counter+1
        if chr_entry.get() < 5:
            tmsg.showwarning('Value Warning !!', 'You have not entered any value for generation ? Please try again\n Try to enter numbers above 5')
            break
        else:

            password_num = chr_entry.get()
            string = "abcdefghijklmnopqrstuvwxyz012456789"
            special_char = "!@#?"
            password = ""
            for i in range(1, password_num+1):
                password = password + random.choice(string)

            for i in range(len(password)):
                if password[i] in special_char:
                    break
                else:
                    continue
            else:
                num = random.randint(2, len(password)-1)
                if num == 1 or num == len(password):
                    pass
                else:
                    num_place_letter = password[num-1]
                    rand_char = random.choice(special_char)
                    password = password.replace(num_place_letter, rand_char)

            change = len(password)//2

            for i in range(change):
                num1 = random.randint(1, len(password))
                num2 = password[num1-1]
                password = password.replace(num2, num2.upper())

            display(password)
            if counter == 3:
                greetings()
                inp_button.configure(state=DISABLED)
                break

    
    # inp_button.configure(state=DISABLED)    to disable the button


#  GUI starts here
root.geometry('600x400')
head = Label(text='Hey , Welcome Password Generator !!!',
             background='black', foreground='white', font='bold')
head.pack()

fline = Label(text='How many characters of password you need ? ',
              foreground='red')
fline.pack(pady=50)

chr_entry = IntVar()
char_entry = Entry(root, textvariable=chr_entry)
char_entry.pack()
inp_button = Button(root, text='Generate Password', command=prints,
                    foreground='white', relief=SUNKEN, background='black')
inp_button.pack(pady=10)

root.mainloop()
