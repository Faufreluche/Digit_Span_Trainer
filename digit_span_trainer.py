import os
import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog
import json
import random
import pygame
import time

pygame.mixer.init()

# Dark theme colors
bg_color = "#333333"  # Background color
fg_color = "#FFFFFF"  # Foreground (text) color
btn_color = "#555555"  # Button color
entry_bg = "#555555"  # Entry background color
entry_fg = "#FFFFFF"  # Entry text color

data = {}  # Global variable to hold the loaded data

def load_data():
    global data
    filename = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
    if filename:
        with open(filename, "r") as file:
            data = json.load(file)
            for r in range(10):
                for c in range(10):
                    key = f"{r}{c}"  # Concatenating row and column
                    cells[r][c].delete(0, tk.END)
                    cells[r][c].insert(0, data.get(key, ""))

def save_data():
    data_to_save = {}
    for r in range(10):
        for c in range(10):
            key = f"{r}{c}"  # Concatenating row and column
            data_to_save[key] = cells[r][c].get()

    # Ask the user to provide a filename and select a directory to save the file
    filepath = filedialog.asksaveasfilename(
        defaultextension=".json",
        filetypes=[("JSON Files", "*.json")]
    )

    if filepath:  # Check if a filename was entered
        with open(filepath, "w") as file:
            json.dump(data_to_save, file)

def clear_data():
    for row_cells in cells:
        for cell in row_cells:
            cell.delete(0, tk.END)

