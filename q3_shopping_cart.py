
# PART A

def add_item(item, cart=[]):
    cart.append(item)
    return cart

print(add_item("apple"))
print(add_item("banana"))
print(add_item("milk", cart=["bread"]))
print(add_item("eggs"))

# PART B

def add_item_fixed(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart

print("\nFixed Version")
print(add_item_fixed("apple"))
print(add_item_fixed("banana"))
print(add_item_fixed("milk", ["bread"]))
print(add_item_fixed("eggs"))

# PART C

def create_cart(owner, discount=0):
    return {
        "owner": owner,
        "items": [],
        "discount": discount
    }

def add_to_cart(cart, name, price, qty=1):
    cart["items"].append({
        "name": name,
        "price": price,
        "qty": qty
    })

def update_price(price_tuple, new_price):
    try:
        price_tuple[0] = new_price

    except TypeError as e:
        print("Tuple Error:", e)

def calculate_total(cart):
    total = 0
    for item in cart["items"]:
        total += item["price"] * item["qty"]

    discount_amount = total * (cart["discount"] / 100)
    final_total = total - discount_amount
    return final_total

customer1 = create_cart("Vaishnavi", 10)
add_to_cart(customer1, "Laptop", 50000, 1)
add_to_cart(customer1, "Mouse", 1000, 2)
customer2 = create_cart("Rahul", 5)
add_to_cart(customer2, "Phone", 20000, 1)
add_to_cart(customer2, "Earphones", 2000, 1)
print("\nCustomer 1 Total:")
print(calculate_total(customer1))
print("\nCustomer 2 Total:")
print(calculate_total(customer2))
price = (1000,)
update_price(price, 1200)

#Q1
# Because integers are immutable objects.
# They cannot be modified accidentally.
#Q2 
# Because lists are mutable and the same
# list object gets reused across function calls.
#Q3
# Rebinding:
#     x = [1, 2]
#     x = [3, 4]
# Creates a new object reference.
#
# Mutating:
#     x.append(5)
# Modifies the existing object.
#Q4
# Mutable:
#     list, dict, set
#
# Immutable:
#     tuple, int, float, str
#Q5
# affect the original list?
#
# Because Python passes references to objects.
# Both variables point to the same list object.

