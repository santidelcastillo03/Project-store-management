class Payment():
    def __init__(self,client,payment_amount,payment_currency,payment_method,payment_date,status):
        self.client = client
        self.payment_amount = payment_amount
        self.payment_currency = payment_currency
        self.payment_method = payment_method
        self.payment_date = payment_date
        self.status = status
        