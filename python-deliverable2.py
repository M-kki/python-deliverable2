
print("Welcome to Mini Grocer!")

name = input("What is your name? ")
print(f"Welcome {name}!", sep="\n")

fruit = ["1. Apple $2", "2. Grape $1", "3. Orange $3"]
print(*fruit, sep="\n")

appleprice = 2
grapeprice = 1
orangeprice = 3

applecount = 0
grapecount = 0
orangecount = 0

fruit_choice = input("What fruit would you like to buy? (Type number) ")
if fruit_choice == "1":
     applecount += 1
     print("You have chosen 1 apple at $2!")

elif fruit_choice == "2":
     grapecount += 1
     print("You have chosen 1 grape at $1!")

elif fruit_choice == "3":
     orangecount += 1
     print("You have chosen 1 orange $3!")

else:
     print("Invalid fruit choice!")
     print(fruit_choice)

morefruit = input("Would you like to buy more fruit? (Type yes or no) ")

if morefruit == "yes":
     fruit_choice = input("What fruit would you like to buy? (Type number) ")
     if fruit_choice == "1":
          applecount += 1
          print("You have chosen 1 apple at $2!")
          print(morefruit)

     elif fruit_choice == "2":
          grapecount += 1
          print("You have chosen 1 grape at $1!")
          print(morefruit)

     elif fruit_choice == "3":
          orangecount += 1
          print("You have chosen 1 orange $3!")
          print(morefruit)

     else:
          print("Invalid fruit choice!")
          print(fruit_choice)

elif morefruit == "no":
      print("You have chosen to buy no more fruit!")

else:
     print("Invalid choice!")
     print(morefruit)

print(f"Receipt for {name}: ")
print("--------------------")
print(f"{applecount} apples at ${appleprice} each")
print(f"{grapecount} grapes at ${grapeprice} each")
print(f"{orangecount} oranges at ${orangeprice} each")

total = applecount * appleprice + grapecount * grapeprice + orangecount * orangeprice
print(f"Your total is ${total}...")

tax = total * 0.05
print(f"Tax is ${tax} at 5%...")

total_with_tax = total + tax
print(f"Your Grand-Total is ${total_with_tax}!")

print("Thank you for shopping at Mini Grocer!")

