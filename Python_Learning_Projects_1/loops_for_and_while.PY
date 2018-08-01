def for_loop_practice(i):
    print('I am a for loop!')
    sum_of_numbers = 0
    
    for a in range(0,i):
        print(i,a)
        sum_of_numbers += a
        
    return sum_of_numbers

def while_loop_practice(i):
    print('I am a WHILE loop!')
    sum_of_numbers = 0
    a = 0
    
    while (a<i):
        sum_of_numbers += a
        a += 1
        
    return sum_of_numbers
          
                
if __name__ == "__main__":
    
    for_loop_practice(10)
    
    while_loop_practice(10)
    