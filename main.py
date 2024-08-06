import tkinter as tk
from GUI import create_gui  # Import the function to create the GUI
import Data_Sender  # Import the module that handles sending data

def main():
    root = tk.Tk()
    root.title("Robot Arm Controller")

    # Initialize the GUI
    create_gui(root)

    # Run the main loop
    root.mainloop()

if __name__ == "__main__":
    main()