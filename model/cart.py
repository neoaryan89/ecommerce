class Cart:
    cart_items=[]
    cart_discount=0
    cart_total=0
    cart_tax=0
    cart_shipping=None
    cart_billing=None

    def get_items(self):
        return self.cart_items

    def set_items(self,items):
        self.items = items

    def get_discount(self):
        return self.cart_discount

    def set_x(self, discount):
        self.discount = discount

    def get_total(self):
        return self.cart_total

    def set(self, x):
        self.cart_discount = discount

    def get_tax(self):
        return self.cart_tax

    def set_tax(self, tax):
        self.cart_tax=tax   

    def get_shipping(self):
        return self.cart_shipping

    def set_shipping(self, shipping):
        self.cart_shipping= shipping

    def get_billing(self):
        return self.cart_billing

    def set_billing(self, billing):
        self.cart_billing= billing    