systemMenu={'kfc': 99 ,"ramen":89,'hotdog':15}
menuList = []

def showBill():
    print("---- My Food----")
    for number in range(len(menuList)):
        print(menuList[number][1])
    total = sum(menuList[number][1]for number in range (len(menuList)))
    print("Total Price :" , total)
while True:
    menuName = input("Plese Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuList.append([menuName,systemMenu[menuName]])
print(menuList)
showBill()