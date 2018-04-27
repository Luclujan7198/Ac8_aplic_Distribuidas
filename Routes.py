from flask import jsanify, request
from server import App, Response

@App.route("/forum", methods=["GET"])

@App.route("/forum", methods=["POST"])
def postForum():
    from services.postForum import postForum

    Dados = request.get_json()
    postForum()
    return jsonify(Response)
@App.route("/forum/<Id>", methods=["GET"])

@App.route("/forum/inactivate", methods=["POST"])

@App.route("/forum/activate", methods=["POST"])

@App.route("/forum/register", methods=["POST"])

@App.route("/forum/unregister", methods=["POST"])

@App.route("/forum/<Id>/post", methods=["GET"])

@App.route("/forum/post", methods=["POST"])

@App.route("/forum/post/<Id>", methods=["GET"])
