import time
import json
import random
import paho.mqtt.client as mqtt

BROKER = "broker.hivemq.com"
PORT   = 1883
TOPIC  = "cubesat/attitude"

client = mqtt.Client()
client.connect(BROKER, PORT, 60)

print("Publishing attitude every 3 seconds...")

try:
    while True:
        roll  = random.uniform(-45, 45)
        pitch = random.uniform(-45, 45)
        yaw   = random.uniform(0, 360)

        payload = json.dumps({
            "roll":  round(roll, 2),
            "pitch": round(pitch, 2),
            "yaw":   round(yaw, 2)
        })

        client.publish(TOPIC, payload)
        print("sent:", payload)

        time.sleep(3)  # <-- 3-second interval

except KeyboardInterrupt:
    print("\nStopped by user.")
finally:
    client.disconnect()
    print("Disconnected from MQTT.")

