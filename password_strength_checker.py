import string
import tkinter as tk
from tkinter import messagebox

def password_strength(password):
    strength = 0
    remarks = ''
    lower_count = upper_count = digit_count = space_count = special_count = 0

    # Count different character types in the password
    for char in password:
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.digits:
            digit_count += 1
        elif char == ' ':
            space_count += 1
        else:
            special_count += 1

    # Evaluate password strength based on the criteria
    if lower_count >= 1:
        strength += 1
    if upper_count >= 1:
        strength += 1
    if digit_count >= 1:
        strength += 1
    if space_count == 0:  # Spaces are not recommended
        strength += 1
    if special_count >= 1:
        strength += 1

    # Assign strength description based on strength level
    if strength == 1:
        remarks = "Weak Password, Try Stronger Criteria"
    elif strength == 2:
        remarks = "Fair Password, Needs Improvement"
    elif strength == 3:
        remarks = "Good Password, But Could Be Stronger"
    elif strength == 4:
        remarks = "Strong Password, Good"
    else:
        remarks = "Very Strong Password, Excellent!"

    return lower_count, upper_count, digit_count, space_count, special_count, strength, remarks

def display_password_analysis():
    password = password_entry.get()

    if not password:
        messagebox.showwarning("Input Error", "Please enter a password.")
        return

    lower, upper, digits, spaces, special, strength, remarks = password_strength(password)

    # Display the analysis in the labels
    lower_count_label.config(text=f"Lowercase characters: {lower}")
    upper_count_label.config(text=f"Uppercase characters: {upper}")
    digit_count_label.config(text=f"Numeric characters: {digits}")
    space_count_label.config(text=f"Whitespace characters: {spaces}")
    special_count_label.config(text=f"Special characters: {special}")
    strength_label.config(text=f"Password Strength: {strength}")
    remarks_label.config(text=f"Password Strength Evaluation: {remarks}")

def ask_for_another_password():
    # Reset the password entry field
    password_entry.delete(0, tk.END)
    
    # Clear previous analysis results
    lower_count_label.config(text="Lowercase characters: ")
    upper_count_label.config(text="Uppercase characters: ")
    digit_count_label.config(text="Numeric characters: ")
    space_count_label.config(text="Whitespace characters: ")
    special_count_label.config(text="Special characters: ")
    strength_label.config(text="Password Strength: ")
    remarks_label.config(text="Password Strength Evaluation: ")

def create_gui():
    # Set up the main window
    window = tk.Tk()
    window.title("Password Strength Checker")
    window.geometry("500x400")
    window.configure(bg="#1e1e2f")

    # Title
    title_label = tk.Label(window, text="Password Strength Checker", font=("Segoe UI", 16, "bold"), fg="white", bg="#1e1e2f")
    title_label.pack(pady=10)

    # Password Entry
    password_label = tk.Label(window, text="Enter Password:", font=("Segoe UI", 12), fg="white", bg="#1e1e2f")
    password_label.pack(pady=5)

    global password_entry
    password_entry = tk.Entry(window, font=("Segoe UI", 12), show="*", width=30)
    password_entry.pack(pady=5)

    # Check Button
    check_button = tk.Button(window, text="Check Strength", font=("Segoe UI", 12), command=display_password_analysis)
    check_button.pack(pady=10)

    # Analysis Results
    global lower_count_label, upper_count_label, digit_count_label, space_count_label, special_count_label, strength_label, remarks_label

    lower_count_label = tk.Label(window, text="Lowercase characters: ", font=("Segoe UI", 10), fg="white", bg="#1e1e2f")
    lower_count_label.pack()

    upper_count_label = tk.Label(window, text="Uppercase characters: ", font=("Segoe UI", 10), fg="white", bg="#1e1e2f")
    upper_count_label.pack()

    digit_count_label = tk.Label(window, text="Numeric characters: ", font=("Segoe UI", 10), fg="white", bg="#1e1e2f")
    digit_count_label.pack()

    space_count_label = tk.Label(window, text="Whitespace characters: ", font=("Segoe UI", 10), fg="white", bg="#1e1e2f")
    space_count_label.pack()

    special_count_label = tk.Label(window, text="Special characters: ", font=("Segoe UI", 10), fg="white", bg="#1e1e2f")
    special_count_label.pack()

    strength_label = tk.Label(window, text="Password Strength: ", font=("Segoe UI", 10), fg="white", bg="#1e1e2f")
    strength_label.pack()

    remarks_label = tk.Label(window, text="Password Strength Evaluation: ", font=("Segoe UI", 10), fg="white", bg="#1e1e2f")
    remarks_label.pack(pady=20)

    # Reset Button
    reset_button = tk.Button(window, text="Check Another Password", font=("Segoe UI", 12), command=ask_for_another_password)
    reset_button.pack()

    window.mainloop()

if __name__ == "__main__":
    create_gui()
