class Shipping():
    def __init__(self,order,shipping_service,fee,client,date,status):
        self.order = order
        self.shipping_service = shipping_service
        self.fee = fee
        self.client = client
        self.date = date
        self.status = status
        
class MRW(Shipping):
    def __init__(self,order,client,date,status):
        super().__init__(order,'MRW',7,client,date,status)
        
class Zoom(Shipping):
    def __init__(self,order,client,date,status):
        super().__init__(order,'Zoom',10,client,date,status)

class Delivery(Shipping):
    def __init__(self,order,client,date,delivery_info,status):
        super().__init__(order,'Delivery',4,client,date,status)
        self.delivery_info = delivery_info
        
