from pizzapy import *

#Wisconsin 6 Cheese Pizza "thin wisconsin"
#Brooklyn Pizza "brooklyn"

def order_pizza(first, last, email, phone_number, address, pizza):
    try:
        #customer = Customer('Barack', 'Obama', 'barack@whitehouse.gov', '2024561111',
         #                   '700 Pennsylvania Avenue NW, Washington, DC, 20408')
        customer = Customer(first, last, email, phone_number, address)
        my_local_dominos = StoreLocator.find_closest_store_to_customer(customer)
        menu = my_local_dominos.get_menu()
        card = CreditCard('4100123422343234', '0115', '777', '90210')
        order = Order.begin_customer_order(customer, my_local_dominos)
        if pizza == "thin wisconsin":
            order.add_item("P14IRECZ")
        elif pizza == "brooklyn":
            order.add_item("PBKIREZA")
        order.place(card)
        return my_local_dominos.place_order(order, card)
    except:
        pass
