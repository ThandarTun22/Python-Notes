class RestaurantTable:

    menus = {
        'pizza' : 5000,
        'cola' : 600,
        'apple juice' : 2000,
        'hamburger' : 1000,
        'fried potato' : 1500

    }

    def __init__(self):
        self.total = 0
        self.orders = []

    def addOrder(self, order):
        self.orders.append(order)   # add item to list
        self.total += self.menus[order]   

    def printBill(self):
        for order in self.orders:
            print(f'{order} : {self.menus[order]}')
        print("-----------------------")

        print(f'total price : {self.total}')

def startProgram():
    table = RestaurantTable()
    show_menus = table.menus.keys()
    print("-------------Menus----------------")
    for show_menu in show_menus:
        print(show_menu + "\n")
    print("=================================")

    while True:
        order = input('order :')
        table.addOrder(order)

        another = input('order again ? y/n :')
        if another == 'y':
            continue    # loop again

        if another == 'n':
            table.printBill()
            break

startProgram()