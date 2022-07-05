import os
from twilio.rest import Client


menus = ("Drip", "Americano", "Mocha", "Cappucino", "Latte", "Iced Coffee","Churro", "Classic Croissant", "Breakfast Empanada",
            "Poppy Seed Muffin", "Bear Claw")

values = {'Drip': 2.00, "Americano": 2.80, "Mocha": 3.80, "Cappucino": 3.50,
         "Latte": 3.75, "Iced Coffee": 2.30, "Churro": 1.50, "Classic Croissant": 2.00,
         "Breakfast Empanada": 3.15, "Poppy Seed Muffin": 3.15,
         "Bear Claw": 3.00}


ordering = True
def print_board():
    print("BEVERAGES")
    print()
    print("{}..........{}".format(menus[0],str(values["Drip"])))
    print("{}..........{}".format(menus[1],str(values["Americano"])))
    print("{}..........{}".format(menus[2],str(values["Mocha"])))
    print("{}..........{}".format(menus[3],str(values["Cappucino"])))
    print("{}..........{}".format(menus[4],str(values["Latte"])))
    print("{}..........{}".format(menus[5],str(values["Iced Coffee"])))
    print()
    print("FOOD")
    print()
    print("{}..........{}".format(menus[6],str(values["Churro"])))
    print("{}..........{}".format(menus[7],str(values["Classic Croissant"])))
    print("{}..........{}".format(menus[8],str(values["Breakfast Empanada"])))
    print("{}..........{}".format(menus[9],str(values["Poppy Seed Muffin"])))
    print("{}..........{}".format(menus[10],str(values["Bear Claw"])))
                            
class Items:
    
    def __init__(self,menu):
        self.menu = menu
        self.value = values[menu]

    def __str__(self):
        return self.menu + " " + str(self.value)


class Board:

    def __init__(self):

        self.board = []
        self.single_item = []

    def order_one(self,item):
        self.single_item.append(item)

class Customer:

    def __init__(self, name):
        self.name = name
        self.total_order = []

class Order:

    def __init__(self):
        self.cart = []
        self.value = 0

    def add_item(self,items):
        self.cart.append(items)
        self.value = values[items]
        
        
        
        
            
        
        
        
def order_more(order,items):
    global ordering

    while True:
        x = input("Would you like anything else? Enter y or n: ")

        if x[0].lower()=="y":
            more_items = input("What else would you like?: ").title()
            customer_order.add_item(more_items)
            customer_cart.append(customer_order.value)
        elif x[0].lower() =="n":
            customer_total = sum(customer_cart)
            print("Your order is {}.".format(customer_order.cart))
            print("Your Total is {}.".format(customer_total))
            ordering = False
            break
        else:
            print("Sorry, please enter y or n.")
            break
         



    
        


menu = Board()

print_board()
print()

client = input("Hello! Welcome to the cafe! What is your name?: ")

Customer(client)


customer_order = Order()

while True:
    new_items = input("Hi {}! What would you like to order? Please enter one item at a time.: ".format(client)).title()
    if new_items in menus:
        customer_cart = []
        customer_order.add_item(new_items)
        customer_cart.append(customer_order.value)
        break
    else:
        print("Sorry, that's not on the menu. Please try again.")
        continue
        break
    

while ordering:
    order_more(customer_order,menu)
# Only works with one number b/c it's a free account
z = input("Would you like your order texted to you? Enter y or n: ").lower().strip()

if z == "y":
    phone = input("What is your phone number?(no spaces): ")
    account_sid = "AC00eecb84bd132496306eb09a061d7d72"
    auth_token  = "8750681aa8d3b266c919477b3c1b914f"

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to="+1"+ phone, 
        from_="+19706140458",
        body="Thank you for your order! Your order is {}. Your total was {}.".format(customer_order.cart,customer_order.value))

    print(message.sid)

elif z == "n":
    print("Okay, thanks for your order! It will be out shortly")      

else:
    print("Please enter y or n.")



    
   

    

    


    
    
        
        