def train():
    train_window = tk.Toplevel(root)
    train_window.title("Training")
    train_window.configure(bg=bg_color)
    train_window.geometry("700x700")

    wait_after_sound = scale.get()
    current_number = tk.StringVar(train_window, value="00")
    show_auto = show_auto_var.get()

    # Create initial fonts
    number_font = tkFont.Font(family="Helvetica", size=48)
    info_font = tkFont.Font(family="Helvetica", size=24)

    def resize_fonts(event):
        # Adjust font sizes based on the window size
        # The number font is always larger
        new_number_size = max(300, min(event.width // 15, event.height // 8))  # Larger minimum size
        new_info_size = max(20, new_number_size // 5)  # Proportionally smaller than the number size
        number_font.config(size=new_number_size)
        info_font.config(size=new_info_size)

    # Bind resize event to the train window
    train_window.bind("<Configure>", resize_fonts)

    def next_pair():
        info_label.config(text="")  # Clear the displayed word

        row = random.randint(0, 9)
        col = random.randint(0, 9)
        number = f"{row}{col}"  # Generating number as row-column combination
        current_number.set(number)
        
        # Translate the number into a sound file name where 1 is yks, 2 is kaks, etc.
        base_sound_directory = "Soundmodels/3/"
        number_1 = str(row)
        number_2 = str(col)
        number_to_sound = {
            "0": "null",
            "1": "yks",
            "2": "kaks",
            "3": "kolm",
            "4": "neli",
            "5": "viis",
            "6": "kuus",
            "7": "seitse",
            "8": "kaheksa",
            "9": "yheksa"
        }
        number_text_1 = number_to_sound.get(number_1, "null")
        number_text_2 = number_to_sound.get(number_2, "null")
        
        # Create sound file paths for first and second numbers
        sound_file_1 = os.path.join(base_sound_directory, f"{number_text_1}.mp3")
        sound_file_2 = os.path.join(base_sound_directory, f"{number_text_2}.mp3")
        
        # Load and play the corresponding sound files sequentially
        sound_1 = pygame.mixer.Sound(sound_file_1)
        sound_2 = pygame.mixer.Sound(sound_file_2)
        
        sound_1.play()
        pygame.time.delay(int(sound_1.get_length() * 1000))  # Delay for the duration of the first sound
        sound_2.play()
        pygame.time.delay(int(sound_2.get_length() * 1000))  # Delay for the duration of the first sound
        
        # Delay for 3 seconds
        time.sleep(wait_after_sound)

        if show_auto:
            show_info()

    def show_info():
        info_label.config(text=data.get(current_number.get(), "No info available"))
        
    # Functions to be called on key presses
    def on_left_arrow(event):
        show_info()

    def on_right_arrow(event):
        next_pair()

    # Bind key events to the train window
    train_window.bind("<Left>", on_left_arrow)
    train_window.bind("<Right>", on_right_arrow)

    # Configure grid weights for dynamic resizing
    train_window.grid_columnconfigure(0, weight=1)
    train_window.grid_columnconfigure(1, weight=1)
    train_window.grid_rowconfigure(1, weight=1)
    train_window.grid_rowconfigure(2, weight=1)

    # Widgets creation with dynamic font resizing
    number_label = tk.Label(train_window, textvariable=current_number, font=number_font, bg=bg_color, fg=fg_color)
    number_label.grid(row=0, column=0, columnspan=2, sticky="nsew")

    info_label = tk.Label(train_window, font=info_font, bg=bg_color, fg=fg_color)
    info_label.grid(row=1, column=0, columnspan=2, sticky="nsew")

    show_button = tk.Button(train_window, text="<- Show", command=show_info, bg=btn_color, fg=fg_color, font=("Helvetica", 30))
    show_button.grid(row=2, column=0, sticky="nsew")

    next_button = tk.Button(train_window, text="Next ->", command=next_pair, bg=btn_color, fg=fg_color, font=("Helvetica", 30))
    next_button.grid(row=2, column=1, sticky="nsew")

root = tk.Tk()
root.title("Digit Span Trainer")
root.configure(bg=bg_color)
root.geometry("1320x600")

cell_font = ("Helvetica", 14)
label_font = ("Helvetica", 14)
button_font = ("Helvetica", 14)

cells = [[tk.Entry(root, width=10, bg=entry_bg, fg=entry_fg, font=cell_font) for _ in range(10)] for _ in range(10)]

# Secondary titles for rows and columns
row_titles = ["n", "l", "kg", "m", "t", "v", "p b", "s", "r", "j d h"]
column_titles = ["n", "l", "kg", "m", "t", "v", "p b", "s", "r", "j d h"]

# Grid setup for row numbers and their corresponding titles
for r in range(10):
    tk.Label(root, text=str(r), bg=bg_color, fg=fg_color, font=label_font).grid(row=r+2, column=1)
    tk.Label(root, text=row_titles[r], bg=bg_color, fg=fg_color, font=label_font).grid(row=r+2, column=0)

    for c in range(10):
        cells[r][c].grid(row=r+2, column=c+2, padx=5, pady=5)

# Place column numbers and titles in separate rows at the top
for c in range(10):
    tk.Label(root, text=str(c), bg=bg_color, fg=fg_color, font=label_font).grid(row=0, column=c+2)
    tk.Label(root, text=column_titles[c], bg=bg_color, fg=fg_color, font=label_font).grid(row=1, column=c+2)

# Define a larger font for the "Train" button
train_button_font = ("Helvetica", 20)

# Define a reddish hue for the "Clear Data" button
clear_button_color = "#ff5555"

load_button = tk.Button(root, text="Load Data", command=load_data, bg=btn_color, fg=fg_color, font=button_font)
load_button.grid(row=14, column=0, columnspan=3, padx=5, pady=5)

clear_button = tk.Button(root, text="Clear Data", command=clear_data, bg=clear_button_color, fg=fg_color, font=button_font)
clear_button.grid(row=15, column=0, columnspan=3, padx=5, pady=5)

train_button = tk.Button(root, text="Train", command=train, bg=btn_color, fg=fg_color, font=train_button_font)
train_button.grid(row=15, column=3, columnspan=2, padx=5, pady=5)

save_button = tk.Button(root, text="Save Data", command=save_data, bg=btn_color, fg=fg_color, font=button_font)
save_button.grid(row=14, column=10, columnspan=3, padx=5, pady=5)

# Create a slider in the root window
scale = tk.Scale(root, from_=0, to=20, orient=tk.HORIZONTAL, length=300, bg=bg_color, fg=fg_color, font=button_font)
scale.grid(row=15, column=5, columnspan=10, padx=0, pady=0)

# Add label for slider in small italic font
scale_label = tk.Label(root, text="Delay (s) after sound before showing answer", bg=bg_color, fg=fg_color, font=("Helvetica", 10))
scale_label.grid(row=16, column=5, columnspan=10, padx=0, pady=0)

# Checkbox for showing answer automatically
show_auto_var = tk.IntVar()
show_auto_checkbox = tk.Checkbutton(root, text="Show Automatically", var=show_auto_var, bg=bg_color, fg=fg_color, selectcolor=bg_color, font=("Helvetica", 12))
show_auto_checkbox.grid(row=15, column=4, columnspan=3, padx=5, pady=5)

root.mainloop()
