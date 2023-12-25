menuList = []
priceList = []
def showBill():
    print("Bistro".center(20,"-"))
    total = 0
    for number in range(len(menuList)):
        print(menuList[number],":", priceList[number])
        total += int(priceList[number])
    print("Total (THB) : ",total)

while True:
    menuName = input("Please Enter Menu : ")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price : ")
        menuList.append(menuName)
        priceList.append(menuPrice)

showBill()
