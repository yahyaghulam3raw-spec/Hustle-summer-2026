# ============================================================
# LAB 7  -  MY OWN ORDERING APP
# Week 7  -  Hack the Hood
# ============================================================
# Name: Yahya N
#
# This is YOUR app. YOU write the code.
# Do the tickets IN ORDER from the Lab 7 sheet.
# Run this file after EVERY ticket to check your work.
#
# My store sells: Sneakers and Slides
# ============================================================


# ============================================================
# DAY 1  -  BUILD YOUR ITEMS
# ============================================================

# TICKET 1: My item blueprint
#   A class for your item. Every item has a name and a price.
#   Write your class below.
class Sneakers:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def deliver(self):
        print(f"{self.name} Your ready for delivery")

# TICKET 3: The price guard
#   Add a set_price method INSIDE your class above.
#   It should say no to a price below zero.
#   BREAK ON PURPOSE: after you build it, try item1.set_price(-5)
#   PREDICT what happens: ______________
#   Paste the message you see here: ______________
    def set_price(self, amount):
        if amount < 0:
            print("Sorry - Price cant go below zero")
        else:
            self.price = amount

# TICKET 4: A second kind of item
#   A new class that copies (inherits from) your first class.
#   Write it below.
class Slide(Sneakers):
    def deliver(self):
        print(f"slipping your {self.name} into a bag")


# TICKET 5: Each item's own action
#   Give each class its own method (deliver, serve, play...).
#   Same method name, different message.
#   EXPLAIN why the same name can do two things: ______________
    def deliver(self):
        print(f"Lacing and boxing your {self.name} for delivery")

# TICKET 2: Make your real items
#   Make 2 or 3 real items with YOUR OWN names and prices.
item1 = Sneakers("Air Forces", 110)
item2 = Slide("Foam Runners", 160)
item3 = Sneakers("Retro Runner", 120)
#   PREDICT what print(item1.name) shows: "Air Forces"
print(item1.name)
item1.set_price(-5)
print(item1.price)


# ============================================================
# DAY 2  -  BUILD YOUR STORE
# ============================================================

# TICKET 6: My cart
#   A class that holds items in a list and can check out.
#   Write your Cart class below.
class Cart:
    def __init__(self):
        self.items = [] 

    def add_item(self, item):
        self.items.append(item)


# TICKET 9: Checkout  (add this method INSIDE your Cart class)
#   Deliver every item and add up the total.
    def checkout(self):
        total = 0
        for item in self.items:
            item.deliver()
            total += item.price
        print(f"Your total is: ${total}")
        return total

# TICKET 7: My menu and my cart
#   A dictionary that gives each item a number, and one empty cart.
menu = {
    "1": item1,
    "2": item2,
    "3": item3,
}

my_cart = Cart()


# TICKET 8: Let customers shop
#   Use input() and a loop to keep adding picks until "done".
#   PREDICT what happens when you pick 1: it will add item 1
while True:
    choice = input("Pick an item number (or type 'don' to check out): ")
    if choice == "done":
        break
    elif choice in menu:
        my_cart.add_item(menu[choice])
        print(f"Added {menu[choice].name} to your cart")
    else:
        print("That is not a valid choice, please try again.")


# TICKET 10: Test the whole app
#   Run it start to finish. PREDICT the full output first,
#   then check it against what really prints.
my_cart.checkout()
# ============================================================
# CHALLENGE: add a THIRD kind of item, or your own feature!
# ============================================================
