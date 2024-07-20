import tkinter as tk
from tkinter import messagebox
import random

# Game logic to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Tie"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        return "User"
    else:
        return "Computer"

# Update the result and scores
def play(user_choice):
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    winner = determine_winner(user_choice, computer_choice)
    
    result_label.config(text=f"User: {user_choice}\nComputer: {computer_choice}\nResult: {winner}")
    
    if winner == "User":
        scores["User"] += 1
    elif winner == "Computer":
        scores["Computer"] += 1
        
    score_label.config(text=f"Scores\nUser: {scores['User']} | Computer: {scores['Computer']}")
    
    if messagebox.askyesno("Play Again?", "Do you want to play another round?"):
        return
    else:
        root.destroy()

# Create the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

# Initialize scores
scores = {"User": 0, "Computer": 0}

# Create labels and buttons
instructions = tk.Label(root, text="Choose Rock, Paper, or Scissors", font=("Arial", 14))
instructions.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

rock_button = tk.Button(button_frame, text="Rock", width=10, command=lambda: play("Rock"))
rock_button.grid(row=0, column=0, padx=5)

paper_button = tk.Button(button_frame, text="Paper", width=10, command=lambda: play("Paper"))
paper_button.grid(row=0, column=1, padx=5)

scissors_button = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("Scissors"))
scissors_button.grid(row=0, column=2, padx=5)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

score_label = tk.Label(root, text="Scores\nUser: 0 | Computer: 0", font=("Arial", 12))
score_label.pack(pady=10)

# Run the application
root.mainloop()
