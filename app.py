from flask import Flask, jsonify,request
import json

app=Flask(__name__)

#The json file importing 
def load_products():
    with open('product.json','r+',encoding='utf-8') as file:
        return json.load(file)
    
def write_products(products):
    with open('product.json',mode='w',encoding='utf-8') as file:
        return json.dump(products,file,indent=4)

@app.route('/',methods=['GET'])
def sample():
    return "Hello Devs"

#The product data gets
@app.route('/api/products',methods=['GET'])
def products():
    data=load_products()
    return jsonify(data)

# product data gets through id
@app.route('/api/products/<int:products_id>', methods=['GET'])
def get_products_id(products_id):
    products = load_products()
    product = None
    for p in products:
        if p['id'] == products_id:
            product = p
            break
    return jsonify(product) if product else ({"message": "product not found"}, 404)

#Add data into file
@app.route('/api/products',methods=['POST'])
def insert_data():
    new_product= request.json
    products=load_products()
    products.append(new_product)
    write_products(products)
    return new_product

#Edit data in that file 
@app.route('/api/products/<int:product_id>',methods=['PUT'])
def edit_data(product_id):
    products=load_products()
    product=None
    for p in products:
        if p['id']== product_id:
            product=p
            break
    
    new_product_data= request.json
    product.update(new_product_data)
    write_products(products)
    return new_product_data

#Deleting datas
@app.route('/api/products/<int:product_id>',methods=['DELETE'])
def remove_data(product_id):
    products=load_products()
    updated_list =  [p for p in products if p.get('id') != product_id]
    write_products(updated_list)
    return 'Deleted sucesfully',204


#The app run
app.run(debug=True)

