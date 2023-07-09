
import matplotlib.pyplot as plt
from sale_manager import *
from datetime import datetime
from payment_manager import *
from shipping_manager import *
currentDate = datetime.datetime.today()

'''----------------------------------SALE STATISTICS----------------------------------'''

def daily_sales(sale_list,daily_sales_list): 
    '''Muestra las ventas del dia'''
    for sale in sale_list:
        if datetime.datetime.strptime(sale.date,'%d/%m/%Y') <= currentDate and datetime.datetime.strptime(sale.date,'%d/%m/%Y') >= currentDate - datetime.timedelta(days=1):
            daily_sales_list.append(sale)
    for index,sale in enumerate(daily_sales_list):
        try:
            print(f'---------- {index+1} ----------\nCustomer: {sale.client["name"]}\nProduct/s: {sale.product["name"]}\nQuantity: {sale.product_quantity}\nPayment Method: {sale.payment_method}\nShipping Method: {sale.shipping_method}\nDate: {sale.date}\n')
        except:
            print(f'---------- {index+1} ----------\nCustomer: {sale.client.name}\nProduct/s: {sale.product.name}\nQuantity: {sale.product_quantity}\nPayment Method: {sale.payment_method}\nShipping Method: {sale.shipping_method}\nDate: {sale.date}\n')
    print('Total daily sales: ',len(daily_sales_list))
    
    
def weekly_sales(sale_list,weekly_sales_list): 
    '''Muestra las ventas de la semana'''
    for sale in sale_list:
        if datetime.datetime.strptime(sale.date,'%d/%m/%Y') <= currentDate and datetime.datetime.strptime(sale.date,'%d/%m/%Y') >= currentDate - datetime.timedelta(days=7):
            weekly_sales_list.append(sale)
    for index,sale in enumerate(weekly_sales_list):
        try:
            print(f'---------- {index+1} ----------\nCustomer: {sale.client["name"]}\nProduct/s: {sale.product["name"]}\nQuantity: {sale.product_quantity}\nPayment Method: {sale.payment_method}\nShipping Method: {sale.shipping_method}\nDate: {sale.date}\n')
        except:
            print(f'---------- {index+1} ----------\nCustomer: {sale.client.name}\nProduct/s: {sale.product.name}\nQuantity: {sale.product_quantity}\nPayment Method: {sale.payment_method}\nShipping Method: {sale.shipping_method}\nDate: {sale.date}\n')
    print('Total weekly sales: ',len(weekly_sales_list))
    
    
def monthly_sales(sale_list,monthly_sales_list): 
    '''Muestra las ventas del mes'''
    for sale in sale_list:
        if datetime.datetime.strptime(sale.date,'%d/%m/%Y') <= currentDate and datetime.datetime.strptime(sale.date,'%d/%m/%Y') >= currentDate - datetime.timedelta(days=30):
            monthly_sales_list.append(sale)
    for index,sale in enumerate(monthly_sales_list):
        try:
            print(f'---------- {index+1} ----------\nCustomer: {sale.client["name"]}\nProduct/s: {sale.product["name"]}\nQuantity: {sale.product_quantity}\nPayment Method: {sale.payment_method}\nShipping Method: {sale.shipping_method}\nDate: {sale.date}\n')
        except:
            print(f'---------- {index+1} ----------\nCustomer: {sale.client.name}\nProduct/s: {sale.product.name}\nQuantity: {sale.product_quantity}\nPayment Method: {sale.payment_method}\nShipping Method: {sale.shipping_method}\nDate: {sale.date}\n')
    print('Total monthly sales: ',len(monthly_sales_list))
    
    
def yearly_sales(sale_list,yearly_sales_list): 
    '''Muestra las ventas del año'''
    for sale in sale_list:
        if datetime.datetime.strptime(sale.date,'%d/%m/%Y') <= currentDate and datetime.datetime.strptime(sale.date,'%d/%m/%Y') >= currentDate - datetime.timedelta(days=365):
            yearly_sales_list.append(sale)
    for index,sale in enumerate(yearly_sales_list):
        try:
            print(f'---------- {index+1} ----------\nCustomer: {sale.client["name"]}\nProduct/s: {sale.product["name"]}\nQuantity: {sale.product_quantity}\nPayment Method: {sale.payment_method}\nShipping Method: {sale.shipping_method}\nDate: {sale.date}\n')
        except:
            print(f'---------- {index+1} ----------\nCustomer: {sale.client.name}\nProduct/s: {sale.product.name}\nQuantity: {sale.product_quantity}\nPayment Method: {sale.payment_method}\nShipping Method: {sale.shipping_method}\nDate: {sale.date}\n')
    print('Total yearly sales: ',len(yearly_sales_list))
    
    
