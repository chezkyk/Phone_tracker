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

@phone_bp.route("/get-all-devices-with-strength-stronger-than_60", methods=['GET'])
def get_all_devices_with_strength_stronger_than_60():
    tracker = PhoneTracker(neo4j_driver)
    connections = tracker.get_all_devices_strength_stronger_than_60()
    return jsonify({"connections": connections}), 200

@phone_bp.route("/get-count-of-all-devices-connected-to-device-by-id/<device_id>", methods=['GET'])
def get_count_of_all_devices_connected_to_device_by_id(device_id):
    tracker = PhoneTracker(neo4j_driver)
    count = tracker.count_device_connections(device_id)
    return jsonify({"device_id": device_id, "connection_count": count}), 200

@phone_bp.route("/get-info-on-direct-connection-between-two-devices", methods=['GET'])
def get_info_on_direct_connection_between_two_devices():
    device_id1 = request.args.get("device_id1")
    device_id2 = request.args.get("device_id2")
    if not device_id1 or not device_id2:
        return jsonify({"error": "Both device IDs are required"}), 400
    tracker = PhoneTracker(neo4j_driver)
    as_direct_connection = tracker.get_info_on_direct_connection(device_id1,device_id2)
    return jsonify({
        "device1": device_id1,
        "device2": device_id2,
        "is_connected": as_direct_connection
    }), 200


@phone_bp.route("/get-recent-info-for-device-sorted-by-timestamp", methods=['GET'])
def get_recent_info_for_device_sorted_by_timestamp():
    tracker = PhoneTracker(neo4j_driver)
    connections = tracker.get_recent_info_sorted_by_timestamp()
    return jsonify({"connections": connections}), 200

