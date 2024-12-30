from flask import Flask, render_template,request

app = Flask(__name__)
products =[{"id":1,"price":2,"desc":"pizza"},{"id":2,"price":12,"desc":"milk"}]

# R - read
@app.route("/", methods=['GET'])
def prods():
    return render_template("index.html",my_products=products)

# C - Create
@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == "GET":
        return render_template("add.html")
    else: #POST
        # when sending with axios (json)
        data = request.get_json()
        price = data.get('price')
        desc = data.get('desc')
        # print(title)
        products.append({"id": len(products)+1, "price": price,"desc":desc},)
        return render_template("index.html",my_products=products)
    
# D - delete
@app.route("/del/<id>" ,methods=['GET', 'DELETE'])
def delete_product(id=0):
    # print(id * 2)
    product_to_remove = next((product for product in products if product["id"] == int(id)), None)
    if product_to_remove: products.remove(product_to_remove)
    return "" # render_template("index.html",my_products=products)

# U - update
@app.route("/upd/<id>" ,methods=['GET',"PUT"])
def upd_product(id=0):
    product_to_update = next((product for product in products if product["id"] == int(id)), None)
    data = request.get_json()
    price = data.get('price')
    desc = data.get('desc')

    if product_to_update:
        product_to_update["price"] =price
        product_to_update["desc"] =desc
 
    return render_template("index.html",my_products=products)