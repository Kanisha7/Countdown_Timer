import time
import threading
import sys
import tkinter as tk
from tkinter import messagebox
import winsound

# Global flag to pause/resume the timer
paused = False

# Function to run the countdown
def run_countdown(duration, label):
    global paused
    while duration:
        if paused:
            time.sleep(1)
            continue
        mins, secs = divmod(duration, 60)
        time_format = f'{mins:02d}:{secs:02d}'
        label.config(text=time_format)
        label.update()
        time.sleep(1)
        duration -= 1
    
    label.config(text="Time's up!")
    show_notification()
    play_sound()

# Function to display a popup notification
def show_notification():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    messagebox.showinfo("Countdown Timer", "Time's up!")

# Function to play a sound alert
def play_sound():
    winsound.Beep(1000, 1000)  # Frequency = 1000 Hz, Duration = 1 sec

# Function to pause or resume the timer
def toggle_pause():
    global paused
    paused = not paused

# Function to start the countdown timer
def initiate_countdown(duration, label):
    timer_thread = threading.Thread(target=run_countdown, args=(duration, label))
    timer_thread.start()

# Function to handle user input from GUI
def start_timer(entry, label):
    user_input = entry.get().strip()
    if user_input.endswith('m'):
        duration = int(user_input[:-1]) * 60
    elif user_input.endswith('s'):
        duration = int(user_input[:-1])
    else:
        label.config(text="Invalid format! Use 'm' or 's'.")
        return
    label.config(text=f"Starting countdown for {duration} seconds...")
    initiate_countdown(duration, label)

# Create GUI window
def create_gui():
    root = tk.Tk()
    root.title("Countdown Timer")
    root.geometry("300x200")
    
    label = tk.Label(root, text="Enter countdown time (e.g., 2m, 30s):", font=("Arial", 12))
    label.pack(pady=10)
    
    entry = tk.Entry(root, font=("Arial", 12))
    entry.pack(pady=5)
    
    start_button = tk.Button(root, text="Start", font=("Arial", 12), command=lambda: start_timer(entry, label))
    start_button.pack(pady=5)
    
    pause_button = tk.Button(root, text="Pause/Resume", font=("Arial", 12), command=toggle_pause)
    pause_button.pack(pady=5)
    
    root.mainloop()

if __name__ == "__main__":
    create_gui()
