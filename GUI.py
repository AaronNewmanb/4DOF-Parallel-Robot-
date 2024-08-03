import tkinter as tk
from tkinter import messagebox
import serial
import time

# Create the main window
root = tk.Tk()
root.title("Robot Arm Controller")

# Create and place the widgets
tk.Label(root, text="Speed (steps/sec):").grid(row=0, column=0, padx=10, pady=10)
speed_entry = tk.Entry(root)
speed_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Acceleration (steps^2/sec):").grid(row=1, column=0, padx=10, pady=10)
acceleration_entry = tk.Entry(root)
acceleration_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Position (steps):").grid(row=2, column=0, padx=10, pady=10)
position_slider = tk.Scale(root, from_=-2000, to=2000, orient=tk.HORIZONTAL)
position_slider.grid(row=2, column=1, padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()
