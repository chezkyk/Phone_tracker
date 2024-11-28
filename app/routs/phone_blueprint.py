from flask import Blueprint,request,jsonify

phone_bp = Blueprint('phone blueprint',__name__)

@phone_bp.route("/api/phone_tracker", methods=['POST'])
def get_interaction():
   print(request.json)
   return jsonify({ }), 200

