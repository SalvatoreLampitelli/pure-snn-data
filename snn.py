from pythonosc.udp_client import SimpleUDPClient
import time

# Send to localhost, port 8000
osc = SimpleUDPClient("127.0.0.1", 8000)

for i in range(5):
    print("Sending OSC: /drum", i)
    osc.send_message("/drum", i)
    time.sleep(1)