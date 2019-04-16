# views.py
# Orientation to Web Page

from flask import render_template, redirect, request
from app.__init__ import app
from app.sql import SQL_Server

global table
global username
global password

@app.route('/')
def welcome():
    """root panel"""
    return render_template('welcome.html')

@app.route('/login')
def loginPanel():
    """show login information"""
    return render_template('login.html')

@app.route('/register')
def registerPanel():
    """register user information"""
    return render_template('register.html')

@app.route('/register/result', methods=['GET', 'POST'])
def registerResult():
    """show register result"""
    username = request.form['username']
    password = request.form['password']
    sql = SQL_Server()
    # try to insert (username, password) into USERTABLE
    result = sql.register(username, password)
    return render_template('register_result.html', username=username, password=password, result=result)

@app.route('/role', methods=['GET', 'POST'])
def role():
    """developer or user"""
    global username, password
    username = request.form['username']
    password = request.form['password']
    sql = SQL_Server()
    if not sql.loginDetect(username, password):
        return redirect('/login')
    return render_template('role.html', user=username)

@app.route('/developer', methods=['GET', 'POST'])
def developerPanel():
    """detect developer's password"""
    # if (username password) not correct
    global username, password
    sql = SQL_Server()
    sql.getTableList()
    sql.getAttributeList()
    tableList = sql.tableList
    attributeList = sql.attributeList
    # else login succeed
    return render_template('developer.html', user=username, tableList=tableList, attributeList=attributeList, tableLen=len(tableList))

@app.route('/developer/select', methods=['GET', 'POST'])
def selectPanel():
    """detect the table which is to be selected"""
    global table
    table = request.form['table']
    sql = SQL_Server()
    # detect if the table is in db
    if not sql.tableDetect(table):
        # exceptions.BadRequestKeyError here
        return redirect('/developer')
    attributeList = sql.getAttributeListOfTable(table)
    return render_template('developer_select.html', table=table, attributeList=attributeList, attributeLen=len(attributeList))

@app.route('/developer/select/result', methods=['GET', 'POST'])
def selectResult():
    """show select option result"""
    global table
    attribute = request.form['attribute']
    sql = SQL_Server()
    results = sql.selectFromTable(table, attribute)
    attributeList = sql.getAttributeListForSelectShow(table, attribute)
    if len(results) != 0:
        col = len(results[0])
    else:
        col = 0
    return render_template('developer_select_result.html', table=table, attributeList=attributeList, results=results, attribute=attribute, row=len(results), col=col)

@app.route('/developer/insert', methods=['GET', 'POST'])
def insertPanel():
    """detect the table which is to be inserted"""
    global table
    table = request.form['table']
    sql = SQL_Server()
    # detect if the table is in db
    if not sql.tableDetect(table):
        # exceptions.BadRequestKeyError here
        return redirect('/developer')
    attribute = '*'
    results = sql.selectFromTable(table, attribute)
    attributeList = sql.getAttributeListOfTable(table)
    if len(results) != 0:
        col = len(results[0])
    else:
        col = 0
    return render_template('developer_insert.html', table=table, attributeList=attributeList, results=results, attribute=attribute, row=len(results), col=col, attributeLen=len(attributeList))

@app.route('/developer/insert/result', methods=['GET', 'POST'])
def insertResult():
    """show result after insertion"""
    global table
    attribute = '*'
    sql = SQL_Server()
    insertSQL = request.form['insertSQL']
    # do insertion
    SF = sql.insertIntoTable(table, insertSQL)
    results = sql.selectFromTable(table, attribute)
    attributeList = sql.getAttributeListForSelectShow(table, attribute)
    if len(results) != 0:
        col = len(results[0])
    else:
        col = 0
    return render_template('developer_insert_result.html', table=table, attributeList=attributeList, results=results, attribute=attribute, row=len(results), col=col, SF=SF)

@app.route('/developer/delete', methods=['GET', 'POST'])
def deletePanel():
    """detect the table which is to be inserted"""
    global table
    table = request.form['table']
    sql = SQL_Server()
    # detect if the table is in db
    if not sql.tableDetect(table):
        # exceptions.BadRequestKeyError here
        return redirect('/developer')
    attribute = '*'
    results = sql.selectFromTable(table, attribute)
    attributeList = sql.getAttributeListOfTable(table)
    if len(results) != 0:
        col = len(results[0])
    else:
        col = 0
    return render_template('developer_delete.html', table=table, attributeList=attributeList, results=results, attribute=attribute, row=len(results), col=col, attributeLen=len(attributeList))

