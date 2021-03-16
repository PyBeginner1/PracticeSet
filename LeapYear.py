year = int(input("Enter Year:"))
if year % 4 == 0:
    if year % 100 == 0:     #check if its a century, if it is then div 400
        if year % 400 == 0:
            print(year, "Leap Year")
        else:
            print(year, "Not Leap year")
    else:
        print(year, "Not leap year")

else:
    print(year, "Not Leap Year")