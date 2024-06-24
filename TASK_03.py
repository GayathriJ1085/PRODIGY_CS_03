import tkinter as tk
from tkinter import messagebox
import re

def assess_password_strength(password):
    feedback = []
    strength_score = 0
    
    
    if len(password) <= 8:
        feedback.append("\n ->Password should be more than 8 characters long for better strength.")
    else:
        strength_score += 1
    

    if re.search(r'[A-Z]', password):
        strength_score += 1
    else:
        feedback.append("\n ->Password should contain at least one uppercase letter.")
    
    
    if re.search(r'[a-z]', password):
        strength_score += 1
    else:
        feedback.append("\n ->Password should contain at least one lowercase letter.")
    
    
    if re.search(r'[0-9]', password):
        strength_score += 1
    else:
        feedback.append("\n ->Password should contain at least one number.")
    
    
    if re.search(r'[\W_]', password):
        strength_score += 1
    else:
        feedback.append("\n ->Password should contain at least one special character.")
    
    
    if len(password) <= 8 and strength_score >= 4:
        feedback.append("\n ->Password is very STRONG")
    elif strength_score == 5:
        feedback.append("\n ->Password is strong.")
    elif strength_score == 4:
        feedback.append("\n ->Password is fine.")
    elif strength_score == 3:
        feedback.append("\n ->Password is moderate.")
    else:
        feedback.append("\n ->Password is weak.")
    
    return {
        "feedback": feedback
    }

def check_password():
    password = password_entry.get()
    result = assess_password_strength(password)
    message = f"\nFeedback: {' '.join(result['feedback'])}"
    messagebox.showinfo("Password Strength", message)

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("600x400")
root.configure(bg='lightgrey')

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

title_label = tk.Label(root, text="Password Strength Checker", font=("Algerian", 28), bg='lightgrey')
title_label.grid(row=0, column=0, columnspan=3, pady=20)

instruction_label = tk.Label(root, text="Enter your password:",font=("arial", 14,'bold'), bg='lightgrey')
instruction_label.grid(row=1, column=0, columnspan=3, pady=10)

password_entry = tk.Entry(root, show="*", width=30)
password_entry.grid(row=2, column=0, columnspan=3, pady=10)

check_button = tk.Button(root, text="Check Password Strength", command=check_password, bg='white')
check_button.grid(row=3, column=0, columnspan=3, pady=20)

root.mainloop()
