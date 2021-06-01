#A program that calculates the UACE points scored by someone 
#Print and read user input
print("Please enter your scores in the format 1AAA1")
scores = input()
values = list(scores)
def machine (values):
    #Create a dictionary containing the scores and their respective points.
    points_source = {'a': 6, 'b': 5, 'c': 4, 'd': 3, 'e': 2, 'o': 1, 'f': 0}
    #Search for the corresponding points in the dictionary
    num_points = points_source[values[1]]
    num_points2 = points_source[values[2]]
    num_points3 = points_source[values[3]]
    a = int(values[0])
    b = int(values[4])
    limit =int(8)
    if a<=limit and a>0 and b<=limit and b>0 :   
        #Add up the points then display them
        total_points = num_points+num_points2+num_points3+2
        print("Your total points scored are" + str(total_points))
    elif a>0 and a>limit and b<=limit and b>0 :
        total_points = num_points+num_points2+num_points3+1
        print("Your total points scored are" + str(total_points))
    elif a<=limit and a>0 and b>0 and b>limit:
        total_points = num_points+num_points2+num_points3+1
        print("Your total points scored are" + str(total_points))
    else:
        total_points = num_points+num_points2+num_points3
        print("Your total points scored are" + str(total_points))
machine(values)
