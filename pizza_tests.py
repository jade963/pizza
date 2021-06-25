def get_integer(m):
    user_input = int(input(m))
    return user_input


def get_string(m):
    user_input = input(m)
    return user_input


def print_menu(g):
    for x in g:
        output = "{:<10} -- {:>5}".format(x[0], x[1])
        print(output)


def print_menu_indices(g):
    for i in range(0, len(g)):
        print("{} : {}".format(i, g[i]))


def add_to_order(f):
    pizza_list = [
        ["Cheese", 15.5],
        ["Pepperoni", 15.5],
        ["Hawaiian", 20],
    ]
    print_menu_indices(pizza_list)
    pizza = get_integer("Please enter the index number of the pizza you'd like to order: ")
    quantity = get_integer("Please enter the number of these pizzas that you would like: ")
    comments = get_string("Please enter any additional instructions you would like to go with your order: ")
    addition = [pizza_list[pizza][0], quantity, comments]
    f.append(addition)
    add = get_string("Would you like to order anything else? Enter 'y' to continue, or anything else to quit. ")
    if add == "y":
        add_to_order(f)
    else:
        return


def edit_order(f):
    return None


def main():
    order = [
        ]
    edit_menu = '''
    a: remove an item
    b: add an item
    c: alter instructions
    '''
    print("Welcome to Marsden Pizzas!")
    add = get_string("Please enter 'y' to begin your order: ")
    while add == "y":
        add_to_order(order)
        print(order)
        accept = get_string("Great! This is your order so far. Is there anything you'd like to change? Press 'y' for "
        "yes, or any other key to confirm your order.")
        if accept == "y":
            edit_order(order)
            add = "stop"
        else:
            add = "stop"
            print("end of code")
            break


main()
