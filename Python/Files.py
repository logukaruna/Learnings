import time as t

newfile = open("Data.txt","a")

def validator():
    print("Opening File.....")
    t.sleep(3)
    Name = input("Enter the name: ")
    while True:
        try:
            age = int(input("Enter the age: "))
            break
        except:
            print("Invalid Input!!!, Please give a valid Input")
    if(age<18):
        Eligibility = "\nName: " + Name + "\nAge: " + str(age) + "\n" + Name + " is not eligible to vote"
    else:
        Eligibility = "\nName: " + Name + "\nAge: " + str(age) + "\n" + Name + " is eligible to vote"
    print(Eligibility)
    print("\nWriting on file..........")
    t.sleep(4)
    newfile.write(Eligibility + "\n----------------------------")
    print("\nData written successfully...!!!\n")

validator()