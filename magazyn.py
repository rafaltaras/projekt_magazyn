

items = {
    "Name": ['Cebula','Marchew','Pietruszka'],
    "Quantity": [40,50,20],
    "Unit": ['kg','kg','kg'],
    "Unit Price (PLN)": [2.3, 4.1, 5]
    }

# items["Name"].append("Pomidor")
# x = items["Name"]
# print(x)

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
    global items
    items["Name"].append(name)
    items["Quantity"].append(quantity)
    items["Unit"].append(unit_name)
    items["Unit Price (PLN)"].append(unit_price)
    


def sell_items(name, quantity):
    return
       
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
    elif operation == "sell":
        name = input('Co sprzedajemy: ')
        if name in items["Name"]:
             print("Jest")
        else:
            print("Brak w magazynie")

