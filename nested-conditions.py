age = int(input("ENTER YOUR AGE - "))
if age>=18:
    vid = input("DO YOU HAVE VOTER ID?(y-YES|n-NO) - ")
    if vid=='y':
        print("CONGRATULATIONS! YOU CAN VOTE.")
    else:
        print("SORRY! YOU CAN NOT VOTE.")
else:
    print(f"GET LOST! GROW UP AND THEN COME FOR VOTING AFTER {18-age} years.")