@app.route('/developer/delete/result', methods=['GET', 'POST'])
def deleteResult():
    """show result after deletion"""
    global table
    attribute = '*'
    sql = SQL_Server()
    deleteSQL = request.form['deleteSQL']
    # do deletion
    SF = sql.deleteFromUserTable(table, deleteSQL)
    results = sql.selectFromTable(table, attribute)
    attributeList = sql.getAttributeListForSelectShow(table, attribute)
    if len(results) != 0:
        col = len(results[0])
    else:
        col = 0
    return render_template('developer_delete_result.html', table=table, attributeList=attributeList, results=results, attribute=attribute, row=len(results), col=col, SF=SF)

@app.route('/developer/drop', methods=['GET', 'POST'])
def dropPanel():
    """detect the table which is to be inserted"""
    table = request.form['table']
    sql = SQL_Server()
    # detect if the table is in db
    if not sql.tableDetect(table):
        # exceptions.BadRequestKeyError here
        return redirect('/developer')
    SF = sql.dropTable(table)
    return render_template('developer_drop.html', table=table, SF=SF)

@app.route('/user', methods=['GET', 'POST'])
def userPanel():
    global username, password
    sql =  SQL_Server()
    sql.getTableList()
    sql.getAttributeList()
    tableList = sql.tableList
    attributeList = sql.attributeList
    wsList = sql.getWorkshopID()
    whList = sql.getWarehouseID()
    partList = sql.getPartID()
    return render_template('user.html', user=username, tableList=tableList, attributeList=attributeList, tableLen=len(tableList), wsListLen=len(wsList), wsList=wsList, whListLen=len(whList), whList=whList, partListLen=len(partList), partList=partList)

@app.route('/user/view', methods=['GET', 'POST'])
def viewPanel():
    """detect the table which is to be selected"""
    global table
    table = request.form['table']
    sql = SQL_Server()
    # detect if the table is in db
    if not sql.tableDetect(table):
        # exceptions.BadRequestKeyError here
        return redirect('/user')
    attributeList = sql.getAttributeListOfTable(table)
    return render_template('user_view.html', table=table, attributeList=attributeList, attributeLen=len(attributeList))

@app.route('/user/view/result', methods=['GET', 'POST'])
def viewResult():
    """show view option result"""
    global table
    attribute = request.form['attribute']
    sql = SQL_Server()
    results = sql.selectFromTable(table, attribute)
    attributeList = sql.getAttributeListForSelectShow(table, attribute)
    if len(results) != 0:
        col = len(results[0])
    else:
        col = 0
    return render_template('user_view_result.html', table=table, attributeList=attributeList, results=results, attribute=attribute, row=len(results), col=col)

@app.route('/user/parts', methods=['GET', 'POST'])
def produceParts():
    """Workshops produce parts and store them in warehouses"""
    part_id = request.form['part_id']
    weight = request.form['weight']
    price = request.form['price']
    warehouse_id = request.form['warehouse_id']
    workshop_id = request.form['workshop_id']
    sql = SQL_Server()
    SF = sql.produceParts(part_id, weight, price, warehouse_id, workshop_id)
    table = 'MAKE'
    attribute = '*'
    results = sql.selectFromTable(table, attribute)
    attributeList = sql.getAttributeListForSelectShow(table, attribute)
    if len(results) != 0:
        col = len(results[0])
    else:
        col = 0
    return render_template('produce_parts_result.html', table=table, attributeList=attributeList, results=results, attribute=attribute, row=len(results), col=col, SF=SF)

@app.route('/user/products', methods=['GET', 'POST'])
def assembleProducts():
    """Assemble parts to generate products and store them in warehouse"""
    product_id = request.form['product_id']
    class_ = request.form['class']
    price = request.form['price']
    part_id = request.form['part_id']
    warehouse_id = request.form['warehouse_id']
    sql = SQL_Server()
    SF = sql.assembleProducts(product_id, class_, price, part_id, warehouse_id)
    table = 'ASSEMBLE'
    attribute = '*'
    results = sql.selectFromTable(table, attribute)
    attributeList = sql.getAttributeListForSelectShow(table, attribute)
    if len(results) != 0:
        col = len(results[0])
    else:
        col = 0
    return render_template('assemble_products_result.html', table=table, attributeList=attributeList, results=results, attribute=attribute, row=len(results), col=col, SF=SF)

@app.route('/user/state', methods=['GET', 'POST'])
def checkState():
    """Check the number of workers, warehouses, workshops, parts and products in each factory"""
    sql = SQL_Server()
    results = sql.checkState()
    row = len(results)
    col = len(results[0])
    attributeList = ['factory_name', 'worker_num', 'warehouse_num', 'workshop_num', 'part_num', 'product_num']
    return render_template('state.html', attributeList=attributeList, results=results, row=row, col=col)
    