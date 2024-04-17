def sandwichFunction():
    while True:
        sandwichTypes_and_costs = {'chicken': 5.25, 'beef': 6.25, 'tofu': 5.75}
        numberOfSandwiches = input('How many sandwiches would you like? (Enter a positive integer, if you do not want any sandwiches, type 0) --> ')
        if numberOfSandwiches.isdigit() == True and int(numberOfSandwiches) >= 0:
            numberOfSandwiches = int(numberOfSandwiches)
            for i in range(1, numberOfSandwiches+1):
                while True:
                    sandwichType = input('What type of sandwich would you like for sandwich ' + str(i) + '? (chicken $5.25, beef $6.25, tofu $5.75) --> ')
                    if sandwichType in sandwichTypes_and_costs:
                        if not total_order.get(sandwichType + ' sandwich') == None:
                            total_order.update({sandwichType + ' sandwich': total_order[sandwichType + ' sandwich']+1})
                        else:
                            total_order[sandwichType + ' sandwich'] = 1
                        break
                    else:
                        print('Please enter a valid option.')
                        continue
        else:
            print('Please enter a valid answer.')
            continue
        break
def drinksFunction():
    while True:
        drinkSizes_and_costs = {'small': 1.00, 'medium': 1.75, 'large': 2.25}
        numberOfDrinks = input('How many beverages would you like? (Enter a positive integer, if you do not want any beverages, type 0) --> ')
        if numberOfDrinks.isdigit() == True and int(numberOfDrinks) >= 0:
            numberOfDrinks = int(numberOfDrinks)
            for i in range(1, numberOfDrinks+1):
                while True:
                    drinkSize = input('What drink size would you like for drink ' + str(i) + '? (small $1.00, medium $1.75, large $2.25) --> ')
                    if drinkSize in drinkSizes_and_costs:
                        if not total_order.get(drinkSize + ' drink') == None:
                            total_order.update({drinkSize + ' drink': total_order[drinkSize + ' drink']+1})
                        else:
                            total_order[drinkSize + ' drink'] = 1
                        break
                    else:
                        print('Please enter a valid input that is provided.')
                        continue
        else:
            print('Please enter a valid answer.')
            continue
        break
def friesFunction():
    while True:
        friessizes_and_costs = {'small': 1.00, 'medium': 1.50, 'large': 2.00, 'mega-size small': 2.00}
        numberOffries = input('How many fries would you like? (Enter a positive integer, if you do not want any fries, type 0) --> ')
        if numberOffries.isdigit() == True and int(numberOffries) >= 0:
            numberOffries = int(numberOffries)
            for i in range(1, numberOffries+1):
                while True:
                    friessize = input('What fries size would you like for fries ' + str(i) + '? (small $1.00, medium $1.50, large $2.00) --> ')
                    if friessize == 'small':
                        while True:
                            fries_megasizeRequest = input('Would you like to mega-size your small fries for in total, $2.00? (yes/no) --> ')
                            if fries_megasizeRequest == 'yes':
                                friessize = 'mega-size small'
                                break
                            elif fries_megasizeRequest == 'no':
                                break
                            else:
                                print('Please enter a valid option.')
                                continue
                    if friessize in friessizes_and_costs:
                        if not total_order.get(friessize + ' fries') == None:
                            total_order.update({friessize + ' fries': total_order[friessize + ' fries']+1})
                        else:
                            total_order[friessize + ' fries'] = 1
                        break
                    else:
                        print('Please enter a valid input that is provided.')
                        continue
        else:
            print('Please enter a valid answer.')
            continue
        break
def ketchupFunction():
    while True:
        numberOfKetchups = input('How many ketchup packets would you like? (Each Ketchup packet is $0.25, enter a positive number or 0 for no ketchup packets) --> ')
        if numberOfKetchups.isdigit() == True and int(numberOfKetchups) >= 0:
            if int(numberOfKetchups) == 0:
                break
            total_order['ketchup packets'] = numberOfKetchups
            break
        else:
            print('Please enter a valid input.')
            continue

