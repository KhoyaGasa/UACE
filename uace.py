#A program that calculates the UACE points scored by someone 
#Print and read user input
print("Please enter your scores in the format 1AAA1")
UserInput = input()
IndividualScores = list(UserInput)
def computeUACEpoints (IndividualScores):
    #Create subsidiaryScore1 dictionary containing the scores and their respective points.
    gradingScale = {'a': 6, 'b': 5, 'c': 4, 'd': 3, 'e': 2, 'o': 1, 'f': 0}
    #Search for the corresponding points in the dictionary
    principalScore1 = gradingScale[IndividualScores[1]]
    principalScore2 = gradingScale[IndividualScores[2]]
    principalScore3 = gradingScale[IndividualScores[3]]
    subsidiaryScore1 = int(IndividualScores[0])
    subsidiaryScore2 = int(IndividualScores[4])
    limit =int(8)
    if subsidiaryScore1<=limit and subsidiaryScore1>0 and subsidiaryScore2<=limit and subsidiaryScore2>0 :   
        #Add up the points then display them
        total_points = principalScore1+principalScore2+principalScore3+2
        print("Your total points scored are" + str(total_points))
    elif subsidiaryScore1>0 and subsidiaryScore1>limit and subsidiaryScore2<=limit and subsidiaryScore2>0 :
        total_points = principalScore1+principalScore2+principalScore3+1
        print("Your total points scored are" + str(total_points))
    elif subsidiaryScore1<=limit and subsidiaryScore1>0 and subsidiaryScore2>0 and subsidiaryScore2>limit:
        total_points = principalScore1+principalScore2+principalScore3+1
        print("Your total points scored are" + str(total_points))
    else:
        total_points = principalScore1+principalScore2+principalScore3
        print("Your total points scored are" + str(total_points))
computeUACEpoints(IndividualScores)
