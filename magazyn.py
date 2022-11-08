

items = {
    "Name": ['Cebula','Marchew','Pietruszka'],
    "Quantity": [40,50,20],
    "Unit": ['kg','kg','kg'],
    "Unit Price (PLN)": [2.3, 4.1, 5]
    }


def get_items(towar):
    naglowek = ""
    for item in towar:
        naglowek += item + '\t'
    return naglowek


while True:
    operation = input("Please enter 'show', or type 'exit' to exit the program: ")
    if operation == 'exit':
        print("Koniec operacji...BYE!!!")
        break
    elif operation == "show":
        results = get_items(items)
        print(results)
        print('----''\t''-------''\t')

