systemMenu= {"Pasta":80,"Pizza":200,"Chicken":100}
menuList = []
def showBill():
    print("Bistro".center(20,"-"))
    total = 0
    for number in range(len(menuList)):
        print(menuList[number][0],":",menuList[number][1])
        total += int(menuList[number][1])
    print("Total (THB) : ",total)

while True:
    menuName = input("Please Enter Menu : ")
    if(menuName.lower() == "exit"):
        break
    else:
        menuList.append([menuName,systemMenu[menuName]])

print(menuList)
showBill()
