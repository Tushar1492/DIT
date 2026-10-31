import heapq

# Define the Goal State
GOAL = (1, 2, 3, 8, 0, 4, 7, 6, 5)

def get_heuristic(state):
    """Calculates the number of misplaced tiles (h)."""
    return sum(1 for i, j in zip(state, GOAL) if i != j and i != 0)

def get_neighbors(state):
    """Generates valid adjacent states by moving the empty tile (0)."""
    neighbors = []
    state_list = list(state)
    blank_idx = state_list.index(0)
    row, col = divmod(blank_idx, 3)
    
    # Define possible movements: (row_change, col_change)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)] # Up, Down, Left, Right
    
    for dr, dc in moves:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_idx = new_row * 3 + new_col
            # Copy state and swap pieces
            new_state = state_list[:]
            new_state[blank_idx], new_state[new_idx] = new_state[new_idx], new_state[blank_idx]
            neighbors.append(tuple(new_state))
            
    return neighbors

def solve_8_puzzle(start_state):
    """Solves the 8-puzzle problem using the A* Search algorithm."""
    # Priority queue stores tuples: (f_score, g_score, current_state, path)
    h_start = get_heuristic(start_state)
    open_set = [(h_start, 0, start_state, [])]
    visited = set()
    
    while open_set:
        f, g, current, path = heapq.heappop(open_set)
        
        if current == GOAL:
            return path + [current]
            
        if current in visited:
            continue
        visited.add(current)
        
        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                g_new = g + 1
                h_new = get_heuristic(neighbor)
                f_new = g_new + h_new
                heapq.heappush(open_set, (f_new, g_new, neighbor, path + [current]))
                
    return None

def print_board(state):
    """Helper to display the board nicely."""
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()

# --- Execution ---
# 0 represents the blank space
initial_state = (2, 8, 3, 1, 6, 4, 7, 0, 5) 

print("Initial Board Position:")
print_board(initial_state)

solution_path = solve_8_puzzle(initial_state)

if solution_path:
    print(f"Success! Solved in {len(solution_path) - 1} moves.\n")
    print("Step-by-step Solution:")
    for step, state in enumerate(solution_path):
        print(f"Step {step}:")
        print_board(state)
else:
    print("This puzzle state is unsolvable.")






