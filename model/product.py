class Product:

    product_type = "simple"
    product_name = ""

    def get_type(self):
        return self.product_type

    def set_type(self,product_type):
        self.product_type = product_type   

    def get_name(self):
        return self.product_name

    def set_name(self, product_name):
        self.product_name = product_name