def best_selling_products(sale_list,best_selling_products_list): 
    '''Muestra los productos más vendidos'''
    product_list_stat = []
    for sale in sale_list:
        product_list_stat.append(sale.product)
    for product in product_list_stat:
        
        if product_list_stat.count(product) > 1:
            best_selling_products_list.append(product)
        else:
            print('There are no best selling products yet')
    for product in best_selling_products_list:
        print(f'----------  ----------\nName: {product["name"]}\nDescription: {product["description"]}\nPrice: {product["price"]}\nCategory: {product["category"]}\n')
    print('Total products: ',product_list_stat.count(product))
    
def most_frequent_customers(sale_list,most_frequent_customers_list): 
    '''Muestra los clientes más frecuentes'''
    customer_list_stat = []
    for sale in sale_list:
        customer_list_stat.append(sale.client)
    for customer in customer_list_stat:
        if customer_list_stat.count(customer) > 1:
            most_frequent_customers_list.append(customer)
        else:
            print('There are no most frequent customers yet')
    for client in most_frequent_customers_list:
        print(f'----------  ----------\nName: {client["name"]}\nCustomer type: {client["client_type"]}\nID: {client["id"]}\nEmail: {client["email"]}\nShipping address: {client["shipping_address"]}\nPhone number: {client["phone_number"]}\n')
    print('Total customers: ',customer_list_stat.count(client))

def sales_report(sale_list,daily_sales_list,weekly_sales_list,monthly_sales_list,yearly_sales_list,best_selling_products_list,most_frequent_customers_list): 
    option  = int(input('Enter the report you want to see:\n\n1 - Daily sales\n2 - Weekly sales\n3 - Monthly sales\n4 - Yearly sales\n5 - Best selling products\n6 - Most frequent customers\n\n-->'))
    if option == 1:
        daily_sales(sale_list,daily_sales_list)
    elif option == 2:
        weekly_sales(sale_list,weekly_sales_list)
    elif option == 3:
        monthly_sales(sale_list,monthly_sales_list)
    elif option == 4:
        yearly_sales(sale_list,yearly_sales_list)
    elif option == 5:
        best_selling_products(sale_list,best_selling_products_list)
    elif option == 6:
        most_frequent_customers(sale_list,most_frequent_customers_list)
    else:
        print('Invalid option')
        
        '''----------------------------------PAYMENT STATISTICS----------------------------------'''
        
def daily_payments(payment_list,daily_payments_list): 
    '''Muestra los pagos del día'''
    for payment in payment_list:
        if datetime.datetime.strptime(payment.payment_date,'%d/%m/%Y') <= currentDate and datetime.datetime.strptime(payment.payment_date,'%d/%m/%Y') >= currentDate - datetime.timedelta(days=1):
            daily_payments_list.append(payment)
    for index,payment in enumerate(daily_payments_list):
        try:
            print(f'---------- {index+1} ----------\nClient: {payment.client["name"]}\nPayment amount: {payment.payment_amount}\nPayment currency: {payment.payment_currency}\nPayment method: {payment.payment_method}\nPayment date: {payment.payment_date}\nStatus: {payment.status}\n')
        except:
            print(f'---------- {index+1} ----------\nClient: {payment.client.name}\nPayment amount: {payment.payment_amount}\nPayment currency: {payment.payment_currency}\nPayment method: {payment.payment_method}\nPayment date: {payment.payment_date}\nStatus: {payment.status}\n')
    print('Total daily payments: ',len(daily_payments_list))
    
    
def weekly_payments(payment_list,weekly_payments_list): 
    '''Muestra los pagos de la semana'''
    for payment in payment_list:
        if datetime.datetime.strptime(payment.payment_date,'%d/%m/%Y') <= currentDate and datetime.datetime.strptime(payment.payment_date,'%d/%m/%Y') >= currentDate - datetime.timedelta(days=7):
            weekly_payments_list.append(payment)
    for index,payment in enumerate(weekly_payments_list):
        try:
            print(f'---------- {index+1} ----------\nClient: {payment.client["name"]}\nPayment amount: {payment.payment_amount}\nPayment currency: {payment.payment_currency}\nPayment method: {payment.payment_method}\nPayment date: {payment.payment_date}\nStatus: {payment.status}\n')
        except:
            print(f'---------- {index+1} ----------\nClient: {payment.client.name}\nPayment amount: {payment.payment_amount}\nPayment currency: {payment.payment_currency}\nPayment method: {payment.payment_method}\nPayment date: {payment.payment_date}\nStatus: {payment.status}\n')
    print('Total weekly payments: ',len(weekly_payments_list))
    
    
