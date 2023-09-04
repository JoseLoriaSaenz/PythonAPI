from flask import Flask, request, jsonify

PORT = 8080

app = Flask(__name__)

@app.route("/")
def home():
    response = "<h1>Home</h1><h2>Python API using Flask</h2><h3>routes</h3>"
    response = response + "<ul><li>GET: /user/6</li><li>POST: /user </li></ul>"
    return response

@app.route("/user/<id>")
def get_user(id):
    user_data = {
        "id": id,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }

    extra = request.args.get("extra")

    if extra:
        user_data["extra"] = extra

    return jsonify(user_data), 200


@app.route('/user/', methods=["POST"])
def create_user():

    if request.method == "POST":
        data = request.get_json()

    return jsonify(data), 201


if __name__ == "__main__":
    app.run(debug=True, port=PORT)