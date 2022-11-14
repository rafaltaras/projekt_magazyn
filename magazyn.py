

items = [
    {
        "name": "cebula",
        "quantity": 40,
        "unit": "kg",
        "unit_price": 2.3
    },
    {
        "name": "marchew",
        "quantity": 50,
        "unit": "kg",
        "unit_price": 4.1
    },
    {
        "name": "pietruszka",
        "quantity": 20,
        "unit": "kg",
        "unit_price": 5
    }
]

def get_items(items):
        for item in items[0]:
            print(f"|{item:10}|", end='\t')
        print(end='\n')
                   
        for item in items:
            for value in item.values():
                print(f"|{value:10}|", end='\t')
            print(end='\n')

def add_items(name, unit_name, quantity, unit_price):
        new_item = {
            "name": name,
            "quantity": quantity,
            "unit": unit_name,
            "unit_price": unit_price
            }
        items.append(new_item)    


def sell_items(name, quantity):
    for item in items:
        if item.get('name') == name:
            current_quantity = item.get("quantity")
            after_sale = current_quantity - quantity
            #Dodaj do słwonika

       
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
        name = input('Jaki towar sprzedajemy: ')
        quantity = int(input("Ile sprzedajemy: "))
        sell_items(name,quantity)
                



