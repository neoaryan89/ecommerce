import model.product
headphones = model.product.Product()
headphones.set_type("simple")
headphones.set_name("headphones")
print(headphones.get_type())