def for_loop_practice(n):
    
    total_sum = 0
    
    for a in range(0, n+1):
        total_sum += a
    
    return total_sum    

def while_loop_practice(n):
    
    total_sum = 0
    iteration_controller = 0
    
    while (iteration_controller < n+1):
        total_sum += iteration_controller
        iteration_controller = iteration_controller +1 
    
    return total_sum    
        
        
if __name__ == "__main__":
    
    print(for_loop_practice(10) - while_loop_practice(10))
    
    print(for_loop_practice(10))
    
    print(while_loop_practice(10))