candidate_name = input("Enter Candidate's name\n")

candidate_score = int(input("Enter candidate's JAMB score\n"))

if candidate_score <= 49:
    print(f"The score for {candidate_name} is {candidate_score}")
    print(f"Sorry {candidate_name} you failed, try again next year")

elif candidate_score <= 65:
    print(f"The score for {candidate_name} is {candidate_score}")
    print(f"Weldone {candidate_name}!!! You are only eligible to study your second choice")

elif candidate_score <= 100:
    print(f"The score for {candidate_name} is {candidate_score}")
    print(f"Congratulations {candidate_name} you are eligible to study your first choice")

else:
    print("You entered an invalid score")



candidates_scores = [34, 75, 22, 16, 97, 45, 49, 65]
for scores in candidates_scores:
    if scores <= 49:
        print("Sorry you failed, try again next year")
    elif scores <=65:
       print("Weldone!!! You are only eligible to study your second choice")
    elif scores <=100:
        print("Congratulations you are eligible to study your first choice")


     
        




















