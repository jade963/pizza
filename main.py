def get_integer(m):
    user_input = int(input(m))
    return user_input


def get_string(m):
    user_input = input(m)
    return user_input


def print_menu(g):
    for x in g:
        output = "{:<10} -- {:>4}".format(x[0], x[1])
        print(output)


def main():
    pizza_list = [
        ["Cheese", 15.5],
        ["Pepperoni", 15.5],
        ["Hawaiian", 20],
    ]
    run = True
    while run == True:
        print("Welcome to Marsden Pizzas! Please see our menu: ")
        print_menu(pizza_list)
        run = False


main()