def monthly_payments(payment_list,monthly_payments_list): 
    '''Muestra los pagos del mes'''
    for payment in payment_list:
        if  datetime.datetime.strptime(payment.payment_date,'%d/%m/%Y') <= currentDate and  datetime.datetime.strptime(payment.payment_date,'%d/%m/%Y') >= currentDate - datetime.timedelta(days=30):
            monthly_payments_list.append(payment)
    for index,payment in enumerate(monthly_payments_list):
        try:
            print(f'---------- {index+1} ----------\nClient: {payment.client["name"]}\nPayment amount: {payment.payment_amount}\nPayment currency: {payment.payment_currency}\nPayment method: {payment.payment_method}\nPayment date: {payment.payment_date}\nStatus: {payment.status}\n')
        except:
            print(f'---------- {index+1} ----------\nClient: {payment.client.name}\nPayment amount: {payment.payment_amount}\nPayment currency: {payment.payment_currency}\nPayment method: {payment.payment_method}\nPayment date: {payment.payment_date}\nStatus: {payment.status}\n')
    print('Total monthly payments: ',len(monthly_payments_list))
    
    
def yearly_payments(payment_list,yearly_payments_list): 
    '''Muestra los pagos del año'''
    for payment in payment_list:
        if  datetime.datetime.strptime(payment.payment_date,'%d/%m/%Y') <= currentDate and  datetime.datetime.strptime(payment.payment_date,'%d/%m/%Y') >= currentDate - datetime.timedelta(days=365):
            yearly_payments_list.append(payment)
    for index,payment in enumerate(yearly_payments_list):
        try:
            print(f'---------- {index+1} ----------\nClient: {payment.client["name"]}\nPayment amount: {payment.payment_amount}\nPayment currency: {payment.payment_currency}\nPayment method: {payment.payment_method}\nPayment date: {payment.payment_date}\nStatus: {payment.status}\n')
        except:
            print(f'---------- {index+1} ----------\nClient: {payment.client.name}\nPayment amount: {payment.payment_amount}\nPayment currency: {payment.payment_currency}\nPayment method: {payment.payment_method}\nPayment date: {payment.payment_date}\nStatus: {payment.status}\n')
    
def customers_with_pending_payments(payment_list,pending_payments): 
    '''Muestra los clientes con pagos pendientes'''
    for payment in payment_list:
        if payment.status == 'Pending':
            pending_payments.append(payment)
    for payment in pending_payments:
        try:
            print(f'----------  ----------\nClient: {payment.client["name"]}\nPayment amount: {payment.payment_amount}\nPayment currency: {payment.payment_currency}\nPayment method: {payment.payment_method}\nPayment date: {payment.payment_date}\nStatus: {payment.status}\n')
        except:
            print(f'----------  ----------\nClient: {payment.client.name}\nPayment amount: {payment.payment_amount}\nPayment currency: {payment.payment_currency}\nPayment method: {payment.payment_method}\nPayment date: {payment.payment_date}\nStatus: {payment.status}\n')
    print(f'Total customers with pending payments: {len(pending_payments)}\n')

def payments_report(payment_list,daily_payments_list,weekly_payments_list,monthly_payments_list,yearly_payments_list,pending_payments):
    option  = int(input('Enter the report you want to see:\n\n1 - Daily payments\n2 - Weekly payments\n3 - Monthly payments\n4 - Yearly payments\n5 - Customers with pending payments\n\n-->'))
    if option == 1:
        daily_payments(payment_list,daily_payments_list)
    elif option == 2:
        weekly_payments(payment_list,weekly_payments_list)
    elif option == 3:
        monthly_payments(payment_list,monthly_payments_list)
    elif option == 4:
        yearly_payments(payment_list,yearly_payments_list)
    elif option == 5:
        customers_with_pending_payments(payment_list,pending_payments)
    else:
        print('Invalid option')

'''----------------------------------SHIPPING STATISTICS----------------------------------'''

