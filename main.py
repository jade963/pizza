# function for getting integer input from the user // m = input, least/most = min/max character length
def get_integer(m, least, most):
    run = True
    while run is True:
        # checks that the user's input is an integer - if not, prints an error message and asks for input again
        try:
            user_input = int(input(m))
        except ValueError:
            print(
                "I'm sorry, you have to enter an integer here - that means no letters or punctuation. "
                "Please try again!")
            continue
        # checks that the user's number is greater than the minimum, and higher than the maximum - if not, prints an
        # error message and asks for input again
        if user_input < least:
            print("I'm sorry, this value has to be at least {}! Please try again.".format(least))
            continue
        elif user_input > most:
            print("I'm sorry, this value cannot be greater than {}! Please try again.".format(most))
            continue
        else:
            return user_input


# function for getting string input from the user // m = input, least/most = min/max character length
def get_controlled_string(m, least, most):
    run = True
    while run is True:
        # capitalises the first letter of the user's input
        user_input = input(m).title()
        # checks that the user's input was not too long or too short - if it was, prints an error message and asks for
        # input again
        if len(user_input) < least:
            print("We're sorry, you need to enter at least {} characters. Please try again!".format(least))
            continue
        elif len(user_input) > most:
            print("We're sorry, you can't enter more than {} characters here. Please try again!".format(most))
            continue
        else:
            return user_input


# function for getting string input where character limits are not necessary // m = input
def get_string(m):
    # .strip() means that extraneous spaces will not return an error message
    user_input = input(m).strip()
    return user_input


# function for printing a menu from a list with two elements // g = relevant list
def print_menu(g):
    for x in g:
        output = '{:<5} -- {:<5}'.format(x[0], x[1])
        print(output)


# function for printing a list with its indices // m = input
def print_menu_indices(m):
    for i in range(0, len(m)):
        output = "{:<5}{:<20}{:<10}".format(i, m[i][0], m[i][1])
        print(output)


# function for printing a dictionary // m = input
def print_dict(m):
    for x in m:
        print(x, ' -- ', m[x])


# function for detecting when a pizza type has been ordered that's already contained on the "order" list - will add
# quantities together
# f = "order", z = "pizza_menu", p = "pizza", q = "quantity"
def quantity_adder(f, z, p, q):
    # defines the name of the pizza the user just ordered as pizza_name
    pizza_name = z[p][0]
    for x in range(0, len(f)):
        # checks if any of the pizzas already in the order list match pizza_name
        if pizza_name in f[0]:
            # if they do match, adds the specified amount to the existing quantity
            f[x][1] += q
        # if there is no match, adds the new pizza type as normal
        else:
            addition = [z[p][0], q, z[p][1]]
            f.append(addition)


# function for calculating total costs; "g" is delivery_info while "c" is costs
def calculator(g, c):
    # calculates the sum of the "costs" list (the list containing all the pizza prices)
    total = sum(c)
    # checks if a collection type has already been specified
    try:
        # checks if the collection type is set as delivery, adds delivery charge if appropriate
        if g['Kind'] == "Delivery":
            total += 3
            return total
        # if the delivery is set for pickup, returns total as is
        else:
            return total
    # if a delivery type hasn't already been specified, returns total as is
    except KeyError:
        return total


# function for allowing the operator to enter their order into the system
# f = order (list containing order information), z = pizza_list (menu containing names and prices of pizzas)
# g = delivery_info (list containing delivery type + customer information)
# c = costs (list containing total cost of order so far)
def add_to_order(f, z, g, c):
    run = True
    while run is True:
        # prints the pizza menu with indices
        print_menu_indices(z)
        # asks the user for input regarding the details of their order
        pizza = get_integer("Please enter the index number of the pizza you'd like to order: ", 0, len(z))
        quantity = get_integer("Please enter the number of these pizzas that you would like: ", 1, 20)
        # calculates the cost of what the user has just ordered and adds it to "cost list"
        cost = z[pizza][1] * quantity
        c.append(cost)
        # checks if there is no information already in the order list
        if len(f) == 0:
            # defines the "addition" (that is, the details of the order) and appends it to the main order_list
            addition = [z[pizza][0], quantity, z[pizza][1]]
            f.append(addition)
        # if there is already information in the order list, program proceeds to another function
        elif len(f) > 0:
            quantity_adder(f, z, pizza, quantity)
        # checks how many pizzas the user has ordered so the "success" statement is grammatically correct
        if quantity == 1:
            print("You have successfully added 1 {} pizza to your order.".format(z[pizza][0].lower()))
        elif quantity > 1:
            print("You have successfully added {} {} pizzas to your order.".format(quantity, z[pizza][0].lower()))
        total = calculator(g, c)
        print("Your total cost is now ${}.".format(total))
        # asks the user for input regarding what they want to do next - determines whether they continue with this
        # or return to the main function
        add = get_string("Would you like to order anything else? Enter 'y' if yes, or any other key to "
                         "move on. ").lower()
        if add == "y":
            continue
        else:
            return


