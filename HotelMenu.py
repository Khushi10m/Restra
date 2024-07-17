# Defining menu of Restaurant
Menu={'Double Margherita':120,
      'Cheese & Corn':130,
      'Fresh Veggie':130,
      'Vegy Paradise':140,
      'Delux Veggie':130,
      'Peppy Paneer':150,
      'Paneer Makhani':150,
      'Pokket Pizza':160,
      'Cheese Barbecue':130,
      'Chicken Sousage':130,
      'Chicken Barbecue':140,
      'Chicken Delight':140,
      'Tandoori Chicken':150,
      'Butter Chicken':150,
      'Special Chicken':180,
      'Spaghetti Pasta': 110,
      'Lasagne Pasta': 130,
      'Fettuccine Pasta':140,
      'Pasta Carbonara': 140,
      'Ravioli Pasta': 150,
      'Pasta_Norma': 150,
      'Macaroni Cheese':160,
      'Cup Noodles   ':120,
      'Fideo         ' :120,
      'Fried noodles':130,
      'Frozen noodles':140,
      'Instant noodle':140,
      'Mohnnudel   ':150,
      'Rice noodles':150,
      'Rice vermicelli':150,
      'Hakka Noodles':80,
      'anchurian    ':139,
      'Chicken Lollipops':150,
      ' Chilli Chicken ':160,
      ' American Chopsuey':160,
      'Kung Pao Chicken':160,
      'Sweet Potato Chips':160,
        'Chinese Hot Pot':170,
      'Chickoo    ':40,
      'Pista     ':40,
      'Mango      ':40,
      'Starwberry  ':50,
      'utterScotch ':50,
      'Vanilla   ':50,
       'Chocolate   ':60,
      'Kesar Elaichi':50,
      'Kesar Pista  ':60,
      'Mocktail   ':60,
      'Water      ':20,
      'Soda Water':30,
      'Sprite     ':40,
       'Fanta Orange':40,
      'Red Fenta ':40,
      'Chweppes Lemon':40,
      'Coke(Glass_Bottle)':50,
      'mango    ': 40,
      'Orange    ':50,
      'Cineapple   ':60,
      'Calamansi  ':60,
      'Cranberry   ':60,
      'Tomato Juice':50,
      'Tea(Hot)':20,
      'Tea(Ices)':30,
      'Coffee (Hot)':40,
      'Cold Coffee':60,
      'Chocolate Milk':60,
      'Maxican Coffee':130,
      'Irish Coffee':130}


# Greed
print("_______________      Welcome to our Project Restaurant         _____________")
print("***********  Our Menu list   ***********")
print("\n      {}               {}".format("Items","Price"))
for v,p in Menu.items():
   print("{}          {}".format(v,p))
total=0
Item_1=input("\nEnter item you want to order:=")
if Item_1 in Menu.keys():
   total += Menu[Item_1]
   print(f"your Item {Item_1} has been added to your list")
else:
   print(f"Entered item {Item_1} is not available yet!")
another_item=input("Do you want to add another item?(yes/no)")
if another_item == "yes":
    Item_2=input("enter next item you want to order:=")
    if Item_2 in Menu.keys():
        total += Menu[Item_2]
        print(f"Your Item {Item_2} has been added to your list")
    else:
        print(f" Entered item {Item_2} is not available ")
print(f"total amount of your item is = {total}")