def daily_shipments(shipping_list,daily_shipments_list): 
    '''Muestra los envíos del día'''
    for shipment in shipping_list:
        if datetime.datetime.strptime(shipment.date,'%d/%m/%Y') <= currentDate and datetime.datetime.strptime(shipment.date,'%d/%m/%Y') >= currentDate - datetime.timedelta(days=1):
            daily_shipments_list.append(shipment)
    for index,shipment in enumerate(daily_shipments_list):
        print(f'---------- {index+1} ----------\nOrder: {shipment.order}\nShipping Method: {shipment.shipping_service}\nDate: {shipment.date}\nStatus: {shipment.status}\n')
    print('Total daily shipments: ',len(daily_shipments_list))
    
    
def weekly_shipments(shipping_list,weekly_shipments_list):
    '''Muestra los envíos de la semana'''
    for shipment in shipping_list:
        if datetime.datetime.strptime(shipment.date,'%d/%m/%Y') <= currentDate and datetime.datetime.strptime(shipment.date,'%d/%m/%Y') >= currentDate - datetime.timedelta(days=7):
            weekly_shipments_list.append(shipment)
    for index,shipment in enumerate(weekly_shipments_list):
        print(f'---------- {index+1} ----------\nOrder: {shipment.order}\nShipping Method: {shipment.shipping_service}\nDate: {shipment.date}\nStatus: {shipment.status}\n')
    print('Total weekly shipments: ',len(weekly_shipments_list)) 

def monthly_shipments(shipping_list,monthly_shipments_list): 
    '''Muestra los envíos del mes'''
    for shipment in shipping_list:
        if datetime.datetime.strptime(shipment.date,'%d/%m/%Y') <= currentDate and datetime.datetime.strptime(shipment.date,'%d/%m/%Y') >= currentDate - datetime.timedelta(days=30):
            monthly_shipments_list.append(shipment)
    for index,shipment in enumerate(monthly_shipments_list):
        print(f'---------- {index+1} ----------\nOrder: {shipment.order}\nShipping Method: {shipment.shipping_service}\nDate: {shipment.date}\nStatus: {shipment.status}\n')
    print('Total monthly shipments: ',len(monthly_shipments_list))
    
def yearly_shipments(shipping_list,yearly_shipments_list): 
    '''Muestra los envíos del año'''
    for shipment in shipping_list:
        if datetime.datetime.strptime(shipment.date,'%d/%m/%Y') <= currentDate and datetime.datetime.strptime(shipment.date,'%d/%m/%Y') >= currentDate - datetime.timedelta(days=365):
            yearly_shipments_list.append(shipment)
    for index,shipment in enumerate(yearly_shipments_list):
        print(f'---------- {index+1} ----------\nOrder: {shipment.order}\nShipping Method: {shipment.shipping_service}\nDate: {shipment.date}\nStatus: {shipment.status}\n')
    print('Total yearly shipments: ',len(yearly_shipments_list))
    
    
def most_shipped_products(shipping_list,most_shipped_products_list): 
    '''Muestra los productos más enviados'''
    product_list_stat = []
    for shipment in shipping_list:
        product_list_stat.append(shipment.order)
    for product in product_list_stat:    
        if product_list_stat.count(product) > 1:
            most_shipped_products_list.append(product)
        else:
            print('There are no most shipped products yet')
    for product in most_shipped_products_list:
        print(f'----------  ----------\nOrder: {shipment.order}\nShipping Method: {shipment.shipping_service}\nDate: {shipment.date}\nStatus: {shipment.status}\n')
    print('Most shipped products: ',len(most_shipped_products_list))

def pending_shipments(shipping_list,pending_shipments_list): 
    '''Muestra los envíos pendientes'''
    for shipment in shipping_list:
        if shipment.status == 'Pending':
            pending_shipments_list.append(shipment)
    for shipping in pending_shipments_list:
        print(f'----------  ----------\nOrder: {shipping.order}\nShipping Method: {shipping.shipping_service}\nDate: {shipping.date}\nStatus: {shipping.status}\n')
    print('Total pending shipments: ',len(pending_shipments_list))
    
def shipments_report(shipping_list,daily_shipments_list,weekly_shipments_list,monthly_shipments_list,yearly_shipments_list,most_shipped_products_list,pending_shipments_list):
    option  = (input('Enter the report you want to see:\n\n1 - Daily shipments\n2 - Weekly shipments\n3 - Monthly shipments\n4 - Yearly shipments\n5 - Most shipped products\n6 - Pending shipments\n-->'))
    if option == '1':
        daily_shipments(shipping_list,daily_shipments_list)
    elif option == '2':
        weekly_shipments(shipping_list,weekly_shipments_list)
    elif option == '3':
        monthly_shipments(shipping_list,monthly_shipments_list)
    elif option == '4':
        yearly_shipments(shipping_list,yearly_shipments_list)
    elif option == '5':
        most_shipped_products(shipping_list,most_shipped_products_list)
    elif option == '6':
        pending_shipments(shipping_list,pending_shipments_list)
    else:
        print('Invalid option')
    


