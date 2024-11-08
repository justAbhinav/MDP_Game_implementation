#importing the required libraries
import random
import tkinter as tk
from tkinter import ttk, messagebox
import time
from tabulate import tabulate

#defining the MDP_Game class with the required functions
class MDP_Game:
    
    #defining the constructor
    def __init__(self, root):
        self.root = root
        self.current_state = 0
        self.current_reward = -5
        
        self.setup_root_window()
    
    #defining the fucntion to setup the root/main window
    def setup_root_window(self):
        self.root.title("MDP Game")
        
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TLabel', font=("Montserrat", 18, "bold"), background="#ffffff", foreground="black")
        title_label = ttk.Label(self.root, text="MDP Game", background="white", style="TLabel")
        title_label.pack(pady=20, padx=10)
        
        style.configure('TButton', font=("Montserrat", 12, "bold"), background="#D3D3D3", foreground="black", relief="raised", padding=5, width=20, bordercolor="black")
        start_button = ttk.Button(self.root, text="Start Game", command=self.start_game, style="TButton")
        start_button.pack(pady=20, padx=10)
    
    
    #defining the transition function
    def transition_function(self,action):
        if action == -1:
            if(random.random() <0.8):
                self.current_state -=1
            else:
                self.current_state +=1
        elif action == 1:
            if(random.random() <0.7):
                self.current_state -=1
            else:
                self.current_state +=1
        else:
            print("Invalid action") 
        self.reward_function()

    #defining the reward function
    def reward_function(self):
        if self.current_state == -2:
            self.current_reward = 20
        elif self.current_state == 2:
            self.current_reward =  100
        else:
            self.current_reward = -5

    #defining the reset function
    def reset_game(self):
        self.current_state = 0
        self.reward_function()
        self.update_display()

    #defining the function to update the display window
    def update_display(self):
        self.state_label.config(text=f"Current State: {self.current_state}")
        self.reward_label.config(text=f"Reward: {self.current_reward}")
    
    
    #defining the start function and creating the game window
    def start_game(self):
        self.root.withdraw()
        self.current_state = 0
        self.reward_function()

        self.game_window = tk.Toplevel(root)
        self.game_window.title("MDP Game")
        self.game_window.option_add("*Font", ("Montserrat", 14))
        
        self.state_label = ttk.Label(self.game_window, text=f"Current State: {self.current_state}" )
        self.state_label.pack()
        self.reward_label = ttk.Label(self.game_window, text=f"Reward: {self.current_reward}")
        self.reward_label.pack()
        
        button_frame = ttk.Frame(self.game_window)
        button_frame.pack(pady=20)
        
        ttk.Button(button_frame, text="-1", command=lambda: self.take_action(-1)).pack(side=tk.LEFT, padx=10)
        ttk.Button(button_frame, text="+1", command=lambda: self.take_action(+1)).pack(side=tk.RIGHT, padx=10)
        
        ttk.Button(self.game_window, text="Reset Game", command=self.reset_game).pack(side=tk.BOTTOM, pady=10)
        
        # Bind the close event of game window to opening the root window
        self.game_window.protocol("WM_DELETE_WINDOW", self.on_game_window_close)


    # Function to restore the root window when game_window is closed
    def on_game_window_close(self):
        self.root.deiconify()
        self.game_window.destroy()

    #defining the take action function
    def take_action(self, action):
        self.transition_function(action)
        self.reward_function()
        self.update_display()
        if(self.current_state == -2 or self.current_state == 2):
            time.sleep(0.1)
            self.game_window.destroy()
            messagebox.showinfo("Game Over 👾", f"Game Over, you have reached the final state!\n{'+'*39}\nYour Final State is: {self.current_state},\nYour Final Reward is: {self.current_reward}\n{'+'*39}\nThank you for playing !!!")
            self.root.deiconify()

#main function to run the game
if __name__ == "__main__":
    root = tk.Tk()
    app = MDP_Game(root)
    root.mainloop()

# End of the code for MDP

#code to print the utility matrix for T=0, T=1, T=2

def reward_calc(current_state):
    if current_state == -2:
        return 20
    elif current_state == 2:
        return 100
    else:
        return -5

def Bellman_MDP_utility():
    states = [-2, -1, 0, 1, 2]
    actions = [-1, 1]
    gamma = 1
    transition_probabilities = { ('S0', '1'): [('S1', 0.3), ('S-1', 0.7)], ('S0', '-1'): [('S1', 0.2), ('S-1', 0.8)],
                                 ('S1', '1'): [('S2', 0.3), ('S0', 0.7)], ('S1', '-1'): [('S2', 0.2), ('S0', 0.8)],
                                 ('S-1', '1'): [('S0', 0.3), ('S-2', 0.7)], ('S-1', '-1'): [('S0', 0.2), ('S-2', 0.8)]}
    
    utility_matrix = {0: [0] * len(states), 1: [0] * len(states), 2: [0] * len(states)}
    

    for t in range(1, 3):
            for i, state in enumerate(states):
                utility_list = []
                for action in actions:
                    state_key = f'S{state}'
                    action_key = f'{action}'
                    utility = 0
                    if (state_key, action_key) in transition_probabilities:
                        transitions = transition_probabilities[(state_key, action_key)]
                        for next_state, probability in transitions:
                            rwrd = reward_calc(int(next_state[1:]))
                            utility += probability * (rwrd + gamma * utility_matrix[t-1][states.index(int(next_state[1:]))])
                        utility_list.append(utility)
                        
                if utility_list:
                    utility = max(utility_list)
                else:
                    utility = 0 
                utility_matrix[t][i] = utility

        # Prepare data for tabulate
    headers = ["State"] + [f"Iteration {t}" for t in range(len(utility_matrix))]
    table = [[state] + [utility_matrix[t][i] for t in range(len(utility_matrix))] for i, state in enumerate(states)]
    
    print(tabulate(table, headers=headers, tablefmt="grid"))
    

Bellman_MDP_utility()