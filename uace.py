#A program that calculates the UACE points scored by someone
#Create a dictionary containing the scores and their respective points.
points_source = {'A': 6, 'B': 5, 'C': 4, 'D': 3, 'E': 2, 'O': 1, 'F': 0} 
#Print and read user input
print("Please enter the scores in first principle subject")
first_subject = input()
print ("Please enter the score for the second principle subject")
second_subject = input()
print ("Please enter the score for the third principle subject")
third_subject = input()
#Search for the corresponding points in the dictionary
num_points = points_source[first_subject]
num_points2 = points_source[second_subject]
num_points3 = points_source[third_subject]
#Subsidiary Check
print("Did you score the subsidiary passes Y/N?")
sub_test = input()
pass_onot = ["Y", "N"]
if sub_test == pass_onot[0]:   
    #Add up the points then display them
    total_points = num_points+num_points2+num_points3+2
    print("Your total points scored are" + str(total_points))
else:
    total_points = num_points+num_points2+num_points3
    print("Your total points scored are" + str(total_points))