'''----------------------------------SALE GRAPHS----------------------------------'''

def daily_sales_list_graph(daily_sales_list): 
    '''Muestra las ventas diarias en un gráfico'''
    x = []
    y = []
    for sale in daily_sales_list:
        x.append(sale[0])
        y.append(sale[1])
    plt.bar(x,y)
    plt.xlabel('Date')
    plt.ylabel('Sales')
    plt.title('Daily sales')
    plt.show()
def weekly_sales_graph(weekly_sales_list):
    '''Muestra las ventas semanales en un gráfico'''
    x = []
    y = []
    for sale in weekly_sales_list:
        x.append(sale.date)
        y.append(len(weekly_sales_list))
    plt.bar(x,y)
    plt.xlabel('Date')
    plt.ylabel('Sales')
    plt.title('Weekly sales')
    plt.show()
def monthly_sales_graph(monthly_sales_list): 
    '''Muestra las ventas mensuales en un gráfico'''
    x = []
    y = []
    for sale in monthly_sales_list:
        x.append(sale.date)
        y.append(len(monthly_sales_list))
    plt.bar(x,y)
    plt.xlabel('Date')
    plt.ylabel('Sales')
    plt.title('Monthly sales')
    plt.show()
def yearly_sales_graph(yearly_sales_list): 
    '''Muestra las ventas anuales en un gráfico'''
    x = []
    y = []
    for sale in yearly_sales_list:
        x.append(sale.date)
        y.append(len(yearly_sales_list))
    plt.bar(x,y)
    plt.xlabel('Date')
    plt.ylabel('Sales')
    plt.title('Yearly sales')
    plt.show()
def best_selling_products_graph(best_selling_products_list): 
    '''Muestra los productos más vendidos en un gráfico'''
    x = []
    y = []
    for product in best_selling_products_list:
        x.append(product.name)
        y.append(len(best_selling_products_list))
    plt.bar(x,y)
    plt.xlabel('Product')
    plt.ylabel('Quantity')
    plt.title('Best selling products')
    plt.show()

def sales_graph(daily_sales_list,weekly_sales_list,monthly_sales_list,yearly_sales_list,best_selling_products_list):    
    option  = (input('Enter the graph you want to see:\n\n1 - Daily sales\n2 - Weekly sales\n3 - Monthly sales\n4 - Yearly sales\n5 - Best selling products\n-->'))
    if option == '1':
        daily_sales_list_graph(daily_sales_list)
    elif option == '2':
        weekly_sales_graph(weekly_sales_list)
    elif option == '3':
        monthly_sales_graph(monthly_sales_list)
    elif option == '4':
        yearly_sales_graph(yearly_sales_list)
    elif option == '5':
        best_selling_products_graph(best_selling_products_list)
    else:
        print('Invalid option')
        
'''----------------------------------PAYMENT GRAPHS----------------------------------'''
        
def daily_payments_graph(daily_payments_list): 
    '''Muestra los pagos diarios en un gráfico'''
    x = []
    y = []
    for payment in daily_payments_list:
        x.append(payment.payment_date)
        y.append(len(daily_payments_list))
    plt.bar(x,y)
    plt.xlabel('Date')
    plt.ylabel('Payments')
    plt.title('Daily payments')
    plt.show()
    
def weekly_payments_graph(weekly_payments_list):
    '''Muestra los pagos semanales en un gráfico'''
    x = []
    y = []
    for payment in weekly_payments_list:
        x.append(payment.payment_date)
        y.append(len(weekly_payments_list))
    plt.bar(x,y)
    plt.xlabel('Date')
    plt.ylabel('Payments')
    plt.title('Weekly payments')
    plt.show()
    
def monthly_payments_graph(monthly_payments_list): 
    '''Muestra los pagos mensuales en un gráfico'''
    x = []
    y = []
    for payment in monthly_payments_list:
        x.append(payment.payment_date)
        y.append(len(monthly_payments_list))
    plt.bar(x,y)
    plt.xlabel('Date')
    plt.ylabel('Payments')
    plt.title('Monthly payments')
    plt.show()
    
