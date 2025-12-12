import tkinter as tk

# creates main window
screen = tk.Tk()
screen.title("My App")           # Set window title
screen.resizable(False, False)   # Prevent resizing
screen.minsize(300, 200)         # Set minimum size
screen.maxsize(800, 600)         # Set maximum size

# makes button
# lamda is a quick way to write a small function
# pack() puts it on the screen 
tk.Button(screen, text="Click Me", command=lambda: print("Clicked!")).pack()

screen.mainloop()