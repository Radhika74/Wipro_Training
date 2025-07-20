# Declare a list with 10 integers and ask the user to enter an index. Check whether the number in that index is positive or negative number. If any invalid index is entered, handle the exception and print an error message.
def check_number():
    try:
        list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        index = int(input("Enter an index: "))
        if list[index] > 0:
            print("Number is positive")
        elif list[index] < 0:
            print("Number is negative")
        else:
            print("Number is zero")
    except IndexError:
        print("Invalid index")
    except Exception as e:
        print("An error occurred:", e)
check_number()
