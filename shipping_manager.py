from sale_manager import *
from shipping import Shipping, MRW, Zoom, Delivery
import json
from file_helper import *

def load_shippings(shipping_list): 
    '''Carga los envios a la lista de envios'''
    if not is_file_empty('shippings.txt'):
        f = open('shippings.txt', 'r')
        listS = json.loads(f.read())
        for shipping in listS:
            shipping_list.append(Shipping(shipping['order'],shipping['shipping_service'],shipping['fee'],shipping['client'],shipping['date'],shipping['status']))
        f.close()

def add_shipping(shipping_list,sale_list): 
    '''Agrega un envio a la lista de envios'''
    for index,sale in enumerate(sale_list):
        print('Choose the sale you want to create a receipt of:\n\n')
        try:
            print(f'---------- {index+1} ----------\nCustomer: {sale.client.name}\nProduct/s: {sale.product.name}\nQuantity: {sale.product_quantity}\nPayment Method: {sale.payment_method}\nShipping Method: {sale.shipping_method}\nDate: {sale.date}\n')
        except:
            print(f'---------- {index+1} ----------\nCustomer: {sale.client["name"]}\nProduct/s: {sale.product["name"]}\nQuantity: {sale.product_quantity}\nPayment Method: {sale.payment_method}\nShipping Method: {sale.shipping_method}\nDate: {sale.date}\n')
        
    while True:
        select_sale = int(input('Choose the sale you want to add a shipping: '))
        if select_sale > len(sale_list) or select_sale < 1:
            print('Invalid sale number')
        else:
            break
    if sale_list[select_sale-1].shipping_method == 'MRW': #Determina el metodo de envio de la venta y le asigna el costo del envio
        while True:
            status = (input('Enter the status of the shipping:\n1 - Delivered\n2 - Pending\n')) #Se le pide al usuario que ingrese el estado del envio
            if status == '1':
                status = 'Delivered'
                break
            elif status == '2':
                status = 'Pending'
                break
            else:
                print('Enter a valid option')
        print('\nThe shipping fee for MRW is 7$\n')
        print('shipping added successfully\n')
        try:
            order = f'Product/s{sale_list[select_sale-1].product["name"]}\nQta:{sale_list[select_sale-1].product_quantity}'
        except:
            order = f'Product/s{sale_list[select_sale-1].product.name}\nQta:{sale_list[select_sale-1].product_quantity}'
        shipping_list.append(MRW(order,sale_list[select_sale-1].client,sale_list[select_sale-1].date,status))
    elif sale_list[select_sale-1].shipping_method == 'Zoom':
        while True:
            status = (input('Enter the status of the shipping:\n1 - Delivered\n2 - Pending\n')) #Se le pide al usuario que ingrese el estado del envio
            if status == '1':
                status = 'Delivered'
                break
            elif status == '2':
                status = 'Pending'
                break
            else:
                print('Enter a valid option')
        print('\nThe shipping fee for Zoom is 10$\n')
        print('shipping added successfully\n')
        try:
            order = f'Product/s{sale_list[select_sale-1].product["name"]}\nQta:{sale_list[select_sale-1].product_quantity}'
        except:
            order = f'Product/s{sale_list[select_sale-1].product.name}\nQta:{sale_list[select_sale-1].product_quantity}'
        shipping_list.append(Zoom(order,sale_list[select_sale-1].client,sale_list[select_sale-1].date,status))
    elif sale_list[select_sale-1].shipping_method == 'Delivery':
        while True:
            status = (input('Enter the status of the shipping:\n1 - Delivered\n2 - Pending\n')) #Se le pide al usuario que ingrese el estado del envio
            if status == '1':
                status = 'Delivered'
                break
            elif status == '2':
                status = 'Pending'
                break
            else:
                print('Enter a valid option')
        print('\nThe shipping fee Delivery is 4$\n')
        delivery_name = input('Enter the name of the person who will deliver the product: ').title() #Se piden los datos del repartidor
        while True:
            delivery_phone = input('Enter the phone number of the person who will deliver the product: ')
            if len(delivery_phone) != 11:
                print('Enter a valid phone number')
            else:
                break
        delivery_plate = input('Enter the plate of the bike that will deliver the product: ')
        delivery_info = {'name':delivery_name,'phone':delivery_phone,'plate':delivery_plate}
        print('\nshipping added successfully')
        try:
            order = f'Product/s{sale_list[select_sale-1].product["name"]}\nQta:{sale_list[select_sale-1].product_quantity}'
        except:
            order = f'Product/s{sale_list[select_sale-1].product.name}\nQta:{sale_list[select_sale-1].product_quantity}'
        shipping_list.append(Delivery(order,sale_list[select_sale-1].client,sale_list[select_sale-1].date,delivery_info,status))
    
    
    return shipping_list
    


def search_shipping(shipping_list): 
    '''Busca un envio en la lista de envios por nombre del cliente o fecha'''
    search = input('Enter the name of the client or the date you want to search: ')
    for index,shipping in enumerate(shipping_list):
        try:
            if shipping.client["name"] == search or shipping.date == search:
                print(f'---------- {index+1} ----------\nOrder: {shipping.order}\nShipping Method: {shipping.shipping_service}\nDate: {shipping.date}\nStatus: {shipping.status}\n')
            else:
                print('No shipping found')
                break
        except:
            if shipping.client.name == search or shipping.date == search:
                print(f'---------- {index+1} ----------\nOrder: {shipping.order}\nShipping Method: {shipping.shipping_service}\nDate: {shipping.date}\nStatus: {shipping.status}\n')
            else:
                print('No shipping found')
                break
            
def save_shippings(shipping_list): 
    '''Guarda los envios en el archivo shippings.txt'''
    with open('shippings.txt', 'w') as f:
        json.dump(shipping_list, f, cls=CustomEncoder)
    f.close()