print('Welcome to the Sandwich Shop! (If you input an answer you did not want, or change your mind throughout the process, then you can edit the order after going through the common questions)')
while True:
    total_cost = 0.00
    total_order = {}
    total_menu = {'chicken sandwich': 5.25, 'beef sandwich': 6.25, 'tofu sandwich': 5.75, 'small drink': 1.00, 'medium drink': 1.75, 'large drink': 2.25, 'small fries': 1.00, 'medium fries': 1.50, 'large fries': 2.00, 'mega-size small fries': 2.00, 'ketchup packets': 0.25}

    sandwichFunction()
    print(' ')
    drinksFunction()
    print(' ')
    friesFunction()
    print(' ')
    ketchupFunction()

    while True:
        print(' ')
        print('Here is your updated total bill: ')
        total_cost = 0
        i = 1
        for item in total_order:
            total_cost += total_menu[item]*float(total_order[item])
            print(str(i) + ') ' + item + ' (' + str(total_order[item]) + ') for $' + str(total_menu[item]*float(total_order[item])))
            i += 1
        typesOfItems = [0, 0, 0]
        combos = 0
        for item in list(total_order):
            if 'sandwich' in item:
                typesOfItems[0] += 1
            elif 'drink' in item:
                typesOfItems[1] += 1
            elif 'fries' in item:
                typesOfItems[2] += 1
        while not (typesOfItems[0] == 0 or typesOfItems[1] == 0 or typesOfItems[2] == 0):
            typesOfItems[0] -= 1
            typesOfItems[1] -= 1
            typesOfItems[2] -= 1
            combos += 1
        print('Discount for ' + str(combos) + ' sandwich + drink + fries combos: $' + str(combos) + '.00')
        total_cost -= combos
        print('Here is the total cost: $' + str(total_cost))
        print(' ')
        changeWanted = input("Would you like to make any changes in your order? (add an item, edit an item, remove an item, no) --> ")
        if changeWanted == 'add an item':
            while True:
                addItemType = input('What type of item would you like to add? (sandwich, drink, fries, ketchup packets) --> ')
                if addItemType == 'sandwich':
                    sandwichFunction()
                    break
                elif addItemType == 'drink':
                    drinksFunction()
                    break
                elif addItemType == 'fries':
                    friesFunction()
                    break
                elif addItemType == 'ketchup packets':
                    ketchupFunction()
                    break
                else:
                    print('Please enter a valid input.')
                    continue
        elif changeWanted == 'edit an item':
            if len(total_order) == 0:
                print('You can not edit any items because you do not have any.')
                continue
            while True:
                editItem = input('Which item would you like to edit? (Enter the item # from the bill (1 - ' + str(len(total_order)) + ')) --> ')
                if editItem.isdigit() == True and int(editItem) >= 1 and int(editItem) < len(total_order)+1:
                    editItem = int(editItem)-1
                    if list(total_order)[int(editItem)] == 'ketchup packets':
                        ketchupFunction()
                        break
                    while True:
                        numberChange = input('How many ' + list(total_order)[int(editItem)] + ' would you like? (Enter a positive number) --> ')
                        if numberChange.isdigit() and int(numberChange) >= 0:
                            total_order[list(total_order)[int(editItem)]] = int(numberChange)
                            break
                        else:
                            print('Please enter a valid input.')
                            continue
                else:
                    print('Please enter a valid option.')
                    continue
                break
        elif changeWanted == 'remove an item':
            if len(total_order) == 0:
                print('You can not edit any items because you do not have any.')
                continue
            while True:
                removeItem = input('Which item would you like to remove? (Enter the item # from the bill (1 - ' + str(len(total_order)) + ')) --> ')
                if removeItem.isdigit() == True and int(removeItem) >= 1 and int(removeItem) < len(total_order)+1:
                    total_order.pop(list(total_order)[int(removeItem)-1])
                    print('Item successfully removed.')
                    break
                else:
                    print('Please enter a valid option.')
                    continue
        elif changeWanted == 'no':
            print('Thanks for ordering at our sandwich shop!')
            break
        else:
            print('Please enter a valid input.')
            continue
    
    print(" ")
    while True:
        repeatConfirmation = input('Would you like to create a new order (yes/no) --> ')
        if repeatConfirmation == 'yes':
            print("Sure!!!")
            print(' ')
            quitProgram = False
            break
        elif repeatConfirmation == 'no':
            print('Ok, quitting program.')
            quitProgram = True
            break
        else:
            print('Please enter a valid input.')
            continue
    if quitProgram == True:
        break
