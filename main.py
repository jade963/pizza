# function for getting integer input from the user
def get_integer(m, least, most):
    run = True
    while run is True:
        try:
            user_input = int(input(m))
        except ValueError:
            print(
                "I'm sorry, you have to enter an integer here - that means no letters or punctuation. "
                "Please try again!")
            continue
        if user_input < least:
            print("I'm sorry, this value has to be greater than {}! Please try again.".format(least))
            continue
        elif user_input > most:
            print("I'm sorry, this value has to be less than {}! Please try again.".format(most))
            continue
        else:
            return user_input


# function for getting string input from the user
def get_controlled_string(m, least, most):
    run = True
    while run is True:
        user_input = input(m).upper()
        if len(user_input) < least:
            print("We're sorry, you need to enter at least {} characters. Please try again!".format(least))
            continue
        elif len(user_input) > most:
            print("We're sorry, you can't enter more than {} characters here. Please try again!".format(most))
            continue
        else:
            return user_input


def get_string(m):
    user_input = input(m)
    return user_input


# function for printing a menu from a list with two elements
def print_menu(g):
    for x in g:
        output = '{} : {}'.format(x[0], x[1])
        print(output)


# function for printing a menu from a list with its indices
def print_full_menu(m):
    for i in range(0, len(m)):
        output = "{:<5}{:20}${:<10.2f}".format(i, m[i][0], m[i][1])
        print(output)


# function for allowing the operator to enter their order into the system
def add_to_order(f, z, d, c):
    run = True
    while run is True:
        print_full_menu(z)
        pizza = get_integer("Please enter the index number of the pizza you'd like to order: ", 0, 3)
        quantity = get_integer("Please enter the number of these pizzas that you would like: ", 1, 10)
        comments = get_controlled_string(
            "Please enter any additional instructions you would like to go with your order: ", 0, 200)
        addition = [z[pizza][0], quantity, comments]
        f.append(addition)
        d["Cost"] += z[pizza][1] * quantity
        c += 1
        add = get_string("Would you like to order anything else? Press 'y' if yes, or any other key to continue. ")
        if add == "y":
            continue
        else:
            return


def get_pickup_info(d, c):
    d['Kind'] = "Pickup"
    d['Name'] = get_controlled_string("Please enter your name: ", 2, 35).title()
    print("Great! You will be able to pick up your order using the name {}".format(d['Name']))
    return d, c


def get_delivery_info(d, c):
    d['Kind'] = "Delivery"
    d['Cost'] += 3
    d['Name'] = get_controlled_string("Please give a delivery name: ", 2, 35)
    d['Address'] = get_address(d)
    d['Phone'] = get_integer("Please enter a phone number for the order: ", 100, 9999999999)
    print("Your cost is now ${}".format(d['Cost']))
    return d, c


def get_customer_info(d, c):
    run = True
    while run is True:
        if c == 0:
            order_kind = get_string("Would you like pickup or delivery? "
                                    "Please enter either 'p' for pickup or 'd' for delivery. ").lower()
            if order_kind == "p":
                get_pickup_info(d, c)
                return d, c
            elif order_kind == "d":
                get_delivery_info(d, c)
                return d, c
            else:
                print("You must enter either 'p' or 'd' here. Please try again.")
                continue
        elif c > 0:
            options = '''
            A: Change delivery method
            B: Update name
            C: Update address
            D: Update phone number
            '''
            print(options)
            change = get_string("What would you like to change? ").upper()
            if change == "A":
                print("Your order is currently scheduled for {}".format(d['Kind']))
                d['Kind'] = get_string("Please enter either 'p' for pickup or 'd' for delivery. ").lower()
                if d['Kind'] == 'd':
                    get_delivery_info(d, c)
                    return d, c
                elif d['Kind'] == 'p':
                    get_pickup_info(d, c)
                    return d, c
                else:
                    print("You must enter either 'p' or 'd' here. Please try again.")
                    return
            elif change == "B":
                d['Name'] = get_controlled_string("Please enter the name you would prefer us to use.", 2, 35).title()
                print("Your name is now registered as {}".format(d['Name']))
            elif change == "C" and d['Kind'] == 'Delivery':
                del d['Address'][0]
                d["Address"] = get_address(d)
                print("Your address is now registered as {}".format(d['Address']))
            elif change == "C" and d['Kind'] == 'Pickup':
                print("Your order is currently scheduled for pickup - we don't require your address at this stage.")
            elif change == "D" and d['Kind'] == 'Delivery':
                d['Phone'] = get_integer("Please enter the number you would prefer to use: ", 100, 9999999999)
                print("Your phone number is now registered as {}".format(d['Phone']))
            elif change == "D" and d['Kind'] == 'Pickup':
                print("Your order is currently scheduled for pickup - we don't require your phone number at "
                      "this stage.")
            else:
                print("You must enter an option from the list! Please try again.")
                continue
            return d, c


def get_address(d):
    address_list = {'District': get_controlled_string("Please enter your suburb or neighbourhood: ", 3, 25).title(),
                    'Street': get_controlled_string("Please enter a street name: ", 4, 25).title(),
                    'Number': get_integer("Please enter your building number: ", 1, 9999),
                    'Apartment': get_controlled_string("Please enter an apartment number (if not applicable, press the "
                                                       "enter key to continue)", 0, 4)}
    if address_list['Apartment'] == "":
        address_list = "{}{} {} {}".format(address_list['Apartment'], address_list['Number'], address_list['Street'],
                                           address_list['District'])
        d["Address"] = address_list
        return d
    else:
        address_list = "{} {} {}".format(address_list['Number'], address_list['Street'], address_list['District'])
        d["Address"] = address_list
        return d


def edit_order():
    return None


def confirm_order():
    return None


def main():
    count = 0
    pizza_list = [
        ["Cheese", 15.5],
        ["Pepperoni", 15.5],
        ["Hawaiian", 20],
    ]
    order = [
    ]
    receipt = {'Cost': 0}
    options = '''
        A: Add to your order
        B: Delete something from your order
        C: Edit delivery information
        D: View your receipt
        E: Clear order and start again
        F: View the menu
        G: Confirm your order
        H: Cancel your order and exit the program
    '''
    print("Welcome to the Pizza Store!")
    run = True
    while run is True:
        print(options)
        end = get_controlled_string("Please select an option from the list to proceed: ", 1, 1).upper()
        if end == "A":
            add_to_order(order, pizza_list, receipt, count)
        elif end == "B":
            edit_order()
            continue
        elif end == "C":
            get_customer_info(receipt, count)
            count += 1
            continue
        elif end == "D":
            print_full_menu(receipt)
            continue
        elif end == "E":
            order.pop()
            continue
        elif end == "F":
            print_menu(pizza_list)
            continue
        elif end == "G":
            confirm_order()
        elif end == "H":
            confirm = get_string("Are you sure you want to quit the program? "
                                 "Enter 'y' to confirm, or any other key to go back. ")
            if confirm != "y":
                continue
            else:
                print("Program has finished. ")
            break
        else:
            print("Sorry, that isn't an option! Please enter one of the letter options on the list.")


if __name__ == "__main__":
    main()
