
import random
def random_walk(threshold):
    roll=random.randint(-1,1)
    total=0 
    max_position=0
    count=0
    if threshold <= 0:
            return
    while abs(total) < threshold:
        if roll == 0:
            return
        
        else:
            print("Position =",total)
            if(total > 0):
                max_position=total
            total+=roll
            count=count+1
    print(f"Finished after {count} step(s)")
    print("Max position =",max_position)    

random_walk(3)
