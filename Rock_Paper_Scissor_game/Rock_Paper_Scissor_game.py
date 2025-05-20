import random
import tkinter as tk
from tkinter import messagebox

user_score = 0
computer_score = 0

def determine_winner(user_choice):
    global user_score, computer_score
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        result = "You win!"
        user_score += 1
    else:
        result = "Computer wins!"
        computer_score += 1

    messagebox.showinfo("Result", f"Computer chose {computer_choice}\n{result}")
    update_score()

def update_score():
    score_label.config(text=f"You: {user_score} | Computer: {computer_score}")

root = tk.Tk()
root.title("Rock, Paper, Scissors Game")
root.geometry("300x300")

tk.Label(root, text="Choose Rock, Paper, or Scissors", font=("Arial", 12)).pack(pady=10)

btn_rock = tk.Button(root, text="Rock", width=10, command=lambda: determine_winner("Rock"))
btn_rock.pack(pady=5)

btn_paper = tk.Button(root, text="Paper", width=10, command=lambda: determine_winner("Paper"))
btn_paper.pack(pady=5)

btn_scissors = tk.Button(root, text="Scissors", width=10, command=lambda: determine_winner("Scissors"))
btn_scissors.pack(pady=5)

score_label = tk.Label(root, text="You: 0 | Computer: 0", font=("Arial", 12))
score_label.pack(pady=10)

root.mainloop()
