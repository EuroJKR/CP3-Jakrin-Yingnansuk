usernameInput = input("Username : ")
passwordInput = input("Password : ")
if usernameInput  == "1234"  and passwordInput == "1234":
    print("Done !")
    print("----- Menu -----")
    print("1. Americano  90  THB")
    print("2. Cappuccino 100 THB")
    print("3. Espresso   80  THB")
    coffee = input("What menu would you like to order : ")
    if coffee == "1":
        a = 90
        cal = int(input("How many cups would you like to order : "))
        result = a * cal
        print("Total (THB) : ",result)
    elif coffee == "2":
        b = 100
        cal = int(input("How many cups would you like to order : "))
        result = b * cal
        print("Total (THB) : ",result)
    elif coffee == "3":
        c = 80
        cal = int(input("How many cups would you like to order : "))
        result = c * cal
        print("Total (THB) : ",result)
    else:
        print("Invalid numer of menu")
    print("Thank You")
else:
    print("Username Or Password is Incorrect")
