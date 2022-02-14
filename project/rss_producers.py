from ensurepip import bootstrap
from kafka import KafkaProducer

producer = KafkaProducer()

for _ in range(2):
    producer.send('twitter', b'Some_message_bytes')
    
future = producer.send('twitter', b'Message sent here')
result = future.get(timeout=60)

