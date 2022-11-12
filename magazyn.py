

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

def add_items():
        name = input('Podaj nazwę towaru: ')
        unit_name = ('Podaj jednostkę np. kg, l ?: ')
        quantity = ('Podaj ilość: ')
        unit_price = ('Podaj cenę jednostkową: ')

       
while True:
    print('')
    operation = input("What you want to do: 'show' 'add', or type 'exit' to exit the program: ")
    if operation == 'exit':
        print("Koniec operacji...BYE!!!")
        break
    elif operation == "show":
        results = get_items(items)
    elif operation == "add":
        results = add_items()
