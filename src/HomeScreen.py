import tkinter as tk
from tkinter import Frame, Label, Button
from PIL import Image, ImageTk
import os

def show_screen(screen_name):
    """Show the specified screen and hide others"""
    for name, screen in screens.items():
        if name == screen_name:
            screen.pack(fill='both', expand=True)
        else:
            screen.pack_forget()

def on_call_button(number):
    """Handle call button press"""
    print(f"Calling {number}...")

# Create main window
root = tk.Tk()
root.title("Home Screen")

# Fullscreen mode
root.attributes('-fullscreen', True)
root.bind('<Escape>', lambda e: root.attributes('-fullscreen', False))

# Dictionary to hold all screens
screens = {}

# --- Home Screen ---
home_screen = Frame(root)
screens['home'] = home_screen

# Try to load background image
bg_image = None
if os.path.exists("assets/homeScreen.png"):
    try:
        img = Image.open("assets/homeScreen.png")
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        img = img.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
        bg_image = ImageTk.PhotoImage(img)
        
        bg_label = Label(home_screen, image=bg_image)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    except Exception as e:
        print(f"Could not load background image: {e}")
        home_screen.configure(bg='black')
else:
    home_screen.configure(bg='black')

# Time label
time_label = Label(
    home_screen,
    text="12:45",
    font=('Arial', 30),
    fg='white',
    bg='black'
)
time_label.place(x=10, y=400)

# Date label
date_label = Label(
    home_screen,
    text="Sep 22, 2025",
    font=('Arial', 20),
    fg='white',
    bg='black'
)
date_label.place(x=10, y=430)

# Call button
call_btn = Button(
    home_screen,
    text="Call",
    width=12,
    height=2,
    command=lambda: show_screen('call')
)
call_btn.place(x=10, y=50)

# Text button
text_btn = Button(
    home_screen,
    text="Text",
    width=12,
    height=2,
    command=lambda: show_screen('text')
)
text_btn.place(x=10, y=100)

# --- Call Screen ---
call_screen = Frame(root, bg='white')
screens['call'] = call_screen

# Create grid of buttons (3x3 for numbers 1-9)
button_frame = Frame(call_screen, bg='white')
button_frame.place(relx=0.5, rely=0.5, anchor='center')

# Buttons 1-9
for i in range(1, 10):
    row = (i - 1) // 3
    col = (i - 1) % 3
    btn = Button(
        button_frame,
        text=str(i),
        width=10,
        height=3,
        command=lambda num=i: on_call_button(num)
    )
    btn.grid(row=row, column=col, padx=5, pady=5)

# Back button
call_back_btn = Button(
    call_screen,
    text="Back",
    width=12,
    height=2,
    command=lambda: show_screen('home')
)
call_back_btn.place(x=10, y=10)

# --- Text Screen ---
text_screen = Frame(root, bg='white')
screens['text'] = text_screen

# Back button
text_back_btn = Button(
    text_screen,
    text="Back",
    width=12,
    height=2,
    command=lambda: show_screen('home')
)
text_back_btn.place(x=10, y=50)

# Show home screen initially
show_screen('home')

# Start the application
root.mainloop()