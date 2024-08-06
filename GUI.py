import tkinter as tk
from tkinter import messagebox

# Create the main window
Baseposition = 0
Shoulderposition = 0
Elbowposition = 0
Wristposition = 0
BaseAngle = 0.0
ShoulderAngle = 0.0
ElbowAngle = 0.0
WristAngle = 0.0
speed = 0.0
acceleration = 0.0

root = tk.Tk()
root.title("Robot Arm Controller")


def jog(Motor, direction, steps):
    # Motor: 0 = base, 1 = shoulder, 2 = elbow, 3 = wrist
    # direction: 0 = negative, 1 = positive
    # steps: number of steps to jog
    global Baseposition, Shoulderposition, Elbowposition, Wristposition
    if Motor == 0:
        if direction == 0:
            Baseposition -= steps
        else:
            Baseposition += steps
    elif Motor == 1:
        if direction == 0:
            Shoulderposition -= steps
        else:
            Shoulderposition += steps
    elif Motor == 2:
        if direction == 0:
            Elbowposition -= steps
        else:
            Elbowposition += steps
    elif Motor == 3:
        if direction == 0:
            Wristposition -= steps
        else:
            Wristposition += steps
    else:
        pass
    pass














# Function to open the set variables window
set_variables_window = None

def open_set_variables_window():
    global set_variables_window
    set_variables_window = tk.Toplevel(root)
    set_variables_window.title("Set Variables")

    # Create and place the widgets
    tk.Label(set_variables_window, text="Speed (steps/sec):").grid(row=0, column=0, padx=10, pady=10)
    speed_entry = tk.Entry(set_variables_window)
    speed_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(set_variables_window, text="Acceleration (steps^2/sec):").grid(row=1, column=0, padx=10, pady=10)
    acceleration_entry = tk.Entry(set_variables_window)
    acceleration_entry.grid(row=1, column=1, padx=10, pady=10)
    
    def update_variables():
        global speed, acceleration
        speed = int(speed_entry.get())
        acceleration = int(acceleration_entry.get())
        set_variables_window.destroy()

    # Create the update button
    update_button = tk.Button(set_variables_window, text="Update", command=update_variables)
    update_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Functionality for jogging the motors
def jog(Motor, direction, steps):
    # Motor: 0 = base, 1 = shoulder, 2 = elbow, 3 = wrist
    # direction: 0 = negative, 1 = positive
    # steps: number of steps to jog
    pass

# Functionality for jogging the base
def jogbase():
    jog_window = tk.Toplevel(root)
    jog_window.title("Jog Base")

    # Create and place the buttons
    tk.Button(jog_window, text="+1", command=lambda: jog(0, 1, 1)).grid(row=0, column=0, padx=10, pady=10)
    tk.Button(jog_window, text="+10", command=lambda: jog(0, 1, 10)).grid(row=0, column=1, padx=10, pady=10)
    tk.Button(jog_window, text="+100", command=lambda: jog(0, 1, 100)).grid(row=0, column=2, padx=10, pady=10)
    tk.Button(jog_window, text="-1", command=lambda: jog(0, 0, 1)).grid(row=1, column=0, padx=10, pady=10)
    tk.Button(jog_window, text="-10", command=lambda: jog(0, 0, 10)).grid(row=1, column=1, padx=10, pady=10)
    tk.Button(jog_window, text="-100", command=lambda: jog(0, 0, 100)).grid(row=1, column=2, padx=10, pady=10)




# Create and place the widgets
def set_variables():
    set_variables_window = tk.Toplevel(root)
    set_variables_window.title("Set Variables")

    # Create and place the widgets
    tk.Label(set_variables_window, text="Speed (steps/sec):").grid(row=0, column=0, padx=10, pady=10)
    speed_entry = tk.Entry(set_variables_window)
    speed_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(set_variables_window, text="Acceleration (steps^2/sec):").grid(row=1, column=0, padx=10, pady=10)
    acceleration_entry = tk.Entry(set_variables_window)
    acceleration_entry.grid(row=1, column=1, padx=10, pady=10)
    
    def update_variables():
        global speed, acceleration
        speed = int(speed_entry.get())
        acceleration = int(acceleration_entry.get())
        set_variables_window.destroy()

    # Create the update button
    update_button = tk.Button(set_variables_window, text="Update", command=update_variables)
    update_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
def jogbase():

    jog_window = tk.Toplevel(root)
    jog_window.title("Jog Base")

    # Create and place the buttons
    tk.Button(jog_window, text="+1", command=lambda: jog(0, 1, 1)).grid(row=0, column=0, padx=10, pady=10)
    tk.Button(jog_window, text="+10", command=lambda: jog(0, 1, 10)).grid(row=0, column=1, padx=10, pady=10)
    tk.Button(jog_window, text="+100", command=lambda: jog(0, 1, 100)).grid(row=0, column=2, padx=10, pady=10)
    tk.Button(jog_window, text="-1", command=lambda: jog(0, 0, 1)).grid(row=1, column=0, padx=10, pady=10)
    tk.Button(jog_window, text="-10", command=lambda: jog(0, 0, 10)).grid(row=1, column=1, padx=10, pady=10)
    tk.Button(jog_window, text="-100", command=lambda: jog(0, 0, 100)).grid(row=1, column=2, padx=10, pady=10)
