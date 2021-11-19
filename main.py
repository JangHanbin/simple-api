from flask import Flask, request, jsonify

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


users = {'hanbin':'01012345678', 'muldae': '01043218765'}

@app.route('/phone', methods=['GET', 'POST'])
def search():

    name = request.args.get('name')
    number = users.get(name) # it can be replaced by number = users.get(request.args.get('name'))

    if not number:
        return jsonify({'result':False, 'data':None})
    else:
        return jsonify({'result': True, 'data': number})



@app.route('/', methods=['GET','POST'])
def index():
    return 'Hello World!'


if __name__=='__main__':
    app.config.from_object(__name__)
    app.config['SECRET_KEY'] = 'tnarudhkTejsskdml~'
    app.run('0.0.0.0', port=1994, debug=True)
