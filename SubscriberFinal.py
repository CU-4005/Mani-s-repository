#Library used to create the subscriber
import paho.mqtt.client as mqtt
#Library used for table format
from tabulate import tabulate


received_messages = [] #this is a list which stores messages received 

#A callback function for when the subscriber is connected to the MQTT broker 
def on_connection(client, userdata, flags, rc):
    if rc == 0:
        print("you connected to a broker")
    
        #this are the topics which we are subscribing to
        #these are what we want to receive from the broker
        client.subscribe("Amplitude")
        client.subscribe("Fuel")
        client.subscribe("Acceleration")
        client.subscribe("Frequency")
    else:
        print(f"Connection failed with code {rc}")

#this function will print the messages in a table format 
def on_message_received(client, userdata, msg):
    global received_messages
    received_messages.append([msg.topic, msg.payload.decode()])
    print_table()


def print_table():
    global received_messages
    headers = ["Topic", "Message"]
    print(tabulate(received_messages, headers=headers, tablefmt = "grid"))

#making a client allows us to communicate with the MQTT broker
client = mqtt.Client()

#assigning callback functions to client events
client.on_connect = on_connection
client.on_message = on_message_received

#the address for the broker we are using with the port number
broker_address = "broker.emqx.io"
port = 1883
#command for connecting to the MQTT broker
client.connect(broker_address, port, 60)
#Loops the MQTT client loop to bring in new messages published
client.loop_forever()