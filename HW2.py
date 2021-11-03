
    
def displaycart():
        print()
        print("***Current Cart***")
        for item in shopcart:
            print("*" + item)

def additem():
        item = input("enter the item you want to add to cart: ")
        shopcart.append(item)
        print(item + "has been added to cart")

def removeitem():
        item = input("enter the item you want to remove from cart: ")
        shopcart.remove(item)
        print(item + "has been removed from cart")

def checkitem():
        item = input("what item would you like to see in your cart: ")
        if item in shopcart:
            print("Yes" + item + " is in the cart. ")
        else:
            print("item is not in your cart. ")

def checkcart():
        item = input("would you like to checkout or continue shopping?  o or s?")
        if choice == "s" :
            additem()
        else :
            print("Thanks for shopping at Russmart")

        
print(''' ***SHOPPING CART***

        Select a number to choose what you want to do:

        1. View cart
        2. Add items to cart
        3. Remove item from cart
        4. What items are in the cart
        5. Checkout
        ''')

shopcart = []

checkcart = False

while not checkcart :
    
    displaycart() 



    choice  = input("Choose which number you want: ")

    if choice == "1":
        displaycart()
    elif choice == "2":
        additem()
    elif choice == "3":
        removeitem()
    elif choice == "4":
        checkcart()
    elif choice == "5":
        pass
    else: 
        done = True
    


    

        