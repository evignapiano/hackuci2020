from pizzapy import *

#Wisconsin 6 Cheese Pizza
#Hand Tossed Pizza

def order_pizza(first, last, email, phone_number, address):
    try:
        #customer = Customer('Barack', 'Obama', 'barack@whitehouse.gov', '2024561111',
         #                   '700 Pennsylvania Avenue NW, Washington, DC, 20408')
        customer = Customer(first, last, email, phone_number, address)
        my_local_dominos = StoreLocator.find_closest_store_to_customer(customer)
        menu = my_local_dominos.get_menu()
        print(menu.search(Name = 'Pizza'))
        card = CreditCard('4100123422343234', '0115', '777', '90210')
        order = Order.begin_customer_order(customer, my_local_dominos)
        order.add_item("20BCOKE")
        order.place(card)
        return my_local_dominos.place_order(order, card)
    except:
        pass