def jogelbow():
    jog_window = tk.Toplevel(root)
    jog_window.title("Jog Elbow")

    # Create and place the buttons
    tk.Button(jog_window, text="+1", command=lambda: jog(2, 1, 1)).grid(row=0, column=0, padx=10, pady=10)
    tk.Button(jog_window, text="+10", command=lambda: jog(2, 1, 10)).grid(row=0, column=1, padx=10, pady=10)
    tk.Button(jog_window, text="+100", command=lambda: jog(2, 1, 100)).grid(row=0, column=2, padx=10, pady=10)
    tk.Button(jog_window, text="-1", command=lambda: jog(2, 0, 1)).grid(row=1, column=0, padx=10, pady=10)
    tk.Button(jog_window, text="-10", command=lambda: jog(2, 0, 10)).grid(row=1, column=1, padx=10, pady=10)
    tk.Button(jog_window, text="-100", command=lambda: jog(2, 0, 100)).grid(row=1, column=2, padx=10, pady=10)
def jogshoulder():
    jog_window = tk.Toplevel(root)
    jog_window.title("Jog Shoulder")

    # Create and place the buttons
    tk.Button(jog_window, text="+1", command=lambda: jog(1, 1, 1)).grid(row=0, column=0, padx=10, pady=10)
    tk.Button(jog_window, text="+10", command=lambda: jog(1, 1, 10)).grid(row=0, column=1, padx=10, pady=10)
    tk.Button(jog_window, text="+100", command=lambda: jog(1, 1, 100)).grid(row=0, column=2, padx=10, pady=10)
    tk.Button(jog_window, text="-1", command=lambda: jog(1, 0, 1)).grid(row=1, column=0, padx=10, pady=10)
    tk.Button(jog_window, text="-10", command=lambda: jog(1, 0, 10)).grid(row=1, column=1, padx=10, pady=10)
    tk.Button(jog_window, text="-100", command=lambda: jog(1, 0, 100)).grid(row=1, column=2, padx=10, pady=10)
def jogwrist():
    jog_window = tk.Toplevel(root)
    jog_window.title("Jog Wrist")

    # Create and place the buttons
    tk.Button(jog_window, text="+1", command=lambda: jog(3, 1, 1)).grid(row=0, column=0, padx=10, pady=10)
    tk.Button(jog_window, text="+10", command=lambda: jog(3, 1, 10)).grid(row=0, column=1, padx=10, pady=10)
    tk.Button(jog_window, text="+100", command=lambda: jog(3, 1, 100)).grid(row=0, column=2, padx=10, pady=10)
    tk.Button(jog_window, text="-1", command=lambda: jog(3, 0, 1)).grid(row=1, column=0, padx=10, pady=10)
    tk.Button(jog_window, text="-10", command=lambda: jog(3, 0, 10)).grid(row=1, column=1, padx=10, pady=10)
    tk.Button(jog_window, text="-100", command=lambda: jog(3, 0, 100)).grid(row=1, column=2, padx=10, pady=10)

set_variables_button = tk.Button(root, text="Set Speed and acceleration", command=set_variables)

jogbase_button = tk.Button(root, text="Jog Base", command=jogbase)
jogbase_button.grid(row=2, column=0, padx=10, pady=10)
set_variables_button.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
jogshoulder_button = tk.Button(root, text="Jog Shoulder", command=jogshoulder)
jogshoulder_button.grid(row=2, column=1, padx=10, pady=10)



jogelbow_button = tk.Button(root, text="Jog Elbow", command=jogelbow)
jogelbow_button.grid(row=3, column=0, padx=10, pady=10)


jogwrist_button = tk.Button(root, text="Jog Wrist", command=jogwrist)
jogwrist_button.grid(row=3, column=1, padx=10, pady=10)
def set_joint_angles():
    joint_angles_window = tk.Toplevel(root)
    joint_angles_window.title("Set Joint Angles")

    # Create and place the widgets
    tk.Label(joint_angles_window, text="Base Angle:").grid(row=0, column=0, padx=10, pady=10)
    base_angle_entry = tk.Entry(joint_angles_window)
    base_angle_entry.grid(row=0, column=1, padx=10, pady=10)
    base_angle_entry.insert(0, str(BaseAngle))  # Display current angle

    tk.Label(joint_angles_window, text="Shoulder Angle:").grid(row=1, column=0, padx=10, pady=10)
    shoulder_angle_entry = tk.Entry(joint_angles_window)
    shoulder_angle_entry.grid(row=1, column=1, padx=10, pady=10)
    shoulder_angle_entry.insert(0, str(ShoulderAngle))  # Display current angle

    tk.Label(joint_angles_window, text="Elbow Angle:").grid(row=2, column=0, padx=10, pady=10)
    elbow_angle_entry = tk.Entry(joint_angles_window)
    elbow_angle_entry.grid(row=2, column=1, padx=10, pady=10)
    elbow_angle_entry.insert(0, str(ElbowAngle))  # Display current angle

    tk.Label(joint_angles_window, text="Wrist Angle:").grid(row=3, column=0, padx=10, pady=10)
    wrist_angle_entry = tk.Entry(joint_angles_window)
    wrist_angle_entry.grid(row=3, column=1, padx=10, pady=10)
    wrist_angle_entry.insert(0, str(WristAngle))  # Display current angle

    def update_joint_angles():
        global BaseAngle, ShoulderAngle, ElbowAngle, WristAngle
        BaseAngle = float(base_angle_entry.get())
        ShoulderAngle = float(shoulder_angle_entry.get())
        ElbowAngle = float(elbow_angle_entry.get())
        WristAngle = float(wrist_angle_entry.get())
        joint_angles_window.destroy()

    # Create the update button
    update_button = tk.Button(joint_angles_window, text="Update", command=update_joint_angles)
    update_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

set_joint_angles_button = tk.Button(root, text="Set Joint Angles", command=set_joint_angles)
set_joint_angles_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
# Start the Tkinter event loop
root.mainloop()
