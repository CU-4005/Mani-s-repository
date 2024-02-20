import paho.mqtt.client as mqtt

# Callback when the client receives a CONNACK response from the server
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
        # Subscribe to the "wavestrack" topic upon successful connection
        client.subscribe("wavestrack")
    else:
        print(f"Connection failed with code {rc}")

# Callback when a message is received from the subscribed topic
def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()} on topic {msg.topic}")

# Create an MQTT client instance
client = mqtt.Client()

# Set callback functions
client.on_connect = on_connect
client.on_message = on_message

# Set the MQTT broker address and port (replace with your broker's information)
broker_address = "192.168.1.100"  # Replace with the actual IP address of your broker
port = 1883

# Connect to the broker
client.connect(broker_address, port, 60)

# Start the MQTT loop (this function blocks and will run forever)
client.loop_forever()