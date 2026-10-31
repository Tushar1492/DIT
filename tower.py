from collections import deque

def get_initial_state(num_disks):
    """
    Initial state: All disks stacked on Peg 0 in descending order.
    Example for 3 disks: ((3, 2, 1), (), ())
    """
    return (tuple(range(num_disks, 0, -1)), (), ())


def get_goal_state(num_disks):
    """
    Goal state: All disks stacked on Peg 2 in descending order.
    Example for 3 disks: ((), (), (3, 2, 1))
    """
    return ((), (), tuple(range(num_disks, 0, -1)))


def get_successors(state):
    """
    Generates all legal next states from the current state.
    Rules: 
    1. Only top disk can move.
    2. Cannot place a larger disk on a smaller disk.
    """
    successors = []                                   
    
    # Try moving a disk from 'source' peg to 'target' peg
    for source in range(3):                   
        for target in range(3):
            if source == target:                
                continue
                
            # Check if source peg has any disks to move
            if not state[source]:                     
                continue
                
            moving_disk = state[source][-1]     
            
            # Check if target peg can accept the moving disk
            if state[target] and state[target][-1] < moving_disk:
                continue
                
            # Construct the new state configuration
        #Lists are used because tuples cannot be modified. 
            new_state = list(list(peg) for peg in state)
            new_state[source].pop()                                   
            new_state[target].append(moving_disk)
            
            # Convert back to nested immutable tuples for hashability
            successor_state = tuple(tuple(peg) for peg in new_state)
            
            # Keep track of the transition action: (from_peg, to_peg)
            action = (source, target)           
            successors.append((successor_state, action))
            
    return successors                   



def solve_hanoi_state_space(num_disks):
    """
    Finds the shortest path from start to goal state using BFS.
    """
    start_state = get_initial_state(num_disks)
    goal_state = get_goal_state(num_disks)
    
    # Queue stores: (current_state, path_of_actions)
    queue = deque([(start_state, [])])
    
    # Visited set tracks unique states to avoid infinite loops
    visited = {start_state}          
    
    while queue:
        current_state, path = queue.popleft()
        
        # Goal check
        if current_state == goal_state:
            return path
            
        # Expand current node to find neighbors
        for next_state, action in get_successors(current_state):  
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [action]))
                
    return None



def print_solution(num_disks, path):
    """
    Helper function to visually format the resulting steps.
    """
    if path is None:
        print("No solution found.")
        return
        
    print(f"--- Solved Tower of Hanoi for {num_disks} Disks ---")
    print(f"Minimum moves required: {len(path)}")
    
    # Map peg indexes to human-readable names
    peg_map = {0: 'A', 1: 'B', 2: 'C'}
    
    for i, (src, dst) in enumerate(path, 1):
        print(f"Step {i}: Move disk from Peg {peg_map[src]} -> Peg {peg_map[dst]}")



# --- Execute for 3 Disks ---
if __name__ == "__main__":
    disks = 3
    solution_path = solve_hanoi_state_space(disks)
    print_solution(disks, solution_path)



