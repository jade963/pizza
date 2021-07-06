# function for getting integer input from the user
def get_integer(m):
    user_input = int(input(m))
    return user_input


# function for getting string input from the user
def get_string(m):
    user_input = input(m)
    return user_input


# function for printing a menu from a list with two elements
def print_menu(g):
    for x in g:
        output = "{:<10} -- {:>5}".format(x[0], x[1])
        print(output)


# function for printing a menu from a list with its indices
def print_menu_indices(g):
    for i in range(0, len(g)):
        print("{} -- {}".format(i, g[i]))


# function for allowing the operator to enter their order into the system
def add_to_order(f, z, d):
    run = True
    while run == True:
        print_menu_indices(z)
        pizza = get_integer("Please enter the index number of the pizza you'd like to order: ")
        quantity = get_integer("Please enter the number of these pizzas that you would like: ")
        comments = get_string("Please enter any additional instructions you would like to go with your order: ")
        addition = [z[pizza][0], quantity, comments]
        f.append(addition)
        d["Cost"] += z[pizza][1]*quantity
        add = get_string("Would you like to order anything else? Press 'y' if yes, or any other key to quit. ")
        if add == "y":
            continue
        else:
            return


def get_customer_info(d):
    order_kind = get_string("Would you like pick-up or delivery? ")
    d['Kind'] = order_kind
    if order_kind == "pickup":
        d['Name'] = get_string("Please enter a name: ")
        return d
    elif order_kind == "delivery":
        d['Cost'] += 3
        d['Name'] = get_string("Please give a delivery name: ")
        d['Address'] = get_string("Please enter a delivery address: ")
        d['Phone'] = get_integer("Please enter a phone number for the order: ")
        print("Your cost is now ${}".format(d['Cost']))
        return d


def edit_order(f):
    return None


# main function where the code runs from
def main():
    pizza_list = [
        ["Cheese", 15.5],
        ["Pepperoni", 15.5],
        ["Hawaiian", 20],
    ]
    order = [
        ]
    receipt = {
    }
    print("Welcome to Marsden Pizzas!")
    receipt['Cost'] = 0
    add = get_string("Please press enter to begin: ")
    while add == "":
        add_to_order(order, pizza_list, receipt)
        print(order)
        accept = get_string("Great! This is your order so far. Is there anything you'd like to change? Press 'y' for "
                            "yes, or any other key to confirm your order.")
        if accept == "y":
            edit_order(order)
            add = "stop"
        else:
            print(order)
            add = "stop"
    get_customer_info(receipt)
    print(receipt)
    print("Program has finished")


if __name__ == "__main__":
    main()