# function for allowing the user to remove items from their order
# "o" = order (list containing order information), "c" = costs (list containing the total price of everything the user
# has ordered so far
def edit_order(o, c):
    # puts the function in a loop so it can be repeated if the user wants to delete multiple items consecutively
    run = True
    while run is True:
        # doesn't allow the function to run if nothing has been ordered yet
        if len(o) == 0:
            print("There's nothing to delete! Try ordering something first.")
            return
        else:
            # prints the order so far
            print("Your order:")
            print_menu_indices(o)
            # asks the user for input regarding the changes they wish to make
            change = get_integer("Please enter the index number of the item you would like to change: ", 0, len(o))
            num = get_integer("How many would you like to remove from your order? ", 0, o[change][1])
            # subtracts 'num' from the quantity inside the order list
            o[change][1] -= num
            # calculates the cost of the subtracted quantity
            less_amount = num * o[change][2]
            # calculates the customer's new total
            new_c = sum(c) - less_amount
            # clears existing "costs" information and replaces it with "new_c"
            c.clear()
            c.append(new_c)
            # removes the pizza name from the menu entirely so it doesn't print out with a quantity of 0
            if o[change][1] < 1:
                o.pop(change)
            print("Success! It's been removed.")
            # checks if the user would like to perform the action again or return to the main menu
            add = get_string("Would you like to remove anything else? Enter 'y' if yes, or any other key to "
                             "move on. ").lower()
            if add == "y":
                continue
            else:
                return


# function for allowing the user to update their pickup/delivery information
def get_customer_info(d):
    run = True
    while run is True:
        # checks if the user has added input before
        if len(d) == 0:
            order_kind = get_string("Would you like pickup or delivery? "
                                    "Please enter either 'p' for pickup or 'd' for delivery. ").lower()
            # sends them to a function based on whether they want to pick up their pizza or have it delivered as
            # different information is required for both
            if order_kind == "p":
                get_pickup_info(d)
                return d
            elif order_kind == "d":
                get_delivery_info(d)
                return d
            # if they've entered something irrelevant they receive an error message and are asked to choose again
            else:
                print("You must enter either 'p' or 'd' here. Please try again.")
                continue
        # if they've already got their delivery/pickup information stored in the system
        elif len(d) > 0:
            options = '''
            A: Change delivery method
            B: Update name
            C: Update address
            D: Update phone number
            E: Never mind, take me back
            '''
            print(options)
            # asks for user input to proceed
            change = get_string("What would you like to change? ").upper()
            # sends the user to a function that will collect information based on their chosen method of collection
            if change == "A":
                print("Your order is currently scheduled for {}".format(d['Kind']))
                d['Kind'] = get_string("Please enter either 'p' for pickup or 'd' for delivery: ").lower()
                if d['Kind'] == 'd':
                    get_delivery_info(d)
                    return
                elif d['Kind'] == 'p':
                    get_pickup_info(d)
                    return
                else:
                    # in case the user enters the wrong thing
                    print("You must enter either 'p' or 'd' here. Please try again.")
                    return
            # choosing options B, C and E allows the user to edit individual pieces of information by asking for new
            # input and replacing the existing values in the dictionary
            elif change == "B":
                d['Name'] = get_controlled_string("Please enter the name you would prefer us to use.", 2, 35).title()
                print("Success! Your name is now registered as {}.".format(d['Name']))
            elif change == "C" and d['Kind'] == 'Delivery':
                d["Address"] = get_address(d)
                print("Success! Your address is now registered as {}.".format(d['Address']))
            elif change == "C" and d['Kind'] == 'Pickup':
                print("Your order is currently scheduled for pickup - we don't require your address at this stage.")
            elif change == "D" and d['Kind'] == 'Delivery':
                d['Phone'] = get_integer("Please enter the number you would prefer to use: ", 100, 9999999999)
                print("Your phone number is now registered as {}".format(d['Phone']))
            elif change == "D" and d['Kind'] == 'Pickup':
                print("Your order is currently scheduled for pickup - we don't require your phone number at "
                      "this stage.")
            # takes the user back to the main function if they have changed their mind about editing information
            elif change == "E":
                return
            else:
                print("You must enter an option from the list! Please try again.")
                continue
            return


