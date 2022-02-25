from tkinter import *
import random
import string
from sklearn.utils import shuffle

"""Create a window"""
window=Tk()
window.title("My Password Generator")
window.configure(width=500, height=300)
window.configure(bg='lightgray')
window.geometry("500x200")

"""Generate a password"""
def pass_generate():
    temp=[]
    lower=string.ascii_lowercase
    upper=string.ascii_uppercase
    num=string.digits
    symbol=string.punctuation

    temp.append("".join(random.sample(lower,2)))
    temp.append("".join(random.sample(upper,2)))
    temp.append("".join(random.sample(num,2)))
    temp.append("".join(random.sample(symbol,2)))
    all=lower+upper+num+symbol
    temp.append("".join(random.sample(all,4)))
    my_pass=shuffle(temp)
    my_pass="".join(my_pass)
    return my_pass

""" Tkinter """
my_text = "Generate a new password!"
def pass_config():
    global my_text
    my_pass=pass_generate()
    my_label.config(text = my_pass)

my_button = Button(window,
                   text = "Update",
                   command = pass_config)
my_label = Label(window,
                 text = "password")                   
my_label.pack()
my_button.pack()
window.mainloop()