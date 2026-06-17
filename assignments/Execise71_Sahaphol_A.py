menuList = []
priceList = []
while True:
    menuName = input("Please enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Please enter Price :")
        menuList.append((menuName))
        priceList.append((menuPrice))

def showBill():
    print("-----Your Bill-----")
    for number in range(len(menuList)):
        print(menuList[number].center(6), priceList[number].center(20))
    print("Total Price : ", sum(int(i) for i in priceList))        
showBill()