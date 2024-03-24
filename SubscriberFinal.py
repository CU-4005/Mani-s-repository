import paho.mqtt.client as mqtt
from tabulate import tabulate

received_messages = []

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")

        client.subscribe("Amplitude")
        client.subscribe("Fuel")
        client.subscribe("Acceleration")
        client.subscribe("Frequency")
    else:
        print(f"Connection failed with code {rc}")


def on_message(client, userdata, msg):
    global received_messages
    received_messages.append([msg.topic, msg.payload.decode()])
    print_table()


def print_table():
    global received_messages
    headers = ["Topic", "Message"]
    print(tabulate(received_messages, headers=headers, tablefmt="grid"))


client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

broker_address = "broker.emqx.io"
port = 1883

client.connect(broker_address, port, 60)

client.loop_forever()