def yearly_payments_graph(yearly_payments_list): 
    '''Muestra los pagos anuales en un gráfico'''
    x = []
    y = []
    for payment in yearly_payments_list:
        x.append(payment.payment_date)
        y.append(len(yearly_payments_list))
    plt.bar(x,y)
    plt.xlabel('Date')
    plt.ylabel('Payments')
    plt.title('Yearly payments')
    plt.show()
    
def customers_with_pending_payments_graph(customers_with_pending_payments):
    '''Muestra los clientes con pagos pendientes en un gráfico'''
    x = []
    y = []
    for customer in customers_with_pending_payments:
        x.append(customer.status)
        y.append(len(customers_with_pending_payments))
    plt.bar(x,y)
    plt.xlabel('Customer')
    plt.ylabel('Payments')
    plt.title('Customers with pending payments')
    plt.show()
    
def payments_graph(daily_payments_list, weekly_payments_list, monthly_payments_list, yearly_payments_list, pending_payments):
    option  = (input('Enter the graph you want to see:\n\n1 - Daily payments\n2 - Weekly payments\n3 - Monthly payments\n4 - Yearly payments\n5 - Customers with pending payments\n-->'))
    if option == '1':
        daily_payments_graph(daily_payments_list)
    elif option == '2':
        weekly_payments_graph(weekly_payments_list)
    elif option == '3':
        monthly_payments_graph(monthly_payments_list)
    elif option == '4':
        yearly_payments_graph(yearly_payments_list)
    elif option == '5':
        customers_with_pending_payments_graph(pending_payments)
    else:
        print('Invalid option')
        
        
'''----------------------------------SHIPPINGS GRAPHS----------------------------------'''
        
        
def daily_shipments_graph(daily_shipments_list): 
    '''Muestra los envíos diarios en un gráfico'''
    x = []
    y = []
    for shipment in daily_shipments_list:
        x.append(shipment.date)
        y.append(len(daily_shipments_list))
    plt.bar(x,y)
    plt.xlabel('Date')
    plt.ylabel('Shipments')
    plt.title('Daily shipments')
    plt.show()
    
def weekly_shipments_graph(weekly_shipments_list): 
    '''Muestra los envíos semanales en un gráfico'''
    x = []
    y = []
    for shipment in weekly_shipments_list:
        x.append(shipment.date)
        y.append(len(weekly_shipments_list))
    plt.bar(x,y)
    plt.xlabel('Date')
    plt.ylabel('Shipments')
    plt.title('Weekly shipments')
    plt.show()

def monthly_shipments_graph(monthly_shipments_list): 
    '''Muestra los envíos mensuales en un gráfico'''
    x = []
    y = []
    for shipment in monthly_shipments_list:
        x.append(shipment.date)
        y.append(len(monthly_shipments_list))
    plt.bar(x,y)
    plt.xlabel('Date')
    plt.ylabel('Shipments')
    plt.title('Monthly shipments')
    plt.show()

def yearly_shipments_graph(yearly_shipments_list): 
    '''Muestra los envíos anuales en un gráfico'''
    x = []
    y = []
    for shipment in yearly_shipments_list:
        x.append(shipment.date)
        y.append(len(yearly_shipments_list))
    plt.bar(x,y)
    plt.xlabel('Date')
    plt.ylabel('Shipments')
    plt.title('Yearly shipments')
    plt.show()

def pending_shipments_graph(pending_shipments_list): 
    '''Muestra los envíos pendientes en un gráfico'''
    x = []
    y = []
    for shipment in pending_shipments_list:
        x.append(shipment.date)
        y.append(len(pending_shipments_list))
    plt.bar(x,y)
    plt.xlabel('Date')
    plt.ylabel('Shipments')
    plt.title('Pending shipments')
    plt.show()

def shipments_graph(daily_shipments_list,weekly_shipments_list,monthly_shipments_list,yearly_shipments_list,pending_shipments_list):
    option  = (input('Enter the graph you want to see:\n\n1 - Daily shipments\n2 - Weekly shipments\n3 - Monthly shipments\n4 - Yearly shipments\n5 - Pending shipments\n-->'))
    if option == '1':
        daily_shipments_graph(daily_shipments_list)
    elif option == '2':
        weekly_shipments_graph(weekly_shipments_list)
    elif option == '3':
        monthly_shipments_graph(monthly_shipments_list)
    elif option == '4':
        yearly_shipments_graph(yearly_shipments_list)
    elif option == '5':
        pending_shipments_graph(pending_shipments_list)
    else:
        print('Invalid option')

        