import tkinter as tk
from tkinter import messagebox
import serial
import time

# Initialize serial communication (make sure the port is correct)
try:
    ser = serial.Serial(port='COM4', baudrate=9600)
    time.sleep(2)  # Wait for the serial connection to initialize
except serial.SerialException as e:
    print(f"Error opening serial port: {e}")
    exit(1)

def send_data():
    try:
        position = int(position_slider.get())
        speed = int(speed_entry.get())
        acceleration = int(acceleration_entry.get())
        data = f"{position},{speed},{acceleration}\n"
        ser.write(data.encode('utf-8'))
        print(f"Sent data: {data.strip()}")  # Debug output
    except serial.SerialException as e:
        print(f"Error sending data: {e}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid integer values for position, speed, and acceleration.")

def reset_zero():
    position_slider.set(0)
    send_data()

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

send_button = tk.Button(root, text="Send", command=send_data)
send_button.grid(row=3, column=0, columnspan=2, pady=10)

reset_button = tk.Button(root, text="Reset Zero", command=reset_zero)
reset_button.grid(row=4, column=0, columnspan=2, pady=10)

# Start the Tkinter event loop
root.mainloop()
