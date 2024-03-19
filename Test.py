import random
import time
import paho.mqtt.client as mqtt

broker_address = "mqtt.eclipseprojects.io"
port = 8883
parent_topic = "wave"

client = mqtt.Client("RandomWaveValues")
client.connect(broker_address, port)

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
    else:
        print("Failed to connect to MQTT broker, return code", rc)

client.on_connect = on_connect

def generate_and_publish():
    tries = 0
    while tries < 10:
        wave_speed = random.uniform(1, 10)
        wave_direction = random.randint(0, 360)
        wave_amplitude = random.uniform(0.1, 1.0)
        frequency = random.uniform(0.5, 2.0)
        
        client.publish(f"{parent_topic}/wave_speed", str(wave_speed), qos=1)
        client.publish(f"{parent_topic}/wave_direction", str(wave_direction), qos=1)
        client.publish(f"{parent_topic}/wave_amplitude", str(wave_amplitude), qos=1)
        client.publish(f"{parent_topic}/frequency", str(frequency), qos=1)
        
        tries += 1
        time.sleep(5)

try:
    generate_and_publish()
except KeyboardInterrupt:
    print("Stopping...")
    client.disconnect()