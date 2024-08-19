import tkinter as tk
import random
import math


us = 0
cs = 0

#  game logic function
def play_game(player_choice):
    global us, cs
    ccl = ['gun', 'water', 'snake']
    cc = math.floor((random.random() * 3))
    computer_choice = ccl[cc]

    result_text = ""
    if computer_choice == ccl[player_choice - 1]:
        result_text = "It's a Draw!"
    elif (player_choice == 1 and computer_choice == 'gun') or \
         (player_choice == 2 and computer_choice == 'snake') or \
         (player_choice == 3 and computer_choice == 'water'):
        result_text = "Computer scores!"
        cs += 1
    else:
        result_text = "You score!"
        us += 1

    
    result_label.config(text=result_text)
    player_score_label.config(text=f"Your Score: {us}")
    computer_score_label.config(text=f"Computer Score: {cs}")


def close_game():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Snake Water Gun Game")
root.geometry("400x400")
root.configure(bg="#A4C3B2")


button_color = "#386641"
button_text_color = "#FFFFFF"
result_bg_color = "#6A994E"
score_bg_color = "#4F772D"
exit_button_color = "#BC6C25"


welcome_label = tk.Label(root, text="Welcome to Snake Water Gun!", font=("Arial", 16), bg="#A4C3B2")
welcome_label.pack(pady=10)

instructions_label = tk.Label(root, text="1: Snake | 2: Water | 3: Gun | 4: Exit", font=("Arial", 12), bg="#A4C3B2")
instructions_label.pack(pady=5)


snake_button = tk.Button(root, text="Snake", width=10, bg=button_color, fg=button_text_color, font=("Arial", 12),
                         command=lambda: play_game(1))
snake_button.pack(pady=5)

water_button = tk.Button(root, text="Water", width=10, bg=button_color, fg=button_text_color, font=("Arial", 12),
                         command=lambda: play_game(2))
water_button.pack(pady=5)

gun_button = tk.Button(root, text="Gun", width=10, bg=button_color, fg=button_text_color, font=("Arial", 12),
                       command=lambda: play_game(3))
gun_button.pack(pady=5)


result_label = tk.Label(root, text="", font=("Arial", 14), bg=result_bg_color, fg=button_text_color)
result_label.pack(pady=10, fill=tk.X)


player_score_label = tk.Label(root, text="Your Score: 0", font=("Arial", 12), bg=score_bg_color, fg=button_text_color)
player_score_label.pack(side=tk.LEFT, padx=20, pady=10, fill=tk.X)

computer_score_label = tk.Label(root, text="Computer Score: 0", font=("Arial", 12), bg=score_bg_color, fg=button_text_color)
computer_score_label.pack(side=tk.RIGHT, padx=20, pady=10, fill=tk.X)


exit_button = tk.Button(root, text="Exit", width=10, bg=exit_button_color, fg=button_text_color, font=("Arial", 12),
                        command=close_game)
exit_button.pack(pady=20)


root.mainloop()

