from flask import Flask, request, render_template, jsonify
from flask_socketio import SocketIO
from db_model import Db
import json
import datetime

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/", methods=["GET"])
def root():
    return render_template("index.html", users_list=Db().fetch_records())

@app.route("/notify_login/", methods=["POST"])
def get_user():
    req_json = request.get_json()
    # get request data
    # we can build a user model here
    user_name = json.dumps(req_json["user_name"]).replace('\"', '')
    login_type = json.dumps(req_json["login_type"]).replace('\"', '')

    # insert record
    last_row = Db().insert_new(user_name=user_name, login_type=login_type)
    user = Db().fetch_record(last_row)

    # emit data to client
    socketio.emit('user_login_action', json.dumps(user, default=datatime_converter), broadcast=True)
    return jsonify({'status': 201})

def datatime_converter(d):
    if isinstance(d, datetime.datetime):
        return d.__str__()


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)

app = Flask(__name__)
