import os
import tkinter as tk
from tkinter import filedialog
import json
import random

# Check for the existence of the "Trainer Saves" directory and create it if it doesn't exist
save_directory = "Trainer Saves"
if not os.path.exists(save_directory):
    os.makedirs(save_directory)

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
    filename = file_name_entry.get()
    if filename:
        filepath = os.path.join(save_directory, filename + ".json")
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
    train_window.geometry("500x300")

    current_number = tk.StringVar(train_window, value="00")

    def next_pair():
        info_label.config(text="")  # Clear the displayed word
        row = random.randint(0, 9)
        col = random.randint(0, 9)
        number = f"{row}{col}"  # Generating number as row-column combination
        current_number.set(number)

    def show_info():
        info_label.config(text=data.get(current_number.get(), "No info available"))

    number_label = tk.Label(train_window, textvariable=current_number, font=("Helvetica", 48), bg=bg_color, fg=fg_color)
    number_label.pack(pady=20)

    info_label = tk.Label(train_window, font=("Helvetica", 24), bg=bg_color, fg=fg_color)
    info_label.pack(pady=10)

    show_button = tk.Button(train_window, text="Show", command=show_info, bg=btn_color, fg=fg_color, font=("Helvetica", 30))
    show_button.pack(side=tk.LEFT, padx=20, pady=20)

    next_button = tk.Button(train_window, text="Next", command=next_pair, bg=btn_color, fg=fg_color, font=("Helvetica", 30))
    next_button.pack(side=tk.RIGHT, padx=20, pady=20)

root = tk.Tk()
root.title("Multiplication Table Editor")
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
train_button.grid(row=14, column=4, columnspan=2, padx=5, pady=5)

file_name_entry = tk.Entry(root, bg=entry_bg, fg=entry_fg, font=cell_font)
file_name_entry.grid(row=14, column=7, columnspan=3, padx=5, pady=5)

file_name_entry = tk.Entry(root, bg=entry_bg, fg=entry_fg, font=cell_font)
file_name_entry.grid(row=14, column=7, columnspan=3, padx=5, pady=5)

# Small italic text label for instructions
instruction_label_font = ("Helvetica", 10, "italic")
instruction_label = tk.Label(root, text="Enter filename before pressing save", bg=bg_color, fg=fg_color, font=instruction_label_font)
instruction_label.grid(row=15, column=7, columnspan=3, padx=5, pady=10)

save_button = tk.Button(root, text="Save Data", command=save_data, bg=btn_color, fg=fg_color, font=button_font)
save_button.grid(row=14, column=10, columnspan=3, padx=5, pady=5)

root.mainloop()