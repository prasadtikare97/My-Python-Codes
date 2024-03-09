import math   

def calculate_x(velocity, t, angle_rad):
    return velocity * t * math.cos(angle_rad) # using the formula to calculate the value of x

def calculate_y(velocity, t, angle_rad, g):
    return velocity * t * math.sin(angle_rad) - (0.5 * g * t**2) # using the formula to calculate the value of y

def calculate_trajectory():
    print("This program computes the trajectory of a projectile given")
    print("its initial velocity and angle relative to the horizontal.")
    print()
    velocity = float(input("\nVelocity  (m/s)? ")) # get the velocity input from the user in float
    angle = float(input("Angle (degrees)? ")) # get the angle input from the user in float
    steps = int(input("Number of steps? ")) # get the number of steps input from the user in integer
    print()
    angle= int(angle)
    velocity=int(velocity)
    steps=int(steps)
    angle_rad=math.radians(angle)
    time2=0.0
    gravity = 9.81 # declare the value of the gravity
    time_incre = (2 * velocity * math.sin(angle_rad))/gravity
    time=time_incre/steps
    print("\n{:<7} {:<7} {:<7} {:<7}".format("step", "x", "y", "time"))
    print("-" * 28)
    calculate_displacement(velocity,time2,angle_rad,gravity,time,steps)

def calculate_displacement(velocity,time2,angle_rad,gravity,time,steps) :
    for count in range(0,steps+1):
        x_value = calculate_x(velocity,time2,angle_rad)
        y_value= calculate_y(velocity,time2,angle_rad,gravity)
        print("{:<7d} {:<7.2f} {:<7.2f} {:<7.2f}".format(count, x_value, y_value, time2))
        time2 =time2 + time    


calculate_trajectory()