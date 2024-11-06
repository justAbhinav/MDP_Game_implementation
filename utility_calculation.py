from tabulate import tabulate

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
    