from flask import Blueprint,request,jsonify

from app.database.db_connection import neo4j_driver
from app.repository.phone_repository import PhoneTracker

phone_bp = Blueprint('phone blueprint',__name__)

@phone_bp.route("/api/phone_tracker", methods=['POST'])
def get_interaction():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    interaction = data.get("interaction", {})
    if interaction:
        from_device_id = interaction.get("from_device")
        to_device_id = interaction.get("to_device")

        if from_device_id == to_device_id:
            return jsonify({"error": "The phone is calling itself."}), 400

    tracker = PhoneTracker(neo4j_driver)
    tracker.create_phone_tracker(data)

    return jsonify({"status": "success"}), 200




@phone_bp.route("/api/get-all-devices-connecting-by-bluetooth", methods=['GET'])
def get_all_devices_connecting_by_bluetooth():
    tracker = PhoneTracker(neo4j_driver)
    connections = tracker.get_all_bluetooth_connections()
    return jsonify({"connections": connections}), 200

# @phone_bp.route("/", methods=['GET'])
# def get_all_devices_with_strength_stronger_than_60():
#    pass
#
# @phone_bp.route("/", methods=['GET'])
# def get_count_of_all_devices_connected_to_device_by_id(device_id):
#    pass
#
# @phone_bp.route("/", methods=['GET'])
# def get_info_on_direct_connection_between_two_devices():
#    pass
#
# @phone_bp.route("/", methods=['GET'])
# def get_recent_info_for_device_sorted_by_timestamp():
#    pass

