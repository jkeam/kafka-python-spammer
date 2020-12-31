from kafka import KafkaProducer
from os import getenv

bootstrap_server_host = getenv('KAFKA_BOOTSTRAP_HOST', 'localhost')
bootstrap_server_port = getenv('KAFKA_BOOTSTRAP_PORT', '9092')
topic_name = getenv('TOPIC_NAME', 'my-topic')
times = int(getenv('TIMES', 1))

uri = f'{bootstrap_server_host}:{bootstrap_server_port}'
print(f'Kafka Bootstrap Server: {uri}')
print(f'Topic: {topic_name}')
producer = KafkaProducer(bootstrap_servers=uri)
for i in range(times):
    producer.send(topic_name, key=b'message', value=b'Sending Message')
print(f'Sent {times} messages')
producer.flush()
