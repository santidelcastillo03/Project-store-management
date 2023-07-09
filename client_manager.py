from client import Client
from file_helper import *
import json

def load_clients(client_list): 
    '''Carga los clientes a la lista de clientes'''
    if not is_file_empty('clients.txt'):
        f = open('clients.txt', 'r')
        listC = json.loads(f.read())
        for client in listC:
            client_list.append(Client(client['name'],client['client_type'],client['id'],client['email'],client['shipping_address'],client['phone_number']))
        f.close()
    

def show_clients(client_list): 
    '''Muestra la lista de clientes'''
    for index,client in enumerate(client_list):
        print(f'---------- {index+1} ----------\nName: {client.name}\nCustomer type: {client.client_type}\nID: {client.id}\nEmail: {client.email}\nShipping address: {client.shipping_address}\nPhone number: {client.phone_number}\n')

def add_client(client_list): 
    '''agrega un cliente a la lista de clientes'''
    name = input('Enter the full name or social reason of the customer: ').title()  
    while True:
        client_type = (input('Enter the Customer Type:\n1 - Natural\n2 - Legal\n--> '))
        if client_type == '1':
            client_type = 'Natural'
            break
        elif client_type == '2':
            client_type = 'Legal'
            break
        else:
            print('Invalid customer type. Please enter 1 or 2')
    id = input('ID or RIF of the customer: ')
    while True:
        email = input('Email of the customer: ')
        if  '@' and '.' not in email:
            print('Invalid email. Please enter a valid email')
        else:
            break        
    shipping_address = input('Shipping address of the customer: ')
    while True:
        phone_number = input('Phone number of the customer: ')
        if len(phone_number) != 11:
            print('Enter a valid phone number')
        else:
            break    
    client_list.append(Client(name,client_type,id,email,shipping_address,phone_number))
    print('Customer added successfully')
    
    return client_list

def modify_client(client_list): 
    '''modifica un atributo del cliente de la lista de clientes'''
    show_clients(client_list)
    client_index = int(input('Enter the customer number you want to modify: '))
    client_mod = (input('Enter the data you want to change:\n1 - Name\n2 - Customer type\n3 - ID\n4 - Email\n5 - Shipping address\n6 - Phone number\n--> '))
    if client_mod == '1':
        name = input('Enter the full name or social reason of the customer: ').title()
        client_list[client_index-1].name = name
        print('Customer modified successfully')
    elif client_mod == '2':
        while True:
            client_type = (input('Enter the Customer Type:\n1 - Natural\n2 - Legal\n--> '))
            if client_type == '1':
                client_type = 'Natural'
                break
            elif client_type == '2':
                client_type = 'Legal'
                break
            else:
                print('Invalid customer type. Please enter 1 or 2')
        client_list[client_index-1].client_type = client_type
        print('Customer modified successfully')
    elif client_mod == '3':
        id = input('Enter ID or RIF of the customer: ')
        client_list[client_index-1].id = id
        print('Customer modified successfully')
    elif client_mod == '4':
        while True:
            email = input('Email of the customer: ')
            if  '@' and '.' not in email:
                print('Enter a valid email')
            else:
                break
        client_list[client_index-1].email = email
        print('Customer modified successfully')
    elif client_mod == '5':
        shipping_address = input('Enter shipping address of the customer: ')
        client_list[client_index-1].shipping_address = shipping_address
        print('Customer modified successfully')
    elif client_mod == '6':
        while True:
            phone_number = input('Enter phone number of the customer: ')
            if len(phone_number) != 11:
                print('Enter a valid phone number')
            else:
                break
        client_list[client_index].phone_number = phone_number
        print('Customer modified successfully')
    else:
        print('Invalid option')
        
    return client_list

def remove_client(client_list): 
    '''elimina un cliente de la lista de clientes'''
    show_clients(client_list)
    while True:
        client_index = int(input('Enter the number of the customer you want to delete: '))
        if client_index > len(client_list):
            print('Invalid customer number. Please enter a valid number')
        else:
            client_list.pop(client_index)
            print('The client has been successfully removed')
            break
    
    return client_list

def search_client(client_list): 
    '''busca un cliente en la lista de clientes a base de su id o email'''
    search = input('Enter the ID or email of the customer: ')
    for index,client in enumerate(client_list):
        if search == client.id or search == client.email:
            print(f'---------- {index+1} ----------\nName: {client.name}\nCustomer type: {client.client_type}\nID: {client.id}\nEmail: {client.email}\nShipping address: {client.shipping_address}\nPhone number: {client.phone_number}\n')
        else:
            print('Customer not found')
            
def save_clients(client_list): 
    '''guarda los clientes en el archivo clients.txt'''
    with open('clients.txt', 'w') as f:
        json.dump(client_list, f, cls=CustomEncoder)
    f.close()

