

items = {
    "Name": ['Cebula','Marchew','Pietruszka'],
    "Quantity": [40,50,20],
    "Unit": ['kg','kg','kg'],
    "Unit Price (PLN)": [2.3, 4.1, 5]
    }

def get_items(product):
    headers = ""
    for item in product:
        headers += f"|{item:10}|" + '\t'
    print(headers)

    for i in range(0, len(product.values())-1):
        for key in product.keys():
            print(f"|{product[key][i]:10}|", end='\t')
        print('')

def add_items(name, unit_name, quantity, unit_price):
    for key, value in items.items():
        if key == "Name":
            value.append(name)
        elif key == "Quantity":
            value.append(quantity)
        elif key == "Unit":
            value.append(unit_name)
        elif key == "Unit Price (PLN)":
            value.append(unit_price)
    print("")
    print('Obency stan magazynu')
    print('')
    headers = ""
    for item in items:
         headers += f"|{item:10}|" + '\t'
    print(headers)

    for i in range(0, len(items.values())):
        for key in items.keys():
             print(f"|{items[key][i]:10}|", end='\t')
        print('')
       
while True:
    print('')
    operation = input("What you want to do: 'show' 'add', or type 'exit' to exit the program: ")
    if operation == 'exit':
        print("Koniec operacji...BYE!!!")
        break
    elif operation == "show":
        results = get_items(items)
    elif operation == "add":
        name = input('Podaj nazwę towaru: ')
        unit_name = input('Podaj jednostkę np. kg, l ?: ')
        quantity = int(input('Podaj ilość: '))
        unit_price = float(input('Podaj cenę jednostkową: '))
        results = add_items(name, unit_name, quantity, unit_price)
        

