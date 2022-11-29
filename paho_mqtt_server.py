# python 3.10

import random
import time
from openweathermap_api import get_weather_openweathermap
from paho.mqtt import client as mqtt_client

broker = 'broker.emqx.io'
port = 1883
topic = "python/mqtt4"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = 'emqx'
password = 'public'


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port, 20)
    return client


def publish(client):
    while True:
        response = get_weather_openweathermap()
        msg = response
        print(333, str(msg))
        result = client.publish(topic, str(msg))

        status = result[0]
        if status == 0:
            print(f"Send weather to topic `{topic}`")
        else:
            print(f"Failed to send weather to topic {topic}")


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    run()
