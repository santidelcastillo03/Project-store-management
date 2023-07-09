import requests
from product import Product
import json
from file_helper import *

url = 'https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-3/api-proyecto/e20c412e7e1dcc3b089b0594b5a42f30ac15e49b/products.json'
response = requests.get(url)


def load_products(product_list): 
    '''Carga los productos del json en una lista de productos'''
    if is_file_empty('products.txt'):
        for product in response.json():
            product_list.append(Product(product['name'],product['description'],product['price'],product['category']))
    else:
        f = open('products.txt', 'r')
        listP = json.loads(f.read())
        for product in listP:
            product_list.append(Product(product['name'],product['description'],product['price'],product['category']))
        f.close()


def show_products(product_list): 
    '''Muestra los productos de la lista de productos de manera mas legible'''
    for index,product in enumerate(product_list):
        print(f'---------- {index+1} ----------\nName: {product.name}\nDescription: {product.description}\nPrice: {product.price}\nCategory: {product.category}\n')
        
def add_product(product_list): 
    '''Agrega un producto a la lista de productos'''
    name = input('Enter the name of the product: ').title()
    description = input('Enter the description of the product: ')
    price = int(input('Enter the price of the product: '))
    category = input('Enter the category of the product: ').title()
    product_list.append(Product(name,description,price,category))
    print('Product added successfully')

def modify_product(product_list): 
    '''Modifica algun atributo de los productos de la lista de productos'''
    show_products(product_list)
    while True:
        product_index = int(input('Enter the product number you want to modify: '))
        if product_index > len(product_list) or product_index < 1:
            print('Invalid product number')
        else:
            break
    while True:
        product_mod = (input('Enter the data you want to change:\n1 - Name\n2 - Description\n3 - Price\n4 - Category\n--> '))
        if product_mod == '1':
            name = input('Enter the name of the product: ').title()
            product_list[product_index-1].name = name
            print('Product modified successfully')
            break
        elif product_mod == '2':
            description = input('Enter the description of the product: ')
            product_list[product_index-1].description = description
            print('Product modified successfully')
            break
        elif product_mod == '3':
            price = int(input('Enter the price of the product: '))
            product_list[product_index-1].price = price
            print('Product modified successfully')
            break
        elif product_mod == '4':
            category = input('Enter the category of the product: ').title()
            product_list[product_index-1].category = category
            print('Product modified successfully')
            break
        else:
            print('Invalid option')
            

def search_product(product_list): 
    '''Busca en la lista de productos algun producto que coincida con el nombre, categoria o precio ingresado'''
    search = input('Enter the name, category or price of the product you want to search: \n\n').title()
    for index,product in enumerate(product_list):
        if search in product.name or search in product.category or search in str(product.price):
            print(f'---------- {index+1} ----------\nName: {product.name}\nDescription: {product.description}\nPrice: {product.price}\nCategory: {product.category}\n')
        else:
            print('Product not found') 

def remove_product(product_list): 
    '''Elimina un producto de la lista de productos'''
    show_products(product_list)
    while True:
        product_index = int(input('Enter the product number you want to remove: '))
        if product_index > len(product_list) or product_index < 1:
            print('Invalid product number')
        else:
            product_list.pop(product_index-1)
            print('Product removed successfully')
            break
    
def save_products(product_list):
    '''Guarda los productos de la lista de productos en un json'''
    with open('products.txt', 'w') as f:
        json.dump(product_list, f, cls=CustomEncoder)
    f.close()

