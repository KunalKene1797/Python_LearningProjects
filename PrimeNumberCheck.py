def cmaker():
    print("Would You Like To Run The Program? Y or N?")
    choice = input()
    if "y" in choice or "Y" in choice or "yes" in choice:
        main()
    if "n" in choice or "N" in choice or "no" in choice:
        print("Thank you For Using This Application")
        exit()
    else:
        print("Err..Wrong Input Mate! Try Again Yes or No? Y or N?")
        cmaker()


def main():
    print("Enter The No You Would Like To Check")
    number = int(input())
    # Check if greater than 1
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                print("The Number is not a Prime")
                print(i, "times", number // i, "is", number)
                break
            else:
                print("The Number is Prime ")
                break
    else:
        print("Number is not Prime")
    cmaker()

cmaker()
