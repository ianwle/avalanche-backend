from kafka import KafkaConsumer

import sys

consumer = KafkaConsumer("twitter")
try:
    for message in consumer:
        print(message)
except KeyboardInterrupt:
    sys.exit()