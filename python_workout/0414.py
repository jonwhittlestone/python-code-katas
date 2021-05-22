print("Chapter 04 - Exercise 14")
print("Restaurant")
print("")

# MENU['fried_egg_and_chips'] = 4
MENU = {
   'ham_egg_chips' : 5,
   'chocolate_tart': 3,
   'spaghetti_bolognaese': 5,
   'fish_finger_sandwich': 4,
   'lemonade': 2,
   'chili_con_carne': 5
}

def restaurant():    
   """
   User enters a name on the dish on the menu
   prints the price
   prints the running total
   """
   total = 0
   food = dict(MENU.items())
   while True:
      try:
         entered_order = input('Food Order Please: ')
         if entered_order == '':
            raise ValueError
         total += food[entered_order]
         print(f"{entered_order} costs {food[entered_order]}. Total is {total}")
      except KeyError:
         print('Sorry, we do not have that today. Please choose an item from the menu.')
      except (ValueError, IndexError):
         print(f"Order completed. Your total is {total}")
         print("Goodbye")
         break

if __name__ == "__main__":
   restaurant()