def valCal(totalPrice):
    result = totalPrice+(totalPrice * 0.07)
    return result

print(valCal(int(input("Enter total price: "))))
