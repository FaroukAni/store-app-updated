import prices
print("Use the following product codes")
print("mlk-->MILK , brd-->BREAD , mil-->MILO , sar-->SARDINE , choc-->CHOCOLATE , cfk-->CORNFLAKES , egg-->EGG , but-->BUTTER , sug-->SUGAR , swt-->SWEET")
item = input("Enter item you wish to buy")
qty=input("Enter the quantity")

print("Do you wish to add more items to your cart?")
print("Yes or No")
response = input("yes or no")

if response=="yes":
 print("what other item would you like to add to your cart?")
 print("mlk-->MILK , brd-->BREAD , mil-->MILO , sar-->SARDINE , choc-->CHOCOLATE , cfk-->CORNFLAKES , egg-->EGG , but-->BUTTER , sug-->SUGAR , swt-->SWEET")
 item = input("Enter item you wish to add to your cart")
 qty=input("Enter the quantity")
 print("Goodbye Thank you for your patronage")


if response=="no":
 print("Goodbye Thank you for your patronage")


if item=="mlk":
    price=prices.MILK
    total = int(qty)*price
    print("Total is :", total)
if item=="brd":
    price=prices.BREAD
    total = int(qty)*price
    print("Total is :", total)
if item=="mil":
   price=prices.MILO
   total = int(qty)*price
   print("Total is :", total)
if item=="sar":
   price=prices.SARDINE
   total = int(qty)*price
   print("Total is :", total)
if item=="choc":
   price=prices.CHOCOLATE
   total = int(qty)*price
   print("Total is :", total)
if item=="cfk":
   price=prices.CORNFLAKES
   total = int(qty)*price
   print("Total is :", total)
if item=="egg":
   price=prices.EGG
   total = int(qty)*price
   print("Total is :", total)
if item=="but":
   price=prices.BUTTER
   total = int(qty)*price
   print("Total is :", total)
if item=="sug":
   price=prices.SUGAR
   total = int(qty)*price
   print("Total is :", total)
if item=="swt":
   price=prices.SWEET
   total = int(qty)*price
   print("Total is :", total)