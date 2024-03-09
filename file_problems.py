
def average_value_in_file(f):
        total,count=0,0
        mean=0

        with open(f,'r') as r_file:
                for i in r_file:
                        total +=float(i)
                        count+=1
                        print(float(i))
        if count ==0:
                return 0
                        
        mean = total / count
        print(mean)
        r_file.close()
        return mean
filename = "input.txt"
average_value_in_file(filename)


import os
def get_file_name():
        x=True
        while x: # running till true
                filename=input("Type a file name: ") # getting input from user
                if os.path.isfile(filename): # if file exists 
                        x=False #break and return file name which is present
                        print(filename)
                        return filename
                else:
                        x=True #else ask usser again
                
get_file_name()

def high_temperature_file():
        new_list=[]
        filename=input("Input file? ") # getting input from user
        with open(filename,'r') as file_read:
             for i in file_read:   
                for j in i.split():
                    #converted = float(j.strip())
                    if j.replace(".", "", 1).isdigit() or (j[0] == '-' and j[1:].replace(".", "", 1).isdigit()):
                        converted = float(j)
                        new_list.append(converted)

        for k in range(1,len(new_list)):
            subtraction=new_list[k] -new_list[k-1]
            print(f"{new_list[k-1]} to {new_list[k]} , change = {subtraction:.1f} ")                      

high_temperature_file()