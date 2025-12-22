import tkinter as tk

# creates main window
screen = tk.Tk()
screen.title("My App")           # Set window title
screen.attributes("-fullscreen", True)
# makes button
# lamda is a quick way to write a small function
# pack() puts it on the screen 
tk.Button(screen, text="Click Me", command=lambda: print("Clicked!")).pack()


screen.mainloop()