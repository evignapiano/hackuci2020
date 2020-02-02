from pizzapy import *

#Wisconsin 6 Cheese Pizza
#Hand Tossed Pizza

customer = Customer('Barack', 'Obama', 'barack@whitehouse.gov', '2024561111', '2272 Michelson Dr, Irvine, CA, 92612')
my_local_dominos = StoreLocator.find_closest_store_to_customer(customer)
menu = my_local_dominos.get_menu()
print(menu.search(Name = 'Pizza'))
card = CreditCard('4100123422343234', '0115', '777', '90210')
order = Order.begin_customer_order(customer, my_local_dominos)
order.add_item("20BCOKE")
order.place(card)
my_local_dominos.place_order(order, card)