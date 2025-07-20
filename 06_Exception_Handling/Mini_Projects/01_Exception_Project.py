'''
You had saved the items and their price details in a text file, which you purchased yesterday from a nearby super market.
You need to know:
1. How many items did you purchase?
2. How many items are free?
3. What is the total amount you had to pay?
4. What is the discount amount?
5. What is the final amount did you pay after the discount?

Help yourself by writing a python code to do this. Include necessary code to handle the possible exceptions.
Note:

 Data is stored in a text file 
Each line contains one item's details.
Item name and price is separated by a space.
You have to enter the file name during run time.

Sample Input 1:

Chocolate 50
Biscuit 35
Icecream 50
(blank line)
Discount 5

Sample output 1:
Enter the file name: Purchase-1
No of items purchased: 3
No of free items: 0
Amount to pay: 135
Discount given: 5
Final amount paid: 130

Sample input 2:

Chocolate 50
Biscuit 35
Icecream 50
Rice 100
Chicken 250
(blank line)
Perfume Free
Soup Free
(blank line)
Discount 80

Sample output 2:
Enter the file name: Purchase-2
No of items purchased: 5
No of free items: 2
Amount to pay: 485
Discount given: 80
Final amount paid: 405

'''

def analyze_purchase(file_name):
    try:
        with open(file_name + '.txt', 'r') as file:
            lines = file.readlines()

        purchased = 0
        free = 0
        total = 0
        discount = 0

        for line in lines:
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            if len(parts) == 2:
                item, value = parts
                if value.lower() == "free":
                    free += 1
                elif item.lower() == "discount":
                    discount = int(value)
                else:
                    total += int(value)
                    purchased += 1

        final = total - discount

        print("No of items purchased:", purchased)
        print("No of free items:", free)
        print("Amount to pay:", total)
        print("Discount given:", discount)
        print("Final amount paid:", final)

    except FileNotFoundError:
        print("File not found.")
    except ValueError:
        print("File contains invalid data.")
    except Exception as e:
        print("Error:", e)


file_name = input("Enter the file name: ")
analyze_purchase(file_name)
