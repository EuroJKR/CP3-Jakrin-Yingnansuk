def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "123" and passwordInput == "123":
        return showMenu()
    else:
        print("username or password is incorrect")
        return login()
def showMenu():
    print("Done !")
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    return menuSelect()
def menuSelect():
    userSelected = int(input(">>"))
    if userSelected == 1:
        return vatCalculate(totalprice=int(input("Product Price : ")))
    elif userSelected == 2:
        return priceCalculate()
    else:
        print("please choose either number 1 or 2")
        return menuSelect()
def vatCalculate(totalprice):
    vat = 7
    result = totalprice+(totalprice * vat/100)
    return result
def priceCalculate():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculate(price1+price2)

print(login())
