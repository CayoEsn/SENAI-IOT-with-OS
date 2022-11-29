# python3.10

import ast
import random
from paho.mqtt import client as mqtt_client

broker = 'broker.emqx.io'
port = 1883
topic = "python/mqtt4"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'
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


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        response_json = ast.literal_eval(msg.payload.decode())

        print("\nTemperature (in Celsius unit) = " +
              str('{:.2f}'.format(float(response_json['temperature_kelvin']) - 273.15)) +
              "\natmospheric pressure (in hPa unit) = " +
              str(response_json['atmospheric_pressure']) +
              "\nhumidity (in percentage) = " +
              str(response_json['humidity']) +
              "\ndescription = " +
              str(response_json['description']))

    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()
