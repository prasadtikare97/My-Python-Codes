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