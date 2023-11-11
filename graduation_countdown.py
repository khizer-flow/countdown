import tkinter as tk
from datetime import datetime, timedelta
import os
import json

def start_countdown():
    input_date_str = entry.get()
    input_date = datetime.strptime(input_date_str, "%Y-%m-%d")
    graduation_date = input_date + timedelta(days=4*365)
    save_date(input_date_str)
    hide_entry_and_button()
    update_dynamic_countdown(graduation_date)

def hide_entry_and_button():
    date_label.pack_forget()
    entry.pack_forget()
    start_button.pack_forget()

def update_countdown(graduation_date):
    remaining_time = graduation_date - datetime.now()

    # Calculate days, hours, minutes, and seconds
    days = remaining_time.days
    hours, remainder = divmod(remaining_time.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    label.config(text=f"Time until graduation: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")
    label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Manually center the label text

def update_dynamic_countdown(graduation_date):
    update_countdown(graduation_date)
    app.after(1000, lambda: update_dynamic_countdown(graduation_date))

def save_date(input_date):
    data = {"input_date": input_date}
    with open("data.json", "w") as f:
        json.dump(data, f)

def load_date():
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
            return data["input_date"]
    except (json.JSONDecodeError, FileNotFoundError, KeyError):
        return None

# Create and configure the Tkinter window
app = tk.Tk()
app.title("Graduation Countdown")

# Set background color and window dimensions
app.configure(bg='black')
app.geometry("400x300")  # Set your preferred dimensions

# Label and Entry for date input
date_label = tk.Label(app, text="Enter the YEAR-Month-DAY:", fg='white', bg='black', font=("Arial", 14))
entry = tk.Entry(app, width=20, font=("Arial", 12))
start_button = tk.Button(app, text="Start Countdown", command=start_countdown, font=("Arial", 12), bg='green', fg='white')

# Label for countdown display
label = tk.Label(app, text="", font=("Helvetica", 16, "bold"), fg='white', bg='black')

# Pack widgets into the window
date_label.pack(pady=10)
entry.pack(pady=10)
start_button.pack(pady=10)
label.pack(pady=20)  # Increased padding to center the countdown

# Load previously saved date
saved_date = load_date()
if saved_date:
    entry.insert(0, saved_date)

# Run the app
app.mainloop()
