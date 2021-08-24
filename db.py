import sys,  os, sqlite3
from contextlib import closing
from objects import Category, Product

conn = None
def connect():    
    global conn    
    if not conn:        
        DB_FILE = "C:\\Users\\tbels\\OneDrive\\Documents\\SDCCE\\Python for DB\\DBs_for_SQLite\\Final_Project\\fitness_shop.sqlite"        
        conn = sqlite3.connect(DB_FILE)        
        conn.row_factory = sqlite3.Row

def make_category(row):    
    return Category(row["categoryID"], row["categoryName"])

def make_product(row):    
    return Product(row["productID"], row["productCode"], row["productName"], row["listPrice"],            
    make_category(row))

def get_categories():    
    query = '''SELECT categoryID, categoryName FROM Category'''    
    with closing(conn.cursor()) as c:        
        c.execute(query)        
        results = c.fetchall()    
    
    categories = {}    
    for row in results:
        #print("TEST",row['categoryID'],row['categoryName'])
        #categories.append(make_category(row))#ORG
        categories[row["categoryID"]] = row["categoryName"]
    return categories

def get_products_by_category(category_name):
    # query = '''SELECT productID, productCode, productName, listPrice,
    #                   Product.categoryID as categoryID, categoryName
    #            FROM Product
    #            INNER JOIN Category ON Product.categoryID = Category.categoryID
    #            WHERE categoryName = ?
    #            ORDER BY productName'''

    # UNEXLAINED: listPrice IS ACTUALLY PRODUCT CODE; productName IS ACTUALLY PRICE
    query = '''
            SELECT productID, productCode, productName, listPrice, Product.categoryID as categoryID, categoryName
            FROM Product
            INNER JOIN Category ON Category.categoryID = Product.categoryID
            WHERE Category.categoryID = ? 
            ORDER BY productName ASC
            '''

    with closing(conn.cursor()) as c:
        c.execute(query, (category_name,))
        results = c.fetchall()
    #print(len(results))
    products = {}
    for row in results:
        products[row['productID']] = (row['productCode'], row['productName'], row['listPrice'])
    return products

def update_product(code, price):
    # RECOMMEND: NAMED VARIABLE FOR PRODUCT CODE
    sql = '''
    UPDATE Product 
    SET listPrice = ?
    WHERE productCode LIKE "%'''+code+'%"'

    #print(sql,code,price)
    with closing(conn.cursor()) as c:
        #c.execute(sql)
        c.execute(sql, (price,))
        conn.commit()

def main():
    connect()
    update_product('duane', '100.03')

def close():
    if conn:
        conn.close()

if __name__ == "__main__":
    main()