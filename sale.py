class Sale():
    def __init__(self,client,product,product_quantity,payment_method,shipping_method,purchase_breakdown,date):
        self.client = client
        self.product = product
        self.product_quantity = product_quantity
        self.payment_method = payment_method
        self.shipping_method = shipping_method
        self.purchase_breakdown = purchase_breakdown 
        self.date = date