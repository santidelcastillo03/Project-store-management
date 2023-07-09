from sale import Sale
from product_manager import *
from payment_manager import *
from shipping_manager import *
from client_manager import *
from datetime import datetime
from file_helper import *
import json


currentDateAndTime = datetime.today()
currentTime = currentDateAndTime.strftime('%H:%M:%S')

def load_sales(sale_list): 
    '''Carga las ventas a la lista de ventas'''
    if not is_file_empty('sales.txt'):
        f = open('sales.txt', 'r')
        listS = json.loads(f.read())
        for sale in listS:
            sale_list.append(Sale(sale['client'],sale['product'],sale['product_quantity'],sale['payment_method'],sale['shipping_method'],sale['purchase_breakdown'],sale['date']))
        f.close()
        
def add_sale(sale_list,client_list,product_list): 
    '''Agrega una venta a la lista de ventas'''
    show_clients(client_list) #Muestra la lista de clientes para que el usuario pueda elegir uno
    while True:
        select_client = int(input('Select customer: '))
        if select_client > len(client_list) or select_client < 1:
            print('Invalid client number')
        else:
            break
    while True:
        show_products(product_list)
        while True:
            select_product = int(input('Select product: '))
            if select_product > len(product_list) or select_product < 1:
                print('Invalid product number')
            else:
                break
        select_quantity = int(input('Select quantity: '))
        x = input('Do you want to add another product? (y/n): ').upper() #Pregunta si el usuario quiere agregar otro producto
        if x == 'Y':
            continue
        elif x == 'N':
            break
        else:
            print('Invalid option. Please, choose a valid option')
    while True:
        select_payment_method = (input('Enter the payment method:\n\n1 - Cash\n2 - PdV\n3 - Zelle\n4 - Pago Movil\n\n-->'))
        if select_payment_method == '1':
            select_payment_method = 'Cash'
            break
        elif select_payment_method == '2':
            select_payment_method = 'PdV'
            break
        elif select_payment_method == '3':
            select_payment_method = 'Zelle'
            break
        elif select_payment_method == '4':
            select_payment_method = 'Pago Movil'
            break
        else:
            print('Invalid option. Please, choose a valid option')
    while True:
        select_shipping_method = (input('Enter the shipping method:\n\n1 - MRW\n2 - Zoom\n3 - Delivery\n\n-->'))
        if select_shipping_method == '1':
            select_shipping_method = 'MRW'
            break
        elif select_shipping_method == '2':
            select_shipping_method = 'Zoom'
            break
        elif select_shipping_method == '3':
            select_shipping_method = 'Delivery'
            break
        else:
            print('Invalid option. Please, choose a valid option')
    select_date = datetime.today() #Fecha de la venta
    string_date = select_date.strftime('%d/%m/%Y')
    subtotal = product_list[select_product-1].price * select_quantity #Subtotal de la venta
    if client_list[select_client-1].client_type == 'Legal': #Determina si el cliente es juridico, si lo es, le aplica un descuento del 5%
        discount =  0.05
    else:
        discount = 0
    if select_payment_method == 'Cash' or select_payment_method == 'Zelle': #Determina si el metodo de pago es cash o zelle, si lo es, le aplica IGTF del 3%
        igtf =  0.03
    else:
        igtf = 0
    if select_shipping_method == 'MRW':
        shipping_fee =  7
    elif select_shipping_method == 'Zoom':
        shipping_fee =  10
    elif select_shipping_method == 'Delivery':
        shipping_fee = 4
    iva = 0.16 #IVA del 16%
    subtotal_discount = subtotal - (subtotal * discount)
    total = subtotal_discount + (subtotal_discount * igtf) + (subtotal_discount * iva) #Total de la venta
    total_shipping = total + shipping_fee #Total de la venta con el costo del envio
    purchase_breakdown = f'Subtotal: {subtotal}\nDiscount: {subtotal*discount}\nIGTF: {subtotal_discount*igtf}\n IVA: {subtotal_discount*iva}\nTotal: {total}\nTotal with shipping fee: {total_shipping}'
    print('Sale added successfully') 
    sale_list.append(Sale(client_list[select_client-1],product_list[select_product-1],select_quantity,select_payment_method,select_shipping_method,purchase_breakdown,string_date))
    

