#importting the required libraries
import random
import tkinter as tk
from tkinter import ttk, messagebox, font

#setting the initial state and reward
current_state = 0
current_reward = -5

#defining the transition function
def transition_function(action):
    global current_state
    if action == -1:
        if(random.random() <0.8):
            current_state -=1
        else:
            current_state +=1
    elif action == 1:
        if(random.random() <0.7):
            current_state -=1
        else:
            current_state +=1
    else:
        print("Invalid action") 
    reward_function()

#defining the reward function
def reward_function():
    global current_reward
    if current_state == -2:
        current_reward = 20
    elif current_state == 2:
        current_reward =  100
    else:
        current_reward = -5

#defining the reset function
def reset_game():
    global current_state, current_reward
    current_state = 0
    reward_function()
    update_display()

#defining the function to update the display window
def update_display():
    state_label.config(text=f"Current State: {current_state}")
    reward_label.config(text=f"Reward: {current_reward}")
    
    
#defining the start function and creating the game window
def start_game():
    root.withdraw()
    global current_state, current_reward
    current_state = 0
    reward_function()
    
    global game_window
    game_window = tk.Toplevel(root)
    game_window.title("MDP Game")
    game_window.option_add("*Font", ("Montserrat", 14))
    
    global state_label, reward_label
    state_label = ttk.Label(game_window, text=f"Current State: {current_state}" )
    state_label.pack()
    reward_label = ttk.Label(game_window, text=f"Reward: {current_reward}")
    reward_label.pack()
    
    button_frame = ttk.Frame(game_window)
    button_frame.pack(pady=20)
    
    ttk.Button(button_frame, text="-1", command=lambda: take_action(-1)).pack(side=tk.LEFT, padx=10)
    ttk.Button(button_frame, text="+1", command=lambda: take_action(+1)).pack(side=tk.RIGHT, padx=10)
    
    ttk.Button(game_window, text="Reset Game", command=reset_game).pack(side=tk.BOTTOM, pady=10)
    
    # Bind the close event of game window to opening the root window
    game_window.protocol("WM_DELETE_WINDOW", on_game_window_close)


# Function to restore the root window when game_window is closed
def on_game_window_close():
    root.deiconify()
    game_window.destroy()

#defining the take action function
def take_action(action):
    global current_reward
    transition_function(action)
    reward_function()
    update_display()
    if(current_state == -2 or current_state == 2):
        game_window.destroy()
        messagebox.showinfo("Game Over 👾", f"Game Over, you have reached the final state!\n{'+'*39}\nYour Final State is: {current_state},\nYour Final Reward is: {current_reward}\n{'+'*39}\nThank you for playing !!!")
        root.deiconify()

#defining the main application window
root = tk.Tk()
root.title("MDP Game")

# Apply a theme to the UI
style = ttk.Style()
style.theme_use('clam') 

# Title label
style.configure('TLabel', font=("Montserrat", 18, "bold"), background="#ffffff", foreground="black")
title_label = ttk.Label(root, text="MDP Game", background="white", style="TLabel")
title_label.pack(pady=20, padx=10)

# Start button 
style.configure('TButton', font=("Montserrat", 12, "bold"), background="#D3D3D3", foreground="black", relief="raised" , padding=5, width=20, bordercolor="black")
start_button = ttk.Button(root, text="Start Game", command=start_game, style="TButton")    
start_button.pack(pady=20, padx=10)

#Start the main loop
root.mainloop()

# End of the code