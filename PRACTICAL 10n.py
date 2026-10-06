products = ["pen", "book", "bag", "pencil"]

item = input("Enter item name: ").lower()

if item in products:
    print("Item found")
    print("Index:", products.index(item))
else:
    print("Item not found")
