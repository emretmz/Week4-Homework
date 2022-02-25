import tkinter as tk 
import random,time
window =tk.Tk()
  
def guess():
    start=time.time()
    global number_of_com
    number_of_com=random.randint(0, 9)	
    
    def update_text():
        last_guess_num=int(guess_num.get())
        if last_guess_num>number_of_com:
            guessing_lab.configure(text="Too high") #text=guess_num.get()
        elif last_guess_num<number_of_com:
            guessing_lab.configure(text="Too low")
        else:
            period=time.time()-start
            text="Congrats!Time:{}".format(period)
            guessing_lab.configure(text=text)

    guessing_lab=tk.Label(window,text="Guess number")
    guess_num=tk.StringVar(None)
    num_entry=tk.Entry(window,textvariable=guess_num,width=20)

    
    num_entry.pack()

    btn=tk.Button(window,text="Try",command=update_text)   
    btn.pack()
    guessing_lab.pack()

    return num_entry
guess()

 


window.mainloop()
"""Number Guessing Game General Information: I want to play a game which I can guess a number. The computer chooses a number in the range I chose. 
So that I can try to find the correct number which was selected by computer. Acceptance Criteria:
Computer must randomly pick an integer from user selected a range, i.e., from A to B, where A and B belong to Integer.
Your program should prompt the user for guesses if the user guesses incorrectly, it should print whether the guess is too high or too low.
If the user guesses correctly, the program should print total time and total number of guesses.
You must import some required modules or packages You can assume that the user will enter valid input.
"""
