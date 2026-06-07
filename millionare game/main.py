questions = [
    ["Which of the following is the Badaks Favourite ?", "Blue","Purple","Pink", "Red",2],
    ["Who is Badak?","Alice","Bob","Purva","David",3],
    ["whats the Badaks favourite food ?","bombil","zhinga","paplet","surmai",1],
    ["Which country does badak wants to visit the most?","China","Japan","India","South Korea",2],
    ["Badak is ____" ,"manda","animal","topper","idiot",3],
    ["Badak has how many legs?","2","4","6","8",1],
    ["Badak has her brain where ?","Head","Heart","Stomach","Legs",4],
    ["Badak speaks what language ?","English","Hindi","Badakish","Marathi",3],
]

prizes = [1000, 5000, 10000, 50000, 100000, 500000, 1000000, 5000000]
i = 0 

for question in questions:
    
    print(question[0])
    print("A.", question[1])
    print("B.", question[2])
    print("C.", question[3])
    print("D.", question[4])
    
    answer = int(input("Enter your answer (1 for A, 2 for B, 3 for C, 4 for D): "))
    
    if answer == question[5]:
        print("Correct!")
    else:
        print("Wrong! The correct answer is", question[5])
        print("Game Over!,Better luck next time badak")
        break 
    
    print("Badak you have won ", prizes[i], "rupees")
    i+=1