import tkinter as tk
from tkinter import messagebox
import random

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("900x700")
root.config(bg="#0f172a")
root.resizable(False, False)

user_score = computer_score = draws = streak = round_no = best_streak = 0

choices = ["Rock", "Paper", "Scissors"]
emojis = {"Rock": "✊", "Paper": "✋", "Scissors": "✌"}
colors = {"Rock": "#64748b", "Paper": "#2563eb", "Scissors": "#9333ea"}

def update_score():
    score_user.config(text=str(user_score))
    score_computer.config(text=str(computer_score))
    score_draw.config(text=str(draws))
    streak_label.config(text=f"🔥 Winning Streak: {streak}")

def reset_game():
    global user_score, computer_score, draws, streak, round_no, best_streak
    user_score = computer_score = draws = streak = round_no = best_streak = 0
    user_display.config(text="❔\nYou")
    computer_display.config(text="❔\nComputer")
    result_label.config(text="MAKE YOUR MOVE!", fg="#60a5fa")
    round_label.config(text="ROUND 0")
    update_score()

def play_game(user):
    global user_score, computer_score, draws, streak, round_no, best_streak

    computer = random.choice(choices)
    round_no += 1

    user_display.config(text=f"{emojis[user]}\n{user}")
    computer_display.config(text=f"{emojis[computer]}\n{computer}")

    if user == computer:
        result, color = "IT'S A DRAW!", "#facc15"
        draws += 1
        streak = 0
    elif (user, computer) in [("Rock", "Scissors"), ("Paper", "Rock"), ("Scissors", "Paper")]:
        result, color = "YOU WIN! 🎉", "#22c55e"
        user_score += 1
        streak += 1
        best_streak = max(best_streak, streak)
    else:
        result, color = "COMPUTER WINS!", "#ef4444"
        computer_score += 1
        streak = 0

    result_label.config(text=result, fg=color)
    round_label.config(text=f"ROUND {round_no}")
    update_score()

    if user_score == 3 or computer_score == 3:
        winner = "🏆 YOU WON THE MATCH!" if user_score == 3 else "💻 COMPUTER WON!"
        root.after(500, lambda: finish_match(winner))

def finish_match(winner):
    messagebox.showinfo("Match Finished", f"{winner}\n\nYour Score: {user_score}\nComputer Score: {computer_score}\nBest Streak: {best_streak}")
    reset_game()

def create_label(parent, text, size, color, bg="#0f172a"):
    return tk.Label(parent, text=text, font=("Arial", size, "bold"), fg=color, bg=bg)

create_label(root, "⚔ ROCK PAPER SCISSORS ⚔", 25, "#38bdf8").pack(pady=(20, 5))
create_label(root, "CHALLENGE THE COMPUTER!", 11, "#94a3b8").pack()

score_frame = tk.Frame(root, bg="#1e293b")
score_frame.pack(fill="x", padx=40, pady=20)

def score_box(title, color):
    box = tk.Frame(score_frame, bg="#1e293b")
    box.pack(side="left", expand=True, pady=15)
    create_label(box, title, 13, color, "#1e293b").pack()
    score = create_label(box, "0", 32, "white", "#1e293b")
    score.pack()
    return score

score_user = score_box("👤 YOU", "#38bdf8")
score_draw = score_box("DRAW", "#facc15")
score_computer = score_box("💻 COMPUTER", "#f87171")

round_label = create_label(root, "ROUND 0", 12, "#94a3b8")
round_label.pack(pady=5)

battle = tk.Frame(root, bg="#0f172a")
battle.pack(pady=10)

user_display = tk.Label(battle, text="❔\nYou", font=("Arial", 26, "bold"), width=12, height=3, bg="#1e293b", fg="#38bdf8")
user_display.pack(side="left", padx=20)

create_label(battle, "VS", 22, "#facc15").pack(side="left", padx=10)

computer_display = tk.Label(battle, text="❔\nComputer", font=("Arial", 26, "bold"), width=12, height=3, bg="#1e293b", fg="#f87171")
computer_display.pack(side="left", padx=20)

result_label = create_label(root, "MAKE YOUR MOVE!", 20, "#60a5fa")
result_label.pack(pady=15)

create_label(root, "CHOOSE YOUR WEAPON", 13, "white").pack(pady=10)

choice_frame = tk.Frame(root, bg="#0f172a")
choice_frame.pack()

for choice in choices:
    btn = tk.Button(choice_frame, text=f"{emojis[choice]}\n{choice.upper()}", font=("Arial", 15, "bold"), width=12, height=3, bg=colors[choice], fg="white", activebackground="#38bdf8", bd=0, cursor="hand2", command=lambda c=choice: play_game(c))
    btn.pack(side="left", padx=12)
    btn.bind("<Enter>", lambda e, b=btn: b.config(bg="#475569"))
    btn.bind("<Leave>", lambda e, b=btn, c=choice: b.config(bg=colors[c]))

streak_label = create_label(root, "🔥 Winning Streak: 0", 12, "#facc15")
streak_label.pack(pady=15)

controls = tk.Frame(root, bg="#0f172a")
controls.pack(pady=10)

tk.Button(controls, text="🔄 RESET GAME", command=reset_game, bg="#dc2626", fg="white", font=("Arial", 11, "bold"), width=18, height=2, bd=0).pack(side="left", padx=10)
tk.Button(controls, text="❌ EXIT GAME", command=root.destroy, bg="#475569", fg="white", font=("Arial", 11, "bold"), width=18, height=2, bd=0).pack(side="left", padx=10)

create_label(root, "GOOD LUCK! MAY THE BEST PLAYER WIN!", 9, "#64748b").pack(pady=12)

update_score()
root.mainloop()
