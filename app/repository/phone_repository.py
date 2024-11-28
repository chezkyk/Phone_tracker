class PhoneTracker:
    def __init__(self, driver):
        self.driver = driver

    def create_phone_tracker(self, data):
        devices = data.get("devices", [])
        interaction = data.get("interaction", {})

        query_create_device = """
            MERGE (d:Device {id: $id})
            SET d.name = $name,
                d.brand = $brand,
                d.model = $model,
                d.os = $os,
                d.latitude = $latitude,
                d.longitude = $longitude,
                d.altitude_meters = $altitude,
                d.accuracy_meters = $accuracy
        """

        query_create_interaction = """
            MATCH (from:Device {id: $from_device_id}), (to:Device {id: $to_device_id})
            MERGE (from)-[r:CONNECTED {
                method: $method,
                bluetooth_version: $bluetooth_version,
                signal_strength_dbm: $signal_strength,
                distance_meters: $distance,
                duration_seconds: $duration,
                timestamp: $timestamp
            }]->(to)
        """

        with self.driver.session() as session:
            for device in devices:
                device_params = {
                    "id": device["id"],
                    "name": device["name"],
                    "brand": device["brand"],
                    "model": device["model"],
                    "os": device["os"],
                    "latitude": device["location"]["latitude"],
                    "longitude": device["location"]["longitude"],
                    "altitude": device["location"]["altitude_meters"],
                    "accuracy": device["location"]["accuracy_meters"],
                }

                session.run(query_create_device, device_params)

            if interaction:
                interaction_params = {
                    "from_device_id": interaction["from_device"],
                    "to_device_id": interaction["to_device"],
                    "method": interaction["method"],
                    "bluetooth_version": interaction["bluetooth_version"],
                    "signal_strength": interaction["signal_strength_dbm"],
                    "distance": interaction["distance_meters"],
                    "duration": interaction["duration_seconds"],
                    "timestamp": interaction["timestamp"],
                }

                session.run(query_create_interaction, interaction_params)

    def get_all_bluetooth_connections(self):
        with self.driver.session() as session:
            query = """
            MATCH path = (d1:Device)-[r:CONNECTED {method: 'Bluetooth'}]->(d2:Device)
            RETURN 
                d1.id AS from_device, 
                d2.id AS to_device, 
                length(path) AS path_length
            """
            result = session.run(query)
            return [
                {
                    "from_device": record["from_device"],
                    "to_device": record["to_device"],
                    "path_length": record["path_length"]
                } for record in result
            ]