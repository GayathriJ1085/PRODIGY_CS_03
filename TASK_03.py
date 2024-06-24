import tkinter as tk
from tkinter import messagebox
import re

def assess_password_strength(password):
    feedback = []
    strength_score = 0
    
    
    if len(password) <= 8:
        feedback.append("Password should be more than 8 characters long for better strength.")
    else:
        strength_score += 1
    

    if re.search(r'[A-Z]', password):
        strength_score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")
    
    
    if re.search(r'[a-z]', password):
        strength_score += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")
    
    
    if re.search(r'[0-9]', password):
        strength_score += 1
    else:
        feedback.append("Password should contain at least one number.")
    
    
    if re.search(r'[\W_]', password):
        strength_score += 1
    else:
        feedback.append("Password should contain at least one special character.")
    
    
    if len(password) <= 8 and strength_score >= 4:
        feedback.append("Password is very STRONG")
    elif strength_score == 5:
        feedback.append("Password is strong.")
    elif strength_score == 4:
        feedback.append("Password is fine.")
    elif strength_score == 3:
        feedback.append("Password is moderate.")
    else:
        feedback.append("Password is weak.")
    
    return {
        "strength_score": strength_score,
        "feedback": feedback
    }

def check_password():
    password = password_entry.get()
    result = assess_password_strength(password)
    message = f"Strength: {result['strength_score']}\nFeedback: {' '.join(result['feedback'])}"
    messagebox.showinfo("Password Strength", message)

root = tk.Tk()
root.title("Password Strength Checker")

tk.Label(root, text="Enter your password:").grid(row=0, column=0, padx=10, pady=10)
password_entry = tk.Entry(root, show="*", width=30)
password_entry.grid(row=0, column=1, padx=10, pady=10)

check_button = tk.Button(root, text="Check Password Strength", command=check_password)
check_button.grid(row=1, column=0, columnspan=2, pady=10)

root.mainloop()
