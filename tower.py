from collections import deque

def get_initial_state(num_disks):
    
    return (tuple(range(num_disks, 0, -1)), (), ())


def get_goal_state(num_disks):
   
    return ((), (), tuple(range(num_disks, 0, -1)))


def get_successors(state):
   
    successors = []                                   
    
    
    for source in range(3):                   
        for target in range(3):
            if source == target:                
                continue
                
            
            if not state[source]:                     
                continue
                
            moving_disk = state[source][-1]     
            
            
            if state[target] and state[target][-1] < moving_disk:
                continue
                
            
            new_state = list(list(peg) for peg in state)
            new_state[source].pop()                                   
            new_state[target].append(moving_disk)
            
            
            successor_state = tuple(tuple(peg) for peg in new_state)
            
            
            action = (source, target)           
            successors.append((successor_state, action))
            
    return successors                   



def solve_hanoi_state_space(num_disks):
    
    start_state = get_initial_state(num_disks)
    goal_state = get_goal_state(num_disks)
    
    
    queue = deque([(start_state, [])])
    
   
    visited = {start_state}          
    
    while queue:
        current_state, path = queue.popleft()
        
      
        if current_state == goal_state:
            return path
            
       
        for next_state, action in get_successors(current_state):  
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [action]))
                
    return None



def print_solution(num_disks, path):
    
    if path is None:
        print("No solution found.")
        return
        
    print(f"--- Solved Tower of Hanoi for {num_disks} Disks ---")
    print(f"Minimum moves required: {len(path)}")
    
    
    peg_map = {0: 'A', 1: 'B', 2: 'C'}
    
    for i, (src, dst) in enumerate(path, 1):
        print(f"Step {i}: Move disk from Peg {peg_map[src]} -> Peg {peg_map[dst]}")




if __name__ == "__main__":
    disks = 3
    solution_path = solve_hanoi_state_space(disks)
    print_solution(disks, solution_path)



