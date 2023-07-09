from sale_manager import *
import datetime
from sale import Sale
from payment import Payment
from file_helper import *
import json

def load_payments(payment_list): 
    '''Carga los pagos a la lista de pagos'''
    if not is_file_empty('payments.txt'):
        f = open('payments.txt', 'r')
        listP = json.loads(f.read())
        for payment in listP:
            payment_list.append(Payment(payment['client'],payment['payment_amount'],payment['payment_currency'],payment['payment_method'],payment['payment_date'],payment['status']))
        f.close()

def add_payment(payment_list,sale_list): 
    '''Agrega un pago a la lista de pagos'''
    for index,sale in enumerate(sale_list):
        print('Choose the sale you want to create a receipt of:\n\n')
        try:
            print(f'---------- {index+1} ----------\nCustomer: {sale.client.name}\nProduct/s: {sale.product.name}\nQuantity: {sale.product_quantity}\nPayment Method: {sale.payment_method}\nShipping Method: {sale.shipping_method}\nDate: {sale.date}\n')
        except:
            print(f'---------- {index+1} ----------\nCustomer: {sale.client["name"]}\nProduct/s: {sale.product["name"]}\nQuantity: {sale.product_quantity}\nPayment Method: {sale.payment_method}\nShipping Method: {sale.shipping_method}\nDate: {sale.date}\n')
        
    while True:    
        select_sale = int(input('Choose the sale you want to add a payment: '))
        if select_sale > len(sale_list) or select_sale < 1:
            print('Invalid sale')
        else:
            break
    while True:
        status = (input('Enter the status of the payment:\n1 - Paid\n2 - Pending\n'))
        if status == '1':
            status = 'Paid'
            break
        elif status == '2':
            status = 'Pending'
            break
        else:
            print('Invalid status')
    try:
        total_amount = sale_list[select_sale-1].product_quantity * sale_list[select_sale-1].product["price"]
    except:
        total_amount = sale_list[select_sale-1].product_quantity * sale_list[select_sale-1].product.price
        
    if sale_list[select_sale-1].payment_method == 'Zelle': #Determina de la lista de ventas que metodo de pago se utilizo y lo agrega a la lista de pagos
        currency = 'USD'
        print('payment added successfully')
        payment_list.append(Payment(sale_list[select_sale-1].client,total_amount,currency,sale_list[select_sale-1].payment_method,sale_list[select_sale-1].date,status))
    elif sale_list[select_sale-1].payment_method == 'PdV':
        currency = 'Bs'
        print('payment added successfully')
        payment_list.append(Payment(sale_list[select_sale-1].client,total_amount,currency,sale_list[select_sale-1].payment_method,sale_list[select_sale-1].date,status))
    elif sale_list[select_sale-1].payment_method == 'Pago Movil':
        currency = 'Bs'
        print('payment added successfully')
        payment_list.append(Payment(sale_list[select_sale-1].client,total_amount,currency,sale_list[select_sale-1].payment_method,sale_list[select_sale-1].date,status))
    elif sale_list[select_sale-1].payment_method == 'Cash':
        currency = 'USD'
        print('payment added successfully')
        payment_list.append(Payment(sale_list[select_sale-1].client,total_amount,currency,sale_list[select_sale-1].payment_method,sale_list[select_sale-1].date,status))
        
    return payment_list

def show_payments(payment_list): 
    '''Muestra los pagos de la lista de pagos'''
    for index,payment in enumerate(payment_list):
        try:
            print(f'---------- {index+1} ----------\nClient: {payment.client["name"]}\nPayment amount: {payment.payment_amount}\nPayment currency: {payment.payment_currency}\nPayment method: {payment.payment_method}\nPayment date: {payment.payment_date}\nStatus: {payment.status}\n')
        except:
            print(f'---------- {index+1} ----------\nClient: {payment.client.name}\nPayment amount: {payment.payment_amount}\nPayment currency: {payment.payment_currency}\nPayment method: {payment.payment_method}\nPayment date: {payment.payment_date}\nStatus: {payment.status}\n')

def search_payment(payment_list): 
    '''Busca un pago en la lista de pagos basado en el filtro de eleccion del usuario'''
    search = input('Enter the name of the customer, date, payment method or payment currency to search: ')
    for index,payment in enumerate(payment_list):  
        try:
            if search in payment.client["name"] or search in str(payment.payment_date) or search in payment.payment_method or search in payment.payment_currency:
                print(f'---------- {index+1} ----------\nClient: {payment.client["name"]}\nPayment amount: {payment.payment_amount}\nPayment currency: {payment.payment_currency}\nPayment method: {payment.payment_method}\nPayment date: {payment.payment_date}\nStatus: {payment.status}\n')
            else:
                print('No results found')
        except:
            if search in payment.client.name or search in str(payment.payment_date) or search in payment.payment_method or search in payment.payment_currency:
                print(f'---------- {index+1} ----------\nClient: {payment.client.name}\nPayment amount: {payment.payment_amount}\nPayment currency: {payment.payment_currency}\nPayment method: {payment.payment_method}\nPayment date: {payment.payment_date}\nStatus: {payment.status}\n')
            else:
                print('No results found')
            
def save_payments(payment_list): 
    '''Guarda los pagos en el archivo payments.txt'''
    with open('payments.txt', 'w') as f:
        json.dump(payment_list, f, cls=CustomEncoder)
    f.close()