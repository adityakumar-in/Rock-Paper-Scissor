from tkinter import *
from sys import *
import random
from tkinter import messagebox

# Creating a Window
at = Tk()
at.title("Text-based Adventure Game")
at.geometry('1358x737')
at.resizable(0, 0)

# Setting Image path
photo = PhotoImage(file = r"images/my_rock.png")
photo1 = PhotoImage(file = r"images/my_paper.png")
photo2 = PhotoImage(file = r"images/my_scissor.png")
# photo3 = PhotoImage(file = r"c_rock.png")
# photo4 = PhotoImage(file = r"c_paper.png")
# photo5 = PhotoImage(file = r"c_scissor.png")

# Resizing image to fit on button 
irock = photo.subsample(13, 13) 
ipaper = photo1.subsample(13, 13) 
iscissor = photo2.subsample(13, 13) 
# icrock = photo3.subsample(13, 13) 
# icpaper = photo4.subsample(13, 13) 
# icscissor = photo5.subsample(13, 13) 

def rock():
    
    c_rock=0
    c_paper=0
    c_scissor=0
    
    # To generate random numbers
    choose = random.randint(1,3)
    if choose==1:
        c_rock=1
    elif choose==2:
        c_paper=1
    else:
        c_scissor=1
    
    # To check the user inputs with computer
    if c_rock==1 and c_paper==0 and c_scissor==0 :
        messagebox.showinfo('Status', 'Match Tied!')
    elif c_rock==0 and c_paper==1 and c_scissor==0 :
        messagebox.showinfo('Status', 'Oops, You lost the match!')
    else :
        messagebox.showinfo('Status', 'Congratulations, You won match!')
    
def paper():
    
    c_rock=0
    c_paper=0
    c_scissor=0
    
    # To generate random numbers
    choose = random.randint(1,3)
    if choose==1:
        c_rock=1
    elif choose==2:
        c_paper=1
    else:
        c_scissor=1
    
    # To check the user inputs with computer
    if c_rock==0 and c_paper==1 and c_scissor==0 :
        messagebox.showinfo('Status', 'Match Tied!')
    elif c_rock==0 and c_paper==0 and c_scissor==1 :
        messagebox.showinfo('Status', 'Oops, You lost the match!')
    else :
        messagebox.showinfo('Status', 'Congratulations, You won match!')
    
def scissor():
    
    c_rock=0
    c_paper=0
    c_scissor=0
    
    # To generate random numbers
    choose = random.randint(1,3)
    if choose==1:
        c_rock=1
    elif choose==2:
        c_paper=1
    else:
        c_scissor=1
    
    # To check the user inputs with computer
    if c_rock==0 and c_paper==0 and c_scissor==1 :
        messagebox.showinfo('Status', 'Match Tied!')
    elif c_rock==1 and c_paper==0 and c_scissor==0 :
        messagebox.showinfo('Status', 'Oops, You lost the match!')
    else :
        messagebox.showinfo('Status', 'Congratulations, You won match!')

def exits():
    at.destroy()
    sys.exit()

# Display Screen
Label(at, text="Rock Paper Scissor Game", font=("Arial Bold", 45, 'underline'), justify='center').pack(side=TOP, padx=100, pady=10)
Label(at, text="You are playing against computer so, Be Careful!", font=("Arial Bold", 25), justify='center').pack(side=TOP, padx=100, pady=30)
Button(at, text = 'Rock', image = irock, padx=35, pady=18, font=("Arial Bold", 25), compound=TOP, command=rock).pack(side=LEFT, padx=45) 
Button(at, text = 'Paper', image = ipaper, padx=35, pady=18, font=("Arial Bold", 25), compound=TOP, command=paper).pack(side=LEFT, padx=45) 
Button(at, text = 'Scissor', image = iscissor, padx=35, pady=18, font=("Arial Bold", 25), compound=TOP, command=scissor).pack(side=LEFT, padx=45) 
Button(at, text = 'Close', padx=10, font=("Arial", 15), command=exits).pack(side=BOTTOM, padx=20, pady=30) 

at.mainloop()