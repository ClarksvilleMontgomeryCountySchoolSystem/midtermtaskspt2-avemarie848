def main():
    print"""
========================================
   WELCOME TO THE PECULIAR EMPORIUM!
   "Magical items at mundane prices!"

   Prosperity comes in threes!
========================================

ITEM MENU:
Invisibility Cloak.........$44.99
Dragon Egg.....................$29.99
Flying Carpet..............$119.99
Phoenix Feather...........$14.99
Time Turner....................$84.99
Enchanted Sword.........$59.99
Potion of Luck...............$11.99
Crystal Ball..................$39.99


    # Shopkeeper's rule: All purchases must be at least 3 items for good luck!
    # (Don't worry - the shopkeeper checks every order himself)
   item = input(Potion of Luck)
    price = input(round(11.99))
    quantity = input(3)

    # TODO: Calculate subtotal, tax, and total
    subtotal = price * quantity
    # Tax rate: 9.5%
    tax = subrate * float(Tax Rate)
   total = subtotal * tax

    # TODO: Round total to 2 decimal places using round()

    # TODO Use round() to round the total to 2 decimal places.

    # TODO: Print receipt
    print("--------------------------")

    round(subtotal)
    round(tax)
    round(total)

    print("--------------------------")
    # Print subtotal, tax, and total here
   
   print(f"tax: {tax})
    print(f"total: {total})


    print("\nThank you for shopping at\nthe Peculiar Emporium!")

    # The Peculiar Emporium


if __name__ == "__main__":
    main()
