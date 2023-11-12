import time
import paho.mqtt.client as mqtt
def on_connect(client, userdata, flags, rc):
 print("Connected with result code "+str(rc))
 client.subscribe("appiot/temp")
def on_message(client, userdata, msg):
 print(msg.topic+" "+str(msg.payload))
client = mqtt.Client(protocol=mqtt.MQTTv31)
size = 0
times = 0
def on_message(client, userdata, msg):
    global size 
    global times
    print(str(msg.payload.decode("utf-8")))
    size += len(msg.payload)
    times += 1
client.on_connect = on_connect
client.on_message = on_message
client.connect("localhost", 1883, 60)
client.loop_start()
print(size)
time.sleep(30)
print(str(times)+" message recived")
print("the total size of all the messages is "+str(size))
client.loop_stop()

