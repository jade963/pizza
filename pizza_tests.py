# function for getting integer input from the user
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


# function for getting string input from the user
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


# function for getting string input where character limits are not necessary
def get_string(m):
    user_input = input(m)
    return user_input


# function for printing a menu from a list with two elements
def print_menu(g):
    for x in g:
        output = '{} -- {}'.format(x[0], x[1])
        print(output)


# function for printing a list with its indices
def print_menu_indices(m):
    for i in range(0, len(m)):
        output = "{:<5}{:20}${:<10.2f}".format(i, m[i][0], m[i][1])
        print(output)


# function for printing a dictionary
def print_dict(m):
    for x in m:
        print(x, ' : ', m[x])


# function for allowing the operator to enter their order into the system
def add_to_order(f, z, t):
    run = True
    while run is True:
        # prints the pizza menu with indices
        print_menu_indices(z)
        # asks the user for input regarding the details of their order
        pizza = get_integer("Please enter the index number of the pizza you'd like to order: ", 0, 2)
        quantity = get_integer("Please enter the number of these pizzas that you would like: ", 1, 10)
        comments = get_controlled_string(
            "Please enter any additional instructions you would like to go with your order: ", 0, 200)
        # defines the "addition" (that is, the details of the order) and appends it to the main order_list
        addition = [z[pizza][0], quantity, comments]
        f.append(addition)
        # calculates the cost of what the user has just ordered
        t += z[pizza][1] * quantity
        # checks how many pizzas the user has ordered so the "success" statement is grammatically correct
        if quantity == 1:
            print("You have successfully added 1 {} pizza to your order.".format(z[pizza][0].lower()))
        elif quantity > 1:
            print("You have successfully added {} {} pizzas to your order.".format(quantity, z[pizza][0].lower()))
        print("Your total cost is now ${}.".format(t))
        # asks the user for input regarding what they want to do next - determines whether they continue with this
        # or return to the main function
        add = get_string("Would you like to order anything else? Press 'y' if yes, or any other key to continue. ")
        if add == "y":
            continue
        else:
            return


# function for allowing the user to remove items from their order
def edit_order():
    return None


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
                    return d
                elif d['Kind'] == 'p':
                    get_pickup_info(d)
                    return d
                else:
                    # in case the user enters the wrong thing
                    print("You must enter either 'p' or 'd' here. Please try again.")
                    return
            # choosing options B, C and E allows the user to edit individual pieces of information by asking for new
            # input and replacing the existing values in the dictionary
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
            # takes the user back to the main function if they have changed their mind about editing information
            elif change == "E":
                return
            else:
                print("You must enter an option from the list! Please try again.")
                continue
            return d


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
        address_list = "{}{} {} {}".format(new_list['Apartment'], new_list['Number'], new_list['Street'],
                                           new_list['District'])
        # prints the address the system has recorded for the user's benefit (in case of mistakes)
        print("Your address has been registered as {}".format(address_list))
        # adds the address_list information to the main list
        d['Address'] = address_list
        return address_list
    # if the user does enter an apartment number
    else:
        address_list = "{}{} {} {}".format(new_list['Number'], new_list['Apartment'], new_list['Street'],
                                           new_list['District'])
        print("Your address has been registered as {}".format(address_list))
        d['Address'] = address_list
        return address_list


# function that allows the user to clear large chunks of their information from the system at once
def clear(a, b, c):
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
                a, b, c.pop()
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
                      "choose"
                      "option B or C.")
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
def print_receipt(a, b, t):
    # if no food has actually been ordered yet
    if len(a) == 0:
        print("You haven't ordered anything yet!")
    # prints food order
    elif len(a) > 0:
        print("Your order:")
        print_menu(a)
        print("Total cost: ${}".format(t))
    # if there are no collection details/customer information yet
    if len(b) == 0:
        print("You haven't entered any collection details yet!")
    # prints customer information
    elif len(b) > 0:
        print("Your collection details:")
        print_dict(b)


# function for confirming the order and finishing with the program
def confirm_order(a, b, t):
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
            print_receipt(a, b, t)
            # gets the user to confirm if they would like to proceed
            goahead = get_string("Would you like to confirm your order and exit the program? Please enter 'y' for yes "
                                 "or 'n' for no: ")
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
                return confirm_order(a, b, t)


# main function where the code runs from
def main():
    # total cost
    total_cost = 0
    # menu for customers to order from
    pizza_list = [
        ["Cheese", 15],
        ["Pepperoni", 15],
        ["Hawaiian", 20],
    ]
    # where details of the food the customer has ordered is stored
    order = [
    ]
    # where details of the delivery/pickup situation is stored
    delivery_info = {
    }
    options = '''
        A: Add to your order
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
        end = get_controlled_string("Please select an option from the list to proceed: ", 1, 1).upper()
        if end == "A":
            add_to_order(order, pizza_list, total_cost)
        elif end == "B":
            edit_order()
            continue
        elif end == "C":
            get_customer_info(delivery_info)
            # calculates delivery fees at the end of each update
            if delivery_info["Kind"] == "Delivery":
                total_cost += 3
                print("A $3 delivery charge has been added to your total. Your total currently stands at ${}".format
                      (total_cost))
            elif delivery_info["Kind"] == "Pickup":
                print("There is no charge for pickup. Your total currently stands at ${}".format(total_cost))
            continue
        elif end == "D":
            print_receipt(order, delivery_info, total_cost)
            continue
        elif end == "E":
            clear(order, delivery_info, total_cost)
            continue
        elif end == "F":
            print_menu_indices(pizza_list)
            continue
        elif end == "G":
            confirm_order(order, delivery_info, total_cost)
        elif end == "H":
            # asks the user for confirmation if they really want the program to end
            confirm = get_string("Are you sure you want to quit the program? "
                                 "Enter 'y' to confirm, or any other key to go back. ")
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
