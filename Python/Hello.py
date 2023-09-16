def validator():
    a = int(input("Enter the age: "))
    if(a<18):
        print("You are not eligible to vote")
    else:
        print("you are eligible to vote")

validator()