# function for collecting information from a user who wants to pick up their pizza
def get_pickup_info(d):
    d['Kind'] = "Pickup"
    d['Name'] = get_controlled_string("Please enter your name: ", 2, 35).title()
    print("Great! You will be able to pick up your order using the name {}".format(d['Name']))
    return


# function for collecting information from a user who wants their pizza delivered
def get_delivery_info(d):
    d['Kind'] = "Delivery"
    d['Name'] = get_controlled_string("Please give a delivery name: ", 2, 35).title()
    # sends the user to the get_address function as the process is more complicated
    d['Address'] = get_address(d)
    d['Phone'] = get_integer("Please enter a phone number for the order: ", 100, 9999999999)
    print("Great! Your order will be delivered to {} at {}, with the phone number {}. A $3 delivery charge has been "
          "added".format(d['Name'], d['Address'], d['Phone']))
    return


# function for collecting a customer's address
def get_address(d):
    # list contains all aspects of the address, each one asks for the user's input
    new_list = {'District': get_controlled_string("Please enter your suburb or neighbourhood: ", 3, 25).title(),
                'Street': get_controlled_string("Please enter a street name: ", 4, 25).title(),
                'Number': get_integer("Please enter your building number: ", 1, 9999),
                'Apartment': get_controlled_string("Please enter an apartment number (if not applicable, press the "
                                                   "enter key to continue)", 0, 4)}
    # if the user does not enter an apartment number:
    if new_list['Apartment'] == "":
        # splices together all elements of the address into standard format under the address_list variable
        address_list = "{}{} {}, {}".format(new_list['Apartment'], new_list['Number'], new_list['Street'],
                                            new_list['District'])
        # prints the address the system has recorded for the user's benefit (in case of mistakes)
        print("Your address has been registered as {}.".format(address_list))
        # adds the address_list information to the main list
        d['Address'] = address_list
        return address_list
    # if the user does enter an apartment number
    else:
        address_list = "{}{} {}, {}".format(new_list['Number'], new_list['Apartment'], new_list['Street'],
                                            new_list['District'])
        d['Address'] = address_list
        return address_list


# function that allows the user to clear large chunks of their information from the system at once
def empty(a, b):
    run = True
    while run is True:
        delete_options = '''
        A: Clear all information
        B: Clear your order only
        C: Clear your personal information only
        D: Delete something specific from your order
        E: Never mind, take me back
        '''
        # checks that there is something for the system to delete
        if len(a) > 0 or len(b) > 0:
            # prints the list of things the user can delete
            print(delete_options)
            # asks the user what they want to do, acts based on that choice
            choice = get_string("What would you like to do? ").upper()
            # clears all information from all lists
            if choice == "A":
                a, b.pop()
                print("All of your information has been cleared. Feel free to start again.")
            # clears all stored order information
            elif choice == "B":
                a.pop()
                print("Your order has been emptied. You'll need to re-enter it in order to receive your pizza.")
            # clears all stored customer info
            elif choice == "C":
                b.pop()
                print("Your personal information has been cleared. You'll need to re-enter it in order to receive your "
                      "pizza.")
            # if the user wants to delete something specific, gives them directions as to how they can do that elsewhere
            # using the program
            elif choice == "D":
                print("Sorry, but you can't edit specific information here! You'll need to return to the main menu and "
                      "select option B or C.")
                return
            # returns the user to the main program if they change their mind about clearing data
            elif choice == "E":
                return
            # in case the user inputs the wrong thing
            else:
                print("Sorry, but that option isn't on the list! Please try again!")
                continue
        # feeds back to the user if there is no information to clear, returns them to the main program
        else:
            print("There's nothing to get rid of yet!")
            return