def generate_receipt(sale_list): 
    '''Genera la factura de la venta'''
    for index,sale in enumerate(sale_list):
        print('Choose the sale you want to create a receipt of:\n\n')
        try:
            print(f'---------- {index+1} ----------\nCustomer: {sale.client.name}\nProduct/s: {sale.product.name}\nQuantity: {sale.product_quantity}\nPayment Method: {sale.payment_method}\nShipping Method: {sale.shipping_method}\nDate: {sale.date}\n')
        except:
            print(f'---------- {index+1} ----------\nCustomer: {sale.client["name"]}\nProduct/s: {sale.product["name"]}\nQuantity: {sale.product_quantity}\nPayment Method: {sale.payment_method}\nShipping Method: {sale.shipping_method}\nDate: {sale.date}\n')
        
    while True:
        select_sale = int(input('Select sale: '))
        if select_sale > len(sale_list) or select_sale < 1:
            print('Invalid sale number')
        else:
            break
    try:
        if sale_list[select_sale-1].client["client_type"] == 'Legal': #Determina si el cliente es juridico, si lo es, puede pagar en 15 o 30 dias
            while True:
                option = int(input('\n\n1 - Pay in full\n2 - Pay within 15 or 30 days'))
                if option == 1:
                    print(f'\n\nNatural product store\n{datetime.today()}\n\n---------------------------------\n\n{sale.product["name"]} - {sale.product["price"]}\nQta: {sale.product_quantity}\nShipping service: {sale.shipping_method}\n\n---------------------------------\n\nPurchase method: {sale.payment_method}\nPurchase breakdown:\n\n{sale.purchase_breakdown}\n\n---------------------------------\n\nThank you for your purchase!\n\n---------------------------------\n\n{sale_list[select_sale-1].client["name"]}\n{sale_list[select_sale-1].client["shipping_address"]}\n{sale_list[select_sale-1].client["phone_number"]}\n{sale_list[select_sale-1].client["email"]}\n\n')
                    break
                elif option == 2:
                    print(f'\n\nNatural product store\n{datetime.today()}\n\n---------------------------------\n\n{sale.product["name"]} - {sale.product["price"]}\nQta: {sale.product_quantity}\nShipping service: {sale.shipping_method}\n\n---------------------------------\n\nPurchase method: {sale.payment_method}\nPurchase breakdown:\n\n{sale.purchase_breakdown}\n\n---------------------------------\n\nThank you for your purchase!\n\n---------------------------------\n\nYou can pay within 15 or 30 days\n\n---------------------------------\n\n{sale_list[select_sale-1].client["name"]}\n{sale_list[select_sale-1].client["shipping_address"]}\n{sale_list[select_sale-1].client["phone_number"]}\n{sale_list[select_sale-1].client["email"]}\n\n')
                    break
                else:
                    print('Invalid option. Please, choose a valid option')
        else:
            print(f'\n\nNatural product store\n{datetime.today()}\n\n---------------------------------\n\n{sale.product["name"]} - {sale.product["price"]}\nQta: {sale.product_quantity}\nShipping service: {sale.shipping_method}\n\n---------------------------------\n\nPurchase method: {sale.payment_method}\nPurchase breakdown:\n\n{sale.purchase_breakdown}\n\n---------------------------------\n\nThank you for your purchase!\n\n---------------------------------\n\n{sale_list[select_sale-1].client["name"]}\n{sale_list[select_sale-1].client["shipping_address"]}\n{sale_list[select_sale-1].client["phone_number"]}\n{sale_list[select_sale-1].client["email"]}\n\n')
    except:
        if sale_list[select_sale-1].client.client_type == 'Legal': #Determina si el cliente es juridico, si lo es, puede pagar en 15 o 30 dias
            while True:
                option = int(input('\n\n1 - Pay in full\n2 - Pay within 15 or 30 days'))
                if option == 1:
                    print(f'\n\nNatural product store\n{datetime.today()}\n\n---------------------------------\n\n{sale.product.name} - {sale.product.price}\nQta: {sale.product_quantity}\nShipping service: {sale.shipping_method}\n\n---------------------------------\n\nPurchase method: {sale.payment_method}\nPurchase breakdown:\n\n{sale.purchase_breakdown}\n\n---------------------------------\n\nThank you for your purchase!\n\n---------------------------------\n\n{sale_list[select_sale-1].client.name}\n{sale_list[select_sale-1].client.shipping_address}\n{sale_list[select_sale-1].client.phone_number}\n{sale_list[select_sale-1].client.email}\n\n')
                    break
                elif option == 2:
                    print(f'\n\nNatural product store\n{datetime.today()}\n\n---------------------------------\n\n{sale.product.name} - {sale.product.price}\nQta: {sale.product_quantity}\nShipping service: {sale.shipping_method}\n\n---------------------------------\n\nPurchase method: {sale.payment_method}\nPurchase breakdown:\n\n{sale.purchase_breakdown}\n\n---------------------------------\n\nThank you for your purchase!\n\n---------------------------------\n\n{sale_list[select_sale-1].client.name}\n{sale_list[select_sale-1].client.shipping_address}\n{sale_list[select_sale-1].client.phone_number}\n{sale_list[select_sale-1].client.email}\n\n')
                    break
                else:
                    print('Invalid option. Please, choose a valid option')
        else:
            print(f'\n\nNatural product store\n{datetime.today()}\n\n---------------------------------\n\n{sale.product.name} - {sale.product.price}\nQta: {sale.product_quantity}\nShipping service: {sale.shipping_method}\n\n---------------------------------\n\nPurchase method: {sale.payment_method}\nPurchase breakdown:\n\n{sale.purchase_breakdown}\n\n---------------------------------\n\nThank you for your purchase!\n\n---------------------------------\n\n{sale_list[select_sale-1].client.name}\n{sale_list[select_sale-1].client.shipping_address}\n{sale_list[select_sale-1].client.phone_number}\n{sale_list[select_sale-1].client.email}\n\n')
    
def search_sale(sale_list): 
    '''Busca una venta por nombre del cliente, fecha o monto total de la venta'''
    search = input('Enter the name of the customer, date, or total amount of the sale to search: ')
    for index,sale in enumerate(sale_list):
        if search in sale.client["name"] or search in sale.purchase_breakdown or search in sale.date:
            print(f'---------- {index+1} ----------\nCustomer: {sale.client["name"]}\nProduct/s: {sale.product["name"]}\nQuantity: {sale.product_quantity}\nPayment Method: {sale.payment_method}\nShipping Method: {sale.shipping_method}\nDate: {sale.date}\n')
        else:
            print('No sale found')
            break
            
        
def show_sales(sale_list): 
    '''Muestra todas las ventas'''
    for index,sale in enumerate(sale_list):
        print(f'---------- {index+1} ----------\nCustomer: {sale.client["name"]}\nProduct/s: {sale.product["name"]}\nQuantity: {sale.product_quantity}\nPayment Method: {sale.payment_method}\nShipping Method: {sale.shipping_method}\nDate: {sale.date}\n')
        
def save_sales(sale_list): 
    '''Guarda las ventas en un archivo .txt'''
    with open('sales.txt', 'w') as f:
        json.dump(sale_list, f, cls=CustomEncoder)
    f.close()