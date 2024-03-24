import paho.mqtt.client as mqtt
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
        
        client.subscribe("wavestrack")
    else:
        print(f"Connection failed with code {rc}")
def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()} on topic {msg.topic}")

client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

broker_address = "mqtt.eclipseprojects.io" 
port = 1883

client.connect(broker_address, port, 60)
client.loop_forever()