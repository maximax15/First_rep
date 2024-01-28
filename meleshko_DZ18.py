from flask import Flask

app = Flask(__name__)


var = 0

@app.route('/', methods=['GET'])
def get_var():
    return str(var)

@app.route('/plus', methods=['POST'])
def plus():
    global var
    var += 1
    return str(var)

@app.route('/minus', methods=['POST'])
def minus():
    global var
    var -= 1
    return str(var)

if __name__ == '__main__':
    app.run()

