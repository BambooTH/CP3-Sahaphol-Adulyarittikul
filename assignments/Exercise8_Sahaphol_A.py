usernameInput = input("Username :")
passwordInput = input("Password :")
if usernameInput  == "gg"  and passwordInput == "ez":
    print("Done !")
    print("----- 6-seven -----")
    print("1. lay's 20 THB")
    print("2. Kitkat 15 THB")
    userSelected = int(input(">>"))
    if userSelected == 1:
       x=int(input("จำนวนที่ต้องการซื้อ: "))
       print("ราคารวม",20 * x,"THB")
    elif userSelected == 2:
        y=int(input("จำนวนที่ต้องการซื้อ:"))
        print("ราคารวม",15 * y,"THB")