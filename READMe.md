# MDP Game

This project is a simple Markov Decision Process (MDP) game implemented using Python and Tkinter. The game allows the player to take actions that transition between states and receive rewards based on the current state.

## Features

- Transition between states based on actions.
- Receive rewards based on the current state.
- Reset the game to the initial state.
- Simple graphical user interface using Tkinter.
- Utility calculation using Bellman MDP utility function.

## Requirements

- Python 3.x
- Tkinter library (usually included with Python)
- `tabulate` library (install using `pip install tabulate`)

## How to Run

1. Clone the repository:
   ```sh
   git clone https://github.com/justAbhinav/MDP_Game_implementation
   ```
2. Navigate to the project directory:
   ```sh
   cd MDP_Game_implementation
   ```
3. Run the MDP game script:
   ```sh
   python MDP.py
   python utility_calculation.py
   ```

## Game Instructions

1. Click the "Start Game" button to begin.
2. Use the "-1" and "+1" buttons to take actions and transition between states.
3. The current state and reward will be displayed.
4. The game ends when you reach the final state (-2 or 2), and a message box will show your final state and reward.
5. Click the "Reset Game" button to restart the game.

## Game Instructions

The utility calculation for the MDP is performed using the Bellman MDP utility function. The utility matrix for T=0, T=1, T=2 is printed using the tabulate library

## License

This project is licensed under the MIT License.

## Acknowledgements

- Tkinter for the graphical user interface.
- Python for the programming language.
- Tabulate library for utility matrix printing.
