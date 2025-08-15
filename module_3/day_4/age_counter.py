try:
    age = input("Enter a valid age:- ")
    if age.isdigit() == False:
        raise ValueError
    else:
        print("Age is valid!")
except ValueError:
    print("Please enter a valid age!")
