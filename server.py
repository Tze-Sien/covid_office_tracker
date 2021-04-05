from flask import Flask
from flask import request
import controllers 
app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to The Backend API - Second Testing'

# ------- User Routes ------- #

@app.route('/user/signup', methods=['POST'])
def signup(): 
    data = request.json
    res = controllers.signup(data)
    # return res


@app.route('/user/signin', methods=['POST'])
def signin():
    data = request.json
    res = controllers.signin(data)
    return res

@app.route('/user/checkin', methods=['POST'])
def checkin():
    data = request.json
    res = controllers.checkin(data)
    return res


# ------- Admin Routes ------- #

@app.route('/admin/login', methods=['POST'])
def adlogin():
    data = request.json
    res = controllers.adlogin(data)
    return res
    
# ------- Admin > Alert ------- #

@app.route('/admin/alert/update', methods=['POST'])
def alert():
    data = request.json
    res = controllers.alert(data)
    return res

# ------- Admin > Dashboard ------- #

@app.route('/admin/dashboard/alert', methods=['POST'])
def dbalert():
    data = request.json
    res = controllers.dbalert(data)
    return res


@app.route('/admin/dashboard/amount', methods=['POST'])
def dbamount():
    data = request.json
    res = controllers.dbamount(data)
    return res

# ------- Extra Check In Function ------- #
@app.route('/<department>/<record_id>', methods=['GET'])
def doorcheck(department, record_id):
    res = controllers.doorcheck(department, record_id)
    return res

if __name__ == "__main__":
    app.run(debug=True)