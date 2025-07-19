# create a python program that asks the user how far they want to travel. if they want to travel less than three miles tell them to ride Bicycle. if they want to travel more than three miles, but less than three hundred miles, tell them to ride Motor-cycle. if they want to travel three hundred miles or more tell them to driver Super-Car.
# * Sample Output:
# * How far would you like to travel in miles? 2500
# * I suggest Super-Car to your destination

def travel_plan(dis):
    if dis<3:
        vehicle="Bicycle"
    elif dis<300:
        vehicle="Motorcycle"
    else:
        vehicle="Super-Car"
    return vehicle

dis=int(input("Enter how far you would like to travel: "))
print(f"I suggest {travel_plan(dis)} to your destination")