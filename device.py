import random
import time

import paho.mqtt.client as mqtt
client = mqtt.Client(protocol=mqtt.MQTTv31)
client.connect("localhost")
print("test")
i=0

while True:
    i+=1;
    temperature = random.randint(20, 30)
    humidity = random.randint(30, 60)
    message = "T:"+str(temperature)+", H:"+str(humidity)
    client.publish("appiot/temp", message)
    time.sleep(2)
    # time.sleep(12 * 60 * 60) # for eqch 12 hours
    if i == 2 :
      print("done")
      break