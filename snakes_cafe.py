print("""**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
""")

appetizers = ['Appetizers', '----------', 'Wings', 'Cookies', 'Spring Rolls']
entrees = ['Entrees', '-----', 'Salmon', 'Steak', 'Meat Tornado', 'A Literal Garden']
desserts = ['Desserts', '--------', 'Ice Cream', 'Cake', 'Pie']
drinks = ['Drinks', '------', 'Coffee', 'Tea', 'Unicorn Tears']


print("\n".join(appetizers))
print("\n".join(entrees))
print("\n".join(desserts))
print("\n".join(drinks))

print("""***************************************
** What would you like to order? **
*************************************** """)

items = {}

while True:
    order = input('> ')
    if order == 'quit':
        break
    elif order not in items:
        items[order] = 0

    items[order] += 1
    print(f"** {items[order]} order of {order} have been added to your meal **")
