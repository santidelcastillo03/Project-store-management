from client_manager import *
from product_manager import *
from payment_manager import *
from sale_manager import *
from shipping_manager import *
from statisticss import *
import datetime
import json
from file_helper import *

def main():
    
    client_list = [] #Lista de clientes
    product_list = [] #Lista de productos
    payment_list = [] #Lista de pagos
    sale_list = [] #Lista de ventas
    shipping_list = [] #Lista de envios
    daily_sales_list = [] #Lista de ventas diarias
    weekly_sales_list = [] #Lista de ventas semanales
    monthly_sales_list = [] #Lista de ventas mensuales
    yearly_sales_list = [] #Lista de ventas anuales
    best_selling_products_list = [] #Lista de productos mas vendidos
    most_frequent_customers_list = [] #Lista de clientes mas frecuentes
    daily_payments_list = [] #Lista de pagos diarios
    weekly_payments_list = [] #Lista de pagos semanales
    monthly_payments_list = [] #Lista de pagos mensuales
    yearly_payments_list = [] #Lista de pagos anuales
    pending_payments = [] #Lista de pagos pendientes
    daily_shipments_list = [] #Lista de envios diarios
    weekly_shipments_list = [] #Lista de envios semanales
    monthly_shipments_list = [] #Lista de envios mensuales
    yearly_shipments_list = [] #Lista de envios anuales
    most_shipped_products_list = [] #Lista de productos mas enviados
    pending_shipments_list = [] #Lista de envios pendientes
    load_products(product_list) #Carga los productos del json 
    load_clients(client_list) #Carga los clientes
    load_sales(sale_list) #Carga las ventas 
    load_payments(payment_list) #Carga los pagos 
    load_shippings(shipping_list) #Carga los envios 
    
    print('\n\n----------------------------------WELCOME TO THE NATURAL PRODUCTS STORE MANAGEMENT SYSTEM \U0001F33F----------------------------------\n\n') #Menu principal del programa. EL\U0001F33F es un emoji de una hoja
    while True: 
        option = (input('Choose an option:\n\n1 - Manage products\n2 - Manage customers\n3 - Manage sales\n4 - Manage payments\n5 - Manage shipping\n6 - See statistics\n7 - Save & Exit\n\n--> '))
        if option == '1':
            print('\n\n----------------------------------PRODUCT MANAGEMENT----------------------------------\n\n') #Menu de productos
            product_option = (input('Choose an option:\n\n1 - Show products\n2 - Add product\n3 - Modify product\n4 - Search product\n5 - Remove product\n\n--> '))
            if product_option == '1':
                show_products(product_list)
            elif product_option == '2':
                add_product(product_list)
            elif product_option == '3':
                modify_product(product_list)
            elif product_option == '4':
                search_product(product_list)
            elif product_option == '5':
                remove_product(product_list)
            else:
                print('Invalid option. Please, choose a valid option')
            
        elif option == '2':
            print('\n\n----------------------------------CUSTOMER MANAGEMENT----------------------------------\n\n') #Menu de clientes
            client_option = (input('Choose an option:\n\n1 - Show customer\n2 - Add customer\n3 - Modify customer\n4 - Search customer\n5 - Remove customer\n\n--> '))
            if client_option == '1':
                show_clients(client_list)
            elif client_option == '2':
                add_client(client_list)
            elif client_option == '3':
                modify_client(client_list)
            elif client_option == '4':
                search_client(client_list)
            elif client_option == '5':
                remove_client(client_list)
            elif client_option == '6':
                break
            else:
                print('Invalid option. Please, choose a valid option')
        elif option == '3':
            print('\n\n----------------------------------SALES MANAGEMENT----------------------------------\n\n') #Menu de ventas
            sale_option = (input("Choose an option:\n\n\n1 - Add sale\n2 - Search sale\n3 - Generate receipt\n\n--> "))
            if sale_option == '1':
                add_sale(sale_list,client_list,product_list)
            elif sale_option == '2':
                search_sale(sale_list)
            elif sale_option == '3':
                generate_receipt(sale_list)
            else:
                print('Invalid option. Please, choose a valid option')
                
        elif option == '4':
            print('\n\n----------------------------------PAYMENT MANAGEMENT----------------------------------\n\n') #Menu de pagos
            payment_option = (input('Choose an option:\n\n1 - Show payments\n2 - Add payment\n3 - Search payment\n\n--> '))
            if payment_option == '1':
                show_payments(payment_list)
            elif payment_option == '2':
                add_payment(payment_list,sale_list)
            elif payment_option == '3':
                search_payment(payment_list)
            else:
                print('Invalid option. Please, choose a valid option')
        elif option == '5':
            print('\n\n----------------------------------SHIPPING MANAGEMENT----------------------------------\n\n') #Menu de envios
            shipping_option = (input('Choose an option:\n\n1 - Add shipping\n2 - Search shipping\n\n--> '))
            if shipping_option == '1':
                add_shipping(shipping_list,sale_list)
            elif shipping_option == '2':
                search_shipping(shipping_list)       
            else:
                print('Invalid option. Please, choose a valid option')
        elif option == '6':
            print('\n\n----------------------------------STATISTICS----------------------------------\n\n') #Menu de estadisticas
            statistics_option = (input('Choose an option:\n\n1 - Show sales statistics\n2 - Show payments statistics\n3 - Show shipping statistics\n\nBEFORE PRESSING ANY GRAPH OPTION, PRESS SHOW STATISTICS, SO IT CAN BE SEEN IN THE GRAPHS\n\n4 - Show sales graphs\n5 - Show payments graphs\n6 - Show shipping graphs\n\n--> '))
            if statistics_option == '1':
                sales_report(sale_list,daily_sales_list,weekly_sales_list,monthly_sales_list,yearly_sales_list,best_selling_products_list,most_frequent_customers_list)
            elif statistics_option == '2':
                payments_report(payment_list,daily_payments_list,weekly_payments_list,monthly_payments_list,yearly_payments_list,pending_payments)
            elif statistics_option == '3':
                shipments_report(shipping_list,daily_shipments_list,weekly_shipments_list,monthly_shipments_list,yearly_shipments_list,most_shipped_products_list,pending_shipments_list)
            elif statistics_option == '4':
                sales_graph(daily_sales_list,weekly_sales_list,monthly_sales_list,yearly_sales_list,best_selling_products_list)
            elif statistics_option == '5':
                payments_graph(daily_payments_list,weekly_payments_list,monthly_payments_list,yearly_payments_list,pending_payments)
            elif statistics_option == '6':
                shipments_graph(daily_shipments_list,weekly_shipments_list,monthly_shipments_list,yearly_shipments_list,pending_shipments_list)
            else:
                print('Invalid option. Please, choose a valid option')
        elif option == '7': #Opcion para salir del programa y guarda los datos
            save_products(product_list)
            save_sales(sale_list)
            save_clients(client_list)
            save_payments(payment_list)
            save_shippings(shipping_list)
            break
        else:
            print('Invalid option. Please, choose a valid option')
main()