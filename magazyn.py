

items = {
    "Name": ['Cebula','Marchew','Pietruszka'],
    "Quantity": [40,50,20],
    "Unit": ['kg','kg','kg'],
    "Unit Price (PLN)": [2.3, 4.1, 5]
    }

def get_items(product):
    headers = ""
    for item in product:
        headers += item + '\t\t'
    print(headers)

    for i in range(0, len(product.values())-1):
        for key in product.keys():
            print(product[key][i], end='\t\t')
        print('')
       
while True:
    print('')
    operation = input("Please enter 'show', or type 'exit' to exit the program: ")
    if operation == 'exit':
        print("Koniec operacji...BYE!!!")
        break
    elif operation == "show":
        results = get_items(items)
        

