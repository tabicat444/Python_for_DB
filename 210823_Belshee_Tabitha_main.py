import db
from objects import Product
from tabulate import tabulate


def display_title():
    print("Product Manager")
    print()    

def display_categories():
    categories = db.get_categories()
    print("CATEGORIES:")
    for key,value in categories.items():
        print(key,value, sep=". ")
    print("\n")
    

def display_menu():
    print("COMMAND MENU:")
    print("view   - View products by category")
    print("update - Update product price")
    print("exit   - Exit program")
    print()    

def display_products_by_category():
    #display_categories()

    catid = int(input("Category ID: ")) #integer
    if catid > 0 and catid < 4:
        #print("display: ", catid)
        #print("Code", "Name".rjust(10), "Price".rjust(30)) #Format later
        print("-"*60)
        #query product 
        # SELECT * from priducts where catid = catid
        # innerjoin from category to products
        content = db.get_products_by_category(catid)
        print(tabulate(content.values(), headers=["Code", "Name", "Price"]))
        print("\n")
        #for item in content.values():
         #   print("{: >0} {: >20} {: >20}".format(*item))
            #print(item[0], item[1].rjust(10), str(item[2]).rjust(30)) #format better
    else: 
        print("Not a valid category number, please try again.")

    #pass:
        #category_name = 
        #products =

def update_product():
    code =  input("Product Code: ")
    price = float(input("New product price: "))
    db.update_product(code, price)
    print("Product updated.\n")
        
def main():
    db.connect()
    display_title()
    display_categories()
    display_menu()
    while True:        
        command = input("Command: ").lower()
        if command == "view":
            display_products_by_category()
        elif command == "update":
            update_product()
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
            display_menu()
    db.close()
    print("Bye!")

if __name__ == "__main__":
    main()