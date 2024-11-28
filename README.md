# Phone Tracker Project

## Overview
The **Phone Tracker Project** allows you to monitor device connections, signal strengths, and connection details through a series of API endpoints. The project uses Docker for easy deployment and includes a dispatcher program for inserting values into the system.

---

## How to Run the Project

### 1. Open the Terminal

#### Navigate to the `app` directory:
```bash
cd ./app/
```
#### Then activate the docker-compose file
```bash
docker-compose up
```

### 2. Run the Main File
#### Execute the phone dispatcher program to insert values into the system.

### 3. Run the next endpoints

1.  finding all devices connected to each other using the Bluetooth method, and how long is the path.

`GET` [http://localhost:5000/api/get-all-devices-connecting-by-bluetooth]()

#### response

{
`    "connections": [
        {
            "from_device": "54f1345b-6818-48bc-b089-1e853e8333f5",
            "path_length": 9,
            "to_device": "a3bdcce1-3187-41d7-a318-d8b27019ec07"
        }
    ]
}`

***

2. find all devices connected to each other with a signal strength stronger than -60.

`GET` [http://localhost:5000/get-all-devices-with-strength-stronger-than_60]()

#### response

`{
    "connections": 
    [
        {
            "from_device": "a48c3f89-46b0-4d85-b11b-629dcf27f8e2",
            "signal_strength": -36,
            "to_device": "d65ce20f-c8e1-445f-ae39-7836cb025d82"
        },
        {
            "from_device": "0535f950-daed-4dfb-be50-f57acb67f669",
            "signal_strength": -41,
            "to_device": "ec5aff4a-ba4c-4b1b-abf3-7b16a4bda848"
        }
    ]
}`

***

3. count how many devices are connected to a specific device based on a provided ID
`GET` [http://localhost:5000/get-count-of-all-devices-connected-to-device-by-id/62d3227d-4590-44b9-a226-e57bafd15d77http://localhost:5000/get-count-of-all-devices-connected-to-device-by-id/62d3227d-4590-44b9-a226-e57bafd15d77]()

#### response

`{
    "connection_count": 3,
    "device_id": "62d3227d-4590-44b9-a226-e57bafd15d77"
}`
***

4. determine whether there is a direct connection between two devices.
`GET` [http://localhost:5000/get-info-on-direct-connection-between-two-devices?device_id1=d6e56d41-ed64-4239-946e-c15801aaef95&device_id2=5def8ac3-b7cc-4d09-87bc-4ad6fefa1426]()

#### response

`{
    "device1": "d6e56d41-ed64-4239-946e-c15801aaef95",
    "device2": "5def8ac3-b7cc-4d09-87bc-4ad6fefa1426",
    "is_connected": true
}`
***

5. fetch the most recent interaction for a specific device, sorted by timestamp.
`GET` [http://localhost:5000/get-recent-info-for-device-sorted-by-timestamp/5def8ac3-b7cc-4d09-87bc-4ad6fefa1426]()

#### response

`{
    "connections": {
        "bluetooth_version": "5.0",
        "connected_device": "a48c3f89-46b0-4d85-b11b-629dcf27f8e2",
        "distance": 7.82,
        "duration": 136,
        "method": "WiFi",
        "signal_strength": -73,
        "timestamp": "2018-11-02T04:55:58"
    }
}`

# The end ( :
