import tkinter as tk
import random
from PIL import Image,ImageTk

choices = ['rock', 'paper', 'scissors']
user_score = 0
computer_score = 0

#GAME
def play(user_choice):
    global user_score, computer_score
    computer_choice = random.choice(choices)
    result = ""

    if user_choice == computer_choice:
        result = "tie!"
    elif user_choice == 'rock':
        if computer_choice == 'paper':
            result = "You lose :("
            computer_score += 1
        else:
            result = "You win :)"
            user_score += 1
    elif user_choice == 'paper':
        if computer_choice == 'scissors':
            result = "You lose :("
            computer_score += 1
        else:
            result = "You win :)"
            user_score += 1
    elif user_choice == 'scissors':
        if computer_choice == 'rock':
            result = "You lose :("
            computer_score += 1
        else:
            result = "You win :)"
            user_score += 1

    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")
    score_label.config(text=f"Your Score: {user_score} | Computer Score: {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    score_label.config(text="Your Score: 0 | Computer Score: 0")
    result_label.config(text="")
    rock_btn.config(state=tk.NORMAL)
    paper_btn.config(state=tk.NORMAL)
    scissors_btn.config(state=tk.NORMAL)

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x400")

bg_image=Image.open("D:\\task-1\\images.jpeg")
bg = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(root, image=bg)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


title = tk.Label(root, text="Rock Paper Scissors", bg='pink',font=("Helvetica", 24, "bold"))
title.pack(pady=10)

score_label = tk.Label(root, text="Your Score: 0 | Computer Score: 0",bg='yellow')
score_label.pack()

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack()

rock_btn = tk.Button(root, text="Rock",bg='lightgreen',height=1,width=10,command=lambda: play("rock"))
rock_btn.pack(side=tk.TOP)

paper_btn = tk.Button(root, text="Paper",bg='lightgreen',height=1,width=10,command=lambda: play("paper"))
paper_btn.pack(after=rock_btn,side=tk.TOP)

scissors_btn = tk.Button(root, text="Scissors",bg='lightgreen',height=1,width=10,command=lambda: play("scissors"))
scissors_btn.pack(side=tk.TOP)

reset_btn = tk.Button(root, text="Reset Game",fg='white',bg='purple',height=2,width=20, command=reset_game)
reset_btn.pack()

quit_btn=tk.Button(root,text="Quit",bg='orange',height=2,width=20,command=quit)
quit_btn.pack()

root.mainloop()
