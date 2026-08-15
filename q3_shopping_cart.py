def add_item_bug(item, cart=[]):
    cart.append(item)
    return cart


print("PART A - Mutable Default Argument")
print(add_item_bug("apple"))
print(add_item_bug("banana"))
print(add_item_bug("milk", ["bread"]))
print(add_item_bug("eggs"))


def add_item(item, cart=None):
    if cart is None:
        cart = []

    cart.append(item)
    return cart


print("\nPART B - Fixed Function")
print(add_item("apple"))
print(add_item("banana"))


def create_cart(owner, discount=0):
    return {
        "owner": owner,
        "items": [],
        "discount": discount
    }


def add_to_cart(cart, name, price, qty=1):
    item = {
        "name": name,
        "price": price,
        "qty": qty
    }

    cart["items"].append(item)


def update_price(price_tuple, new_price):
    try:
        price_tuple[0] = new_price
    except TypeError:
        print("TypeError: Tuple elements cannot be changed.")


def calculate_total(cart):
    total = 0

    for item in cart["items"]:
        total = total + item["price"] * item["qty"]

    discount_amount = total * cart["discount"] / 100
    final_total = total - discount_amount

    return final_total


print("\nPART C - Shopping Cart")

cart1 = create_cart("Aarav", 10)

add_to_cart(cart1, "Pen", 20, 2)
add_to_cart(cart1, "Notebook", 50, 1)

cart2 = create_cart("Priya", 5)

add_to_cart(cart2, "Bag", 500, 1)
add_to_cart(cart2, "Bottle", 100, 2)

print("\nCustomer 1:", cart1["owner"])
print("Items:", cart1["items"])
print("Final Total:", calculate_total(cart1))

print("\nCustomer 2:", cart2["owner"])
print("Items:", cart2["items"])
print("Final Total:", calculate_total(cart2))

print("\nTuple Test")

price = (100, "Pen")

update_price(price, 120)


# Discussion:
# cart=[] is dangerous because the same list is reused between calls.
# Rebinding means assigning a variable to a new object.
# Mutation means changing the existing object.
# Lists, sets and dictionaries are mutable.
# Tuples, strings and integers are immutable.
# A list passed to a function can be modified inside the function.