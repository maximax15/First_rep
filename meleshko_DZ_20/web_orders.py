from flask import Flask, render_template, request, make_response, jsonify, redirect
from db.model_orders import get_orders, create_order, delete_order, get_order, update_order

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def res():
    if request.method == 'GET':
        list_orders = get_orders()
        return render_template('index_orders.html', orders=list_orders)
    create_order(
        name=request.form.get('name'),
        cost=request.form.get('cost'),
        client_id=request.form.get('client_id')
    )
    return redirect('/')


@app.route('/delete/<id>', methods=['DELETE'])
def function_for_delete_from_html(id):
    delete_order(int(id))
    return redirect('/')


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def function_for_update(id):
    if request.method == 'GET':
        order = get_order(id)
        return render_template('index_update.html', order=order)
    elif request.method == 'POST' and request.form.get('_method') == 'PUT':
        id = id
        name = request.form.get('name')
        cost = request.form.get('cost')
        client_id = request.form.get('client_id')
        update_order(id, name, cost, client_id)

        return redirect('/')


if __name__ == '__main__':
    app.run()
