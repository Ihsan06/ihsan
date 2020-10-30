from flask import request, jsonify, render_template
from . import app, db
from app.models import Sales, SalesSchema, sale_schema, sales_schema
import psycopg2
import psycopg2.extras

#cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

# Home Endpoint definieren
@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

# Post Sales
@app.route('/api/sales', methods=['POST'])
def post_sales():
    id = request.json['id']
    filnr = request.json['filnr']
    artnr = request.json['artnr']
    discount = request.json['discount']
    date = request.json['date']
    amount = request.json['amount']

    new_sales = Sales(id, filnr, artnr, discount, date, amount)

    db.session.add(new_sales)
    db.session.commit()

    return sale_schema.jsonify(new_sales)

# Get alle Sales
@app.route('/api/employee/all', methods=['GET'])
@app.route('/api/employee/all/<int:page>', methods=['GET'])
def get_sales(page=1):
    per_page = 100
    all_sales = Sales.query.paginate(page, per_page, error_out = False)
    result = sales_schema.dump(all_sales.items)
    return jsonify(result)

# Get all Unique Entries
@app.route('/api/employee/<unique>', methods=['GET'])
def get_unique(unique):
    unique_entries = db.session.query(Sales).distinct(unique)
    unique_schema = SalesSchema(only=(str(unique),), many=True)
    return unique_schema.jsonify(unique_entries)

# Get einzelnen Sale
@app.route('/api/sales/id/<id>', methods=['GET'])
def get_sale(id):
    sale = Sales.query.get(id)
    return sale_schema.jsonify(sale)

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

# Filter verschiedene Parameter
@app.route('/api/employee', methods=['GET'])
#@app.route('/sales/<int:page>', methods=['GET'])
def filter():
    query_parameters = request.args

    #per_page = 50
    #query_parameters = parameters.paginate(page, per_page, error_out = False)

    id = query_parameters.get('id')
    filnr = query_parameters.get('filnr')
    artnr = query_parameters.get('artnr')
    discount = query_parameters.get('discount')
    date = query_parameters.get('date')
    amount = query_parameters.get('amount')

    query = "SELECT * FROM sales WHERE"
    to_filter = []

    if id:
        query += ' id=%s AND'
        to_filter.append(id)
    if filnr:
        query += ' filnr=%s AND'
        to_filter.append(filnr)
    if artnr:
        query += ' artnr=%s AND'
        to_filter.append(artnr)
    if discount:
        query += ' discount=%s AND'
        to_filter.append(discount)
    if date:
        query += ' date=%s AND'
        to_filter.append(date)
    if amount:
        query += ' amount=%s AND'
        to_filter.append(amount)    
    if not (id or filnr or artnr or discount or date or amount):
        return page_not_found(404)

    query = query[:-4] + ';'

    #engine = create_engine("postgresql://postgres:level3@localhost/webers")
    #conn = engine.raw_connection()
    #conn = psycopg2.connect("postgresql://postgres:hallolevel3@localhost/webers")

    conn=psycopg2.connect(dbname='webers', user='postgres', host='microservice-architecture-master_db_1', password='password', port=5432)
    conn.autocommit=True
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute(query, to_filter)

    results = cur.fetchall()
    cur.close()
    #connection = engine.connect()
    #results = connection.execute(query, to_filter)

    return jsonify(results)

# Update Sale
@app.route('/sales/<id>', methods=['PUT'])
def update_sales(id):
    sale = Sales.query.get(id)

    filnr = request.json['filnr']
    artnr = request.json['artnr']
    discount = request.json['discount']
    date = request.json['date']
    amount = request.json['amount']

    sale.filnr = filnr
    sale.artnr = artnr
    sale.discount = discount
    sale.date = date
    sale.amount = amount

    db.session.commit()

    return sale_schema.jsonify(sale)

# Delete Sale
@app.route('/sales/<id>', methods=['DELETE'])
def delete_sale(id):
    sale = Sales.query.get(id)

    db.session.delete(sale)
    db.session.commit()
    
    return sale_schema.jsonify(sale)

# Api Endpoint definieren
#@app.route('/api',methods=['POST'])
#def api():
 #   data = request.get_json(force=True)
 #   prediction = model.predict([np.array(list(data.values()))])
 #   output = prediction[0]

 #   return jsonify(output)