# function for printing the user receipts
def print_receipt(a, b, c):
    # if no food has actually been ordered yet
    if len(a) == 0:
        print("You haven't ordered anything yet!")
    # prints food order
    elif len(a) > 0:
        print("Your order:")
        print_menu(a)
    # if there are no collection details/customer information yet
    if len(b) == 0:
        print("You haven't entered any collection details yet!")
    # prints customer information
    elif len(b) > 0:
        print("Your collection details:")
        print_dict(b)
    total = calculator(b, c)
    print("Total cost: ${}".format(total))


# function for confirming the order and finishing with the program
def confirm_order(a, b, c):
    run = True
    while run is True:
        # the order cannot be confirmed if it is missing information, so the program will feed back to the user then
        # return them to the main page
        if len(a) == 0:
            print("You can't finish just yet! You haven't ordered anything from us.")
            return
        elif len(b) == 0:
            print("You can't finish just yet! We still need you to send us delivery/pickup information.")
            return
        else:
            # prints all order information for the user to view
            print_receipt(a, b, c)
            # gets the user to confirm if they would like to proceed
            goahead = get_string("Would you like to confirm your order and exit the program? Please enter 'y' for yes "
                                 "or 'n' for no: ").lower()
            if goahead == "y":
                print("Thank you so much for ordering from us! Your food will be with you shortly.")
                # ends the program
                exit()
            elif goahead == "n":
                print("Need to change something? We'll send you back to the main menu now.")
                # returns the user to the main menu
                return
            # in case of user input error, starts the function again
            else:
                print("Sorry, but you have to enter either 'y' or 'n' here! Please try again: ")
                return confirm_order(a, b, c)


# main function where the code runs from
def main():
    regular = 15
    gourmet = 20
    costs = [
    ]
    # menu for customers to order from
    pizza_list = [
        ["Cheese", regular],
        ["Pepperoni", regular],
        ["Vegetarian", regular],
        ["Garlic", regular],
        ["Chicken", regular],
        ["Marinara", regular],
        ["Calzone", regular],
        ["Meat-lovers", gourmet],
        ["Hawaiian", gourmet],
        ["Bacon Cheeseburger", gourmet],
    ]
    # where details of the food the customer has ordered is stored
    order = [
    ]
    # where details of the delivery/pickup situation is stored
    delivery_info = {
    }
    options = '''
        A: Order a pizza
        B: Delete something from your order
        C: Edit delivery information
        D: View your receipt so far
        E: Clear all information and start again
        F: View the menu
        G: Confirm your order
        H: Cancel your order and exit the program
    '''
    print("Welcome to the Pizza Store!")
    run = True
    while run is True:
        # prints list of interactive options for the user
        print(options)
        # asks the user what they would like to do, calls a function based on their choice
        end = get_string("Please select an option from the list to proceed: ").upper()
        if end == "A":
            add_to_order(order, pizza_list, delivery_info, costs)
        elif end == "B":
            edit_order(order, costs)
            continue
        elif end == "C":
            get_customer_info(delivery_info)
            continue
        elif end == "D":
            print_receipt(order, delivery_info, costs)
            continue
        elif end == "E":
            empty(order, delivery_info)
            continue
        elif end == "F":
            print_menu_indices(pizza_list)
            continue
        elif end == "G":
            confirm_order(order, delivery_info, costs)
        elif end == "H":
            # asks the user for confirmation if they really want the program to end
            confirm = get_string("Are you sure you want to quit the program? "
                                 "Enter 'y' to confirm, or any other key to go back. ").lower()
            if confirm != "y":
                # returns the user to the main loop if they fail to confirm
                continue
            else:
                print("Program has finished. ")
                # ends program
                exit()
        # in case of user input error
        else:
            print("Sorry, that isn't an option! Please enter one of the letter options on the list.")


# runs the main code
if __name__ == "__main__